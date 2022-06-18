

import requests


def GetCityImage(cityName,config):  
    url = "https://contextualwebsearch-websearch-v1.p.rapidapi.com/api/Search/ImageSearchAPI"

    querystring = {"q":cityName,"pageNumber":"1","pageSize":"1","autoCorrect":"true"}

    headers = {
    "X-RapidAPI-Key": config["X-RapidAPI-Key"],
    "X-RapidAPI-Host": config["X-RapidAPI-Host"]
     }

    response = requests.request("GET", url, headers=headers, params=querystring).json()["value"][0]["url"]

    return response



def FilterPriorities(prio,config):
    temp={}

    for p in prio.items():
        if p[1] !=0:
            for x in config["prio"][p[0]]:
                temp[x]=p[1]
        
    return temp


