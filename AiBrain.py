

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
        self.userPriorities=dict(sorted(userPriorities.items(), key=lambda x: x[1], reverse=True))
        self.__getPlaces()
        self.__calculatePriority()



       
    def Initialize(self):
        if self.init:
            return
        for place in self.places:
            self.__calculateHeuristic(place)

        self.init=True  
        
         
    def GetData(self):
        num=len(self.rest)
        if(num>30):
            num=30
        
        data={}
        data['places']=self.places
        data['restaurant']=self.rest[0:num-1]
        
        return data
    


    def __calculatePriority(self):
        
        self.__debug()
        for place in self.places:
            priority=0
            for type in place['types']:
                if type in self.userPriorities:
                    priority+=float(self.userPriorities[type])
            if priority==0:
                priority=1
            place['priority']=priority
            
       

    

    def __calculateHeuristic(self,place):
        score=1

        try:score*=float(place['rating'])
        except:pass
        try:score*=float(place['priority'])
        except:pass

        place['score']=score




    def __getPlaces(self):

        gmap=googlemaps.Client(key=self.configurations['places_Api'])
        places=[]
        rest=[]
        position=self.hotel['lat']+","+self.hotel['long']
        
        for x in self.userPriorities:
            
            if self.userPriorities[x] !=0:
                places.append(gmap.places_nearby(position,self.configurations['radius'],type=x))

        rest.append(gmap.places_nearby(position,self.configurations['radius'],type="restaurant"))
        self.places=self.__filter(places)
        print(len(self.places))
        self.rest=self.__filter(rest)




    def __filter(self,data):
        tempArray=[]

        for x in data:
            for y in x['results']:
                y['score']=0
                if "rating" not in y:
                    y['rating']=1
                try:
                    y.pop('icon')
                    y.pop('icon_background_color')
                    y.pop('icon_mask_base_uri')
                    y.pop('opening_hours')
                except:pass
                tempArray.append(dict(y))


        return tempArray


    def __debug(self):
        with open('tests/placesarray.json', 'w') as outfile:
             outfile.write(json.dumps(self.places))

        with open('tests/prio.json', 'w') as outfile:
             outfile.write(json.dumps(self.userPriorities))     