import googlemaps

apiKey="AIzaSyCRe9Kyry9O0AFeM9IDGfmggxTjxQN8VQk"

gmap=googlemaps.Client(key=apiKey)
result=gmap.places_nearby(location="43.7768,11.2586",radius=40000,type='cafe')
print(result)