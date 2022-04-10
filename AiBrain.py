
#   categories 

    #           -rating                     (from 0.0 to 5.0) 
    #           -price_level                0=Free 1=Inexpensive 2=Moderate 3=Expensive 4=Very Expensive
    #           -opening_hr
        #            -open_now              A boolean value indicating if the place is open at the current time.              
        #            -periods               An array of opening periods covering seven days, starting from Sunday, in chronological order
        #            -weekday_text          An array of strings describing in human-readable text the hours of the place.
    #           -types                      Contains an array of feature types describing the given result. See the list of supported types.
    #           -user_ratings_total         The total number of reviews, with or without text, for this place.
    #           -geometry
        #            -location              "lat": , "lng":
        #            -viewport

               

# usage
    #calculate distance using geocodes
    #give points to each category
    #give point to each category given specific times
    #points related to rating
    #data closed if valid -> give a negative point or remove

#algorithm steps
    #   - calculate heuristic for each place
            # loop here
    #   - choose the one with the highest heuristic
    #   - recalculate heuristic given new parameters
     



#heuristic 
#       Rating*(types*priority)*(Best performing hr)*(price Level)/Distance

       


from copy import deepcopy
import json
from operator import attrgetter




class AiBrain:

    def __init__(self,places,userPriorities,hotel,days):
        self.places=[]
        self.rest=[]
        self.hotel=hotel
        self.days=days
        self.init=False
        with open('Config.json') as json_file:
            self.configurations = json.load(json_file)

        self.__filterTypes(places)
        self.__calculatePriority(userPriorities)



       
    def Initialize(self):
        if self.init:
            return
        for place in self.places:
            self.__calculateHeuristic(place)

        self.__modelInit()
        self.init=True  
        
         
    def getData(self):
        num=len(self.rest)
        if(num>30):
            num=30
        return self.places,self.rest[0:num-1]
    





    def __calculatePriority(self,userPriorities):
        priority=0
        for place in self.places:
            priority=0
            for type in place['types']:
                if type in userPriorities:
                    priority+=float(userPriorities[type])
            self.place['priority']=priority
       

    def __calculateHeuristic(self,place):
        score=1

        try:score*=float(place['rating'])
        except:pass
        try:score*=float(place['priority'])
        except:pass

        place['score']=score


    def __modelInit(self):
        temp=[]
        num=len(self.places)

        if(num>150):
            num=150

        listscore=deepcopy(self.places)
        sorted(listscore, key=attrgetter('score'),reverse=True)

    

        for i in range (0,num):
            temp.append(listscore[i])
        for i in range (0,num):
            if (self.places[i]) not in temp:
                temp.append(self.places[i])

        self.places=temp


#appends restaurants in rest List and all important types in places list

    def __filterTypes(self,places):
        for place in places:
            for type in place['types']:
                if (type=="restaurant"):
                    self.rest.append(place)
                    break
                if type in self.configurations['types']:
                    self.places.append(place)
                    break
                
