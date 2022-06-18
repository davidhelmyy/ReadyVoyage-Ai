

import googlemaps
import json



class AiBrain:

    def __init__(self,userPriorities,hotel,configurations):
        self.places=[]
        self.rest=[]
        self.hotel=hotel
        self.init=False
        self.configurations =configurations
        self.userPriorities=userPriorities
        self.one=[]
        self.two=[]
        self.__getPlaces()
       

       
    def Initialize(self):

        if self.init:
            return

        flag=True

        for place in self.places:
            flag=True
            for type in place['types']:
                if flag and type in self.configurations['best_time']:
                    index=self.configurations['best_time'][type]
                    if index==0:
                        self.one.append(place)
                        flag=False
                    elif index==1:
                        self.two.append(place)
                        flag=False
                    else :    
                        self.two.append(place)
                        self.one.append(place)
                        flag=False

       
     
        self.init=True  

    def CreateTrip(self,numOfDays):

        numTemp=int(numOfDays)
        if(len(self.places)<(numOfDays*3)):
            numTemp=int(len(self.places)/(numOfDays*3))

        trip={}
        listTemp=[]
        sizeOne=len(self.one)
        sizeTwo=len(self.two)
       
        self.one=sorted(self.one, key=lambda x: x['score'], reverse=True)    
        self.two=sorted(self.two, key=lambda x: x['score'], reverse=True)

        if(sizeOne>numOfDays*2):
            listTemp.append(self.one[numOfDays*2:])
        

        if(sizeTwo>numOfDays):
            listTemp.append(self.two[numOfDays:])
       

  
        
        indexTemp=0
        day="Day " 
        for i in range (0,numTemp):
            temp=[]
            if(sizeOne>1):
                temp.append(self.one[(i*2)])
                sizeOne-=1
            else:
                temp.append(listTemp[indexTemp])
                indexTemp+=1

            if(sizeOne>1):
                temp.append(self.one[(i*2)+1])
                sizeOne-=1
            else:
                temp.append(listTemp[indexTemp])
                indexTemp+=1
            
            if(sizeTwo>0):
                temp.append(self.two[i])
                sizeTwo-=1

            else:
                temp.append(listTemp[indexTemp])
                indexTemp+=1

            temp.append(self.rest[i])



            trip[day+str((i+1))]=temp
        
        
        if(numTemp<numOfDays):
            index=0
            for i in range (numTemp,numOfDays):
                trip[day+str((i+1))]=trip[day+str((index+1))]
                index+=1



        return trip


    


    def __calculatePriority(self,place):  
        priority=0
        for type in place['types']:
            if type in self.userPriorities:
                priority+=float(self.userPriorities[type])

        if priority==0:
            priority=1
        place['priority']=priority

        return place
     
    def __calculateHeuristic(self,place):
        score=1

        try:score*=float(place['rating'])
        except:pass
        try:score*=float(place['priority'])
        except:pass

        place['score']=score
        return place

    def __getPlaces(self):

        gmap=googlemaps.Client(key=self.configurations['places_Api'])
        places=[]
        rest=[]
        position=self.hotel['lat']+","+self.hotel['long']
        
        for x in self.userPriorities:
            
            if self.userPriorities[x] !=0:
                places.append(gmap.places_nearby(position,self.configurations['radius'],type=x))

        rest.append(gmap.places_nearby(position,self.configurations['radius'],type="restaurant"))
        self.places=self.__FilterAndCalculations(places)
        # For debuging
        print(len(self.places))

        self.rest=self.__FilterAndCalculations(rest,True)

    def __FilterAndCalculations(self,data,flag=False):

        tempArray=[]
        
       
        for x in data:
            for y in x['results']:
                tempPlace={}
                tempPlace['score']=0
                tempPlace['name']=y['name']
                tempPlace['lat']=y['geometry']['location']['lat']
                tempPlace['lng']=y['geometry']['location']['lng']
                try:
                    tempPlace['types']=y['types']
                except:pass
                try:
                    tempPlace['rating']=y['rating']
                except:
                    tempPlace['rating']=1
                try:
                    tempPlace['user_ratings_total']=y['user_ratings_total']
                except:pass
                try:
                    tempPlace['photos']=y['photos']
                except:pass

                if(not flag):
                    tempPlace=self.__calculatePriority(tempPlace)
                    tempPlace=self.__calculateHeuristic(tempPlace)

                
                tempArray.append(dict(tempPlace))


        return tempArray
 
    def __debug(self):
        with open('tests/placesarray.json', 'w') as outfile:
             outfile.write(json.dumps(self.places))

        with open('tests/prio.json', 'w') as outfile:
             outfile.write(json.dumps(self.userPriorities))     