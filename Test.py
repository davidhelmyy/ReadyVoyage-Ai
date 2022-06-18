
from AIModel import AIModel



def initData():
    userPriorities={
        "Casino":7,
        "Stadium":3,
        "TouristicPlaces":8,
        "Museums":10
   }
    numDays=5
    budget=1
    cityName="Milan"

    return userPriorities,cityName,numDays,budget



userPriorities,cityName,numDays,budget=initData()
Model=AIModel(userPriorities,cityName,numDays,budget)
jsonFile=Model.RunAI()


with open('tests/test_results.json', 'w') as outfile:
    outfile.write(jsonFile)