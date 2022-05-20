
from datetime import datetime
from dateutil.relativedelta import relativedelta
import geocoder # pip install geocoder
import requests


class AiHotel:

    def __init__(self,hotelApi,cityLocatorApi,cityName,n,budget):
        self.hotelApi=hotelApi
        self.cityLocatorApi=cityLocatorApi
        self.cityName=cityName
        self.numDays=n
        self.budget=budget
        self.hotel=[]
        self.init=False


    def GetMyHotel(self):
        if self.init:
            return self.hotel

        self.__GetHotel()
        return self.hotel


    def __GetHotel(self):
        
        #Get Random Start Date and End Date 
        currentTimeDate = datetime.now() + relativedelta(months=2)
        endTimeDate=currentTimeDate+relativedelta(days=self.numDays)
        currentTime = currentTimeDate.strftime('%Y-%m-%d')
        endTime = endTimeDate.strftime('%Y-%m-%d')

        #Get the city Lat,Lng 
        g = geocoder.bing(self.cityName, key=self.cityLocatorApi)
        results = g.json
        lat=results['lat']
        lng=results['lng']
        

        #Define Budget
        Min=0
        Max=int(100000/self.numDays)
        if(self.budget==0):Max=int(5000/self.numDays)
        elif(self.budget==1):Max=int(10000/self.numDays)
        elif(self.budget==2):Max=int(25000/self.numDays)
        

        url = "https://hotels-com-provider.p.rapidapi.com/v1/hotels/nearby"
        querystring = {"latitude":str(lat),"currency":"EGP","longitude":str(lng),
                    "checkout_date":endTime,"sort_order":"STAR_RATING_HIGHEST_FIRST",
                    "checkin_date":currentTime,"adults_number":"1",
                    "locale":"en_US","price_min":"0","price_max":str(Max)}
        headers = {
            "X-RapidAPI-Host": "hotels-com-provider.p.rapidapi.com",
            "X-RapidAPI-Key": self.hotelApi
        }
    
        response = requests.request("GET", url, headers=headers, params=querystring).json()["searchResults"]["results"][0]
        long=response["coordinate"]["lon"]
        latit=response["coordinate"]["lat"]
        name=response["name"]
        pic=response["optimizedThumbUrls"]["srpDesktop"]
        pic=pic[:pic.index("jpg") + len("jpg")]
        price=response["ratePlan"]["price"]["fullyBundledPricePerStay"]
        night_price=response["ratePlan"]["price"]["current"]
        #The Hotel also has
        # ["starRating"] <= Star Rating
        # ["address"]    <= Exact Address of the Hotel
        # ["ratePlan"]["price"]["fullyBundledPricePerStay"] <= Full price of Stay at hotel in Egyptian Pound
        # ["neighbourhood"] <= Name of Neighbourhood
        # ["landmarks"] <= Famous landmarks close to Hotel
        #["coordinate"]["lon"] <=
        #["coordinate"]["lat"] <=
        #["name"] <= Name of Hotel
        # ["optimizedThumbUrls"]["srpDesktop"] <= Pic of Hotel
        
        self.hotel={"name":name,"lat":str(latit),"long":str(long),"total_price":price,"night_price":night_price,"pic_url":pic}
        self.init=True



    

        