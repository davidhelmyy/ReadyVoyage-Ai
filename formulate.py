import json
class Formula:
       
       def __init__(self,age,gender,preferences,userID):
            self.age=age
            self.gender=gender
            self.preferences=preferences
            self.init=False
            self.userID=userID
            self.formula=[]
       
       def GetMyFormula(self):
            if self.init:
                return self.userID,self.formula

            self.__formula()
            return self.userID,self.formula
        
        
       def __formula(self):
            final=[0,0,0,0,0,0]
            if self.age <=25:final[0]=100
            elif self.age >25 and self.age <=45:final[0]=300
            elif self.age >45 :final[0]=500

            if self.gender=="M":final[1]=100
            elif self.gender =="F":final[1]=300
            
            if self.predicted.budget <=10000:final[2]=0
            elif self.predicted.budget >10000 and self.predicted.budget <=20000:final[2]=500
            elif self.predicted.budget >20000 and self.predicted.budget <=50000:final[2]=1000
            elif self.predicted.budget >50000 :final[2]=1500

            final[3]=(self.preferences.AmusementParks+self.preferences.Zoo+self.preferences.GreenAreas+self.preferences.Aquarium+self.preferences.Stadium)*(300/5)
            
            final[4]=(self.preferences.Bar+self.preferences.NightClub+self.preferences.Casino+self.preferences.Cafe+self.preferences.Restaurant+self.preferences.Mall)*(300/6)
            
            final[5]=(self.preferences.TouristicPlaces+self.preferences.ReligousLocations+self.preferences.Museum)*(300/3)

            self.formula=final
            self.init=True  