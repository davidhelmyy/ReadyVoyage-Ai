
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

       


from math import radians, cos, sin, asin, sqrt



class AiBrain:

    def __init__(self,places,userPriorities,hotel,days):
        self.places=places
        self.plan=[]
        self.rest=[]
        self.hotel=hotel
        self.days=days
        self.__calculatePriority(userPriorities)
        


    def __calculatePriority(self,userPriorities):
        priority=0
        for place in self.places:
            priority=0
            for type in place['types']:
                if type in userPriorities:
                    priority+=float(userPriorities[type])
            self.place['priority']=priority
       

    def __calculateDistance (self,lat1,long1,lat2,long2):
        lon1 = radians(float(long1))
        lon2 = radians(float(long2))
        lat1 = radians(float(lat1))
        lat2 = radians(float(lat2))
        
        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    
        c = 2 * asin(sqrt(a))
        
        # Radius of earth in kilometers. Use 3956 for miles
        r = 6371
        
        # calculate the result
        return(c * r)
    

    def __calculateHeuristic(self,place,current,time):
        score=0

        try:score+=float(place['rating'])
        except:pass
        try:score+=float(place['priority'])
        except:pass

        try:score+=float(place['price'])
        except:pass

        try:score+=self.__calculateBestTime(place,time)
        except:pass

        try:score=score/self.__calculateDistance(place['geometry']['location']['lat'],place['geometry']['location']['lng'],
        current['geometry']['location']['lat'],current['geometry']['location']['lng'])
        except:pass

        return score


    def __calculateBestTime(self,place,time):
        return

    def __createPlan(self): 
        visited=[]

        for i in range (self.days):
            self.plan.append(self.__getDayPlan(self.hotel,visited))
            self.rest.append(self.__getRestaurant(self.plan[i][1],visited))
        for i in range (len(self.plan)):
            self.planID.append([self.plan[i][0]["place_id"],self.plan[i][1]["place_id"],self.plan[i][2]["place_id"]])

    

    def __getDayPlan(self,current,visited):
        plan=[]
        for i in range (3):
            score=[]
            for place in self.places:
                score.append(self.__calculateHeuristic(place,current,i))
            temp=self.__findMax(score)
            while self.places[temp] in visited:
                score[temp]=0
                temp=self.__findMax(score)

            plan.append(self.places[temp])
            visited.append(self.places[temp])
            current=self.places[temp]
        return plan
          


    def __findMax(self,scores):
        max=scores[0]
        index=0
        i=0
        for score in scores:
            if max<score:
                max=score
                index=i
            i+=1
        return index

    def __getRestaurant(self,current,visited):
        distance=[]
        id=[]
        for place in self.places:
            if place not in visited:
                if "restaurant" in place['types'] :
                    id.append(place['place_id'])
                    distance.append(self.__calculateDistance(place['geometry']['location']['lat'],place['geometry']['location']['lng'],current['geometry']['location']['lat'],current['geometry']['location']['lng']))
        temp=self.__findMin(distance)
        return id[temp]

    def __findMin(self,array):
        min=array[0]
        index=0
        i=0
        for x in array:
            if x<min:
                min=x
                index=i
            i+=1


    def createMyPlan(self):
        self.__createPlan
        print ("plan creation finished")
        
    def getMyPlan(self):
        return self.plan,self.rest
    