import json
import numpy as np


class ML1:
       
       def __init__(self,user_trips,age,gender,All_trips):
            self.user_trips=user_trips
            self.age=age
            self.gender=gender
            self.All_trips=All_trips
            self.init=False
            with open('Config.json') as json_file:
                self.configurations = json.load(json_file)
            self.recommendation=[]
            self.predicted={}
            self.formula=[]
       
       def GetMyRecommendations(self):
            if self.init:
                return self.recommendation

            self.__GetRecommendation()
            return self.recommendation
        
        
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
              
            final[3]=(self.predicted.preferences.AmusementParks+self.predicted.preferences.Zoo+self.predicted.preferences.GreenAreas+self.predicted.preferences.Aquarium+self.predicted.preferences.Stadium)*(300/5)
            
            final[4]=(self.predicted.preferences.Bar+self.predicted.preferences.NightClub+self.predicted.preferences.Casino+self.predicted.preferences.Cafe+self.predicted.preferences.Restaurant+self.predicted.preferences.Mall)*(300/6)
            
            final[5]=(self.predicted.preferences.TouristicPlaces+self.predicted.preferences.ReligousLocations+self.predicted.preferences.Museum)*(300/3)

            self.formula=final  
           
           
           
           
           
       def __get_prediction(self):
            total_number_of_trips=len(self.user_trips)
            array=[]
            array.append ([0,0,0,0])
            for i in range (0,14):array.append([0,0,0])
            for i in range(0,total_number_of_trips):
                if(self.user_trips[i].rating>7):
                    temp=json.loads(self.user_trips[i].preferences)
                    if(temp["budget"]<=10000):array[0][0]=array[0][0]+1
                    elif(temp["budget"]>10000 and temp["budget"]<=20000):array[0][1]=array[0][1]+1
                    elif(temp["budget"]>20000 and temp["budget"]<=50000):array[0][2]=array[0][2]+1
                    elif(temp["budget"]>50000):array[0][3]=array[0][3]+1

                    for j in range(1,len(myfields)):
                        if(int(temp["preferences"][self.configurations["myfields"][j]])==0):array[j][0]=array[j][0]+1
                        elif(int(temp["preferences"][self.configurations["myfields"][j]])<=5):array[j][1]=array[j][1]+1
                        elif(int(temp["preferences"][self.configurations["myfields"][j]])>5):array[j][2]=array[j][2]+1

            predicted={}
            number=array[0].index(max(array[0]))
            if number==0:predicted["budget"]=5000
            elif number==1:predicted["budget"]=15000
            elif number==2:predicted["budget"]=35000
            elif number==3:predicted["budget"]=70000
              
            temp_dict={}
            for x in range(1,len(myfields)):
                number=array[j].index(max(array[j]))
                if number==0:temp_dict[self.configurations["myfields"][j]]=0
                elif number==1:temp_dict[self.configurations["myfields"][j]]=5
                elif number==2:temp_dict[self.configurations["myfields"][j]]=10
            predicted["preferences"]=temp_dict
            self.predicted= predicted

           
       
       def __GetRecommendation(self):
            self.__get_prediction()       
            self.__formula()
            point1 = np.array(self.formula)
            recommended = []
            for i in range(0,len(self.All_trips)):
                point2 = np.array(self.All_trips[i][1])
                recommended.append(np.linalg.norm(point1 - point2), self.All_trips[i].id)
            recommended.sort(reverse=True)       
            self.recommendation= [recommended[0][0],recommended[1][0],recommended[2].[0]]
            self.init=True
            
            
            
