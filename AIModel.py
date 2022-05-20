

from AiBrain import AiBrain
from AiHotel import AiHotel
import json

class AIModel:
    def __init__(self,userPriorities,cityName,numDays,budget):
        self.hotel=[]
        self.userPriorities=userPriorities
        self.cityName=cityName
        self.numDays=numDays
        self.budget=budget
        
        with open('Config.json') as json_file:
            self.configurations = json.load(json_file)


    #run this fuunction only to get data

    def RunAI(self):
        self.__GetHotel()
        ## returns Json File containing places,restaurant,hotel
        return self.__GetPlan()   

        

    def __GetHotel(self):
        HotelAi=AiHotel(self.configurations['hotel_Api'],self.configurations['cityLocator_Api'],
            self.cityName,self.numDays,self.budget)

        self.hotel=HotelAi.GetMyHotel()
        


    def __GetPlan(self):
       
        
        Ai=AiBrain(self.userPriorities,self.hotel,self.configurations)
        Ai.Initialize()
        data=Ai.GetData()
        data['hotel']=self.hotel
        jsonData=json.dumps(data)
        return jsonData

