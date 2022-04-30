############# Geolocalization ################

### Packages Import ###

import googlemaps as gm 
import pandas as pd
import geopy as gp
import time 

### Variables Initialization ### 

API_Key = 'AIzaSyDgsXVXBLQ9FEN72hXLHtTVe_-nnhghhds'
map_client = gm.Client(API_Key)
adress = '27 Boulevard Thomas Gobert, Palaiseau 91120'
radius = 4e3

### User's coordinates ### 

geolocator = gp.geocoders.Nominatim(user_agent="my_request")
user_location = geolocator.geocode(adress)
user_coords = (user_location.latitude, user_location.longitude)
print((user_location.latitude, user_location.longitude))

### Establishing a list of nearby grocery stores ### 

search_string = 'grocery'
distance = radius
grocery_stores_list = [ ]

grocery_request = map_client.places_nearby(
    location = user_coords,
    keyword = search_string,
    name = 'Supermarket',
    radius = distance, 
)

grocery_stores_list.extend(grocery_request.get('results'))
next_page_token = grocery_request.get('next_page_token')

while next_page_token:
  time.sleep(5)
  grocery_request = map_client.places_nearby(
    location = user_coords,
    keyword = search_string,
    name = 'Supermarket',
    radius = distance, 
    page_token = next_page_token 
  )
  grocery_stores_list.extend(grocery_request.get('results'))
  next_page_token = grocery_request.get('next_page_token') 

grocery_stores_list

df = pd.DataFrame(grocery_stores_list)
df

grocery_names = df.filter(['name'])
grocery_stores = df.filter(['geometry'])
n = len(grocery_names)
grocery_stores_locations = [[grocery_names['name'][i],grocery_stores['geometry'][i]['location']['lat'],grocery_stores['geometry'][i]['location']['lng']] for i in range(n)]
grocery_stores_coords = [(grocery_stores_locations[i][1],grocery_stores_locations[i][2]) for i in range(n)]
grocery_stores_locations

### Distance and trip time estimation ### 

trip_list = []

for i in range(n) : 
  trip_list.append(map_client.distance_matrix(
      origins = user_coords,
      destinations = grocery_stores_coords[i]
  ))

trip_df = pd.DataFrame(trip_list)
trip_df

travel_informations = [(grocery_names['name'][i],trip_df['rows'][i][0]['elements'][0]['distance']['text'],trip_df['rows'][i][0]['elements'][0]['duration']['text']) for i in range(len(place_ids))]
travel_informations 





