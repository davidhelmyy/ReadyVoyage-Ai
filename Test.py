
from AIModel import AIModel



def initData():
    userPriorities={
        "casino":7,
        "night_club" :5,
       "stadium":3,
        "tourist_attraction":8
   }

    #userPriorities={'tourist_attraction':7}
    numDays=7
    budget=1
    cityName="italy"

    return userPriorities,cityName,numDays,budget



userPriorities,cityName,numDays,budget=initData()
Model=AIModel(userPriorities,cityName,numDays,budget)
jsonFile=Model.RunAI()


with open('tests/test_results.json', 'w') as outfile:
    outfile.write(jsonFile)