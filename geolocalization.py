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

geolocator = gp.geocoders.Nominatim(user_agent="my_request")            # Using a module from geopy we can geocode user's adress
user_location = geolocator.geocode(adress)                              # into coordinates, latitude and longitude. 
user_coords = (user_location.latitude, user_location.longitude)
print((user_location.latitude, user_location.longitude))

### Establishing a list of nearby grocery stores ### 

search_string = 'Supermarket'                         
distance = radius
grocery_stores_list = []

grocery_request = map_client.places_nearby(                             # Using one of google maps API, Places API, we can requests for
    location = user_coords,                                             # nearby places around our coordinates following our keyword.
    keyword = search_string,                                            # In this very example, we're looking for supermarkets, 
    name = 'Supermarket',                                               # explaining the keyword selected. 
    radius = distance, 
)

grocery_stores_list.extend(grocery_request.get('results'))
next_page_token = grocery_request.get('next_page_token')

while next_page_token:                                                  # Places API restricts answers for 20 by pages and 60 in total,
  time.sleep(5)                                                         # to avoid the 20 limits, we need to take in account all of the pages,
  grocery_request = map_client.places_nearby(                           # However, the 60 responses limit still represents an issue not solved yet
    location = user_coords,                                             # In order to bypass this issue, we limit our search radius to prevent 
    keyword = search_string,                                            # more than 59 answers from the places_nearby request. 
    name = 'Supermarket',
    radius = distance,
    page_token = next_page_token 
  )
  grocery_stores_list.extend(grocery_request.get('results'))
  next_page_token = grocery_request.get('next_page_token') 

df = pd.DataFrame(grocery_stores_list)

grocery_names = df.filter(['name'])
grocery_stores = df.filter(['geometry'])

n = len(grocery_names)

grocery_stores_locations = [[
    grocery_names['name'][i],
    grocery_stores['geometry'][i]['location']['lat'],
    grocery_stores['geometry'][i]['location']['lng']] for i in range(n)]

grocery_stores_coords = [(
    grocery_stores_locations[i][1],
    grocery_stores_locations[i][2]) for i in range(n)]


### Distance and trip time estimation ### 

trip_list = []

for i in range(n) :                               # For each grocery store found nearby the user, we establish 
  trip_list.append(map_client.distance_matrix(    # both the distance and the time using the Google Maps 
      origins = user_coords,                      # distance matrix API. 
      destinations = grocery_stores_coords[i]
  ))

trip_df = pd.DataFrame(trip_list)                 # We render the results in a DataFrame for a better work environment.

travel_informations = [(                                                              # Using the data, we extract the informations
    grocery_names['name'][i],                                                         # needed, the name and both the distance
    trip_df['rows'][i][0]['elements'][0]['distance']['text'],                         # and the travel time, as a list.
    trip_df['rows'][i][0]['elements'][0]['duration']['text']) for i in range(n)]

print(travel_informations)



## Function of geolocalization 

def find_supermarkets(adress, radius = 4e3):
  '''
  return a list of supermarkets with the name, the distance and the estimated travel time
  '''
  
  # We determine the localisation of the user
  geolocator = gp.geocoders.Nominatim(user_agent="my_request")  
  user_location = geolocator.geocode(adress)                          
  user_coords = (user_location.latitude, user_location.longitude)
  
  search_string = 'Supermarket'                         
  distance = radius
  grocery_stores_list = []
  
  # We determine the nearest supermarkets
  grocery_request = map_client.places_nearby(location = user_coords,                                            
                                             keyword = search_string,                                            
                                             name = 'Supermarket',                                               
                                             radius = distance)
  grocery_stores_list.extend(grocery_request.get('results'))
  next_page_token = grocery_request.get('next_page_token')
  
  while next_page_token:
    time.sleep(5)
    grocery_request = map_client.places_nearby(location = user_coords,
                                               keyword = search_string,
                                               name = 'Supermarket',
                                               radius = distance,
                                               page_token = next_page_token)
    grocery_stores_list.extend(grocery_request.get('results'))
    next_page_token = grocery_request.get('next_page_token') 

  # The list is converted as a dataframe
  df = pd.DataFrame(grocery_stores_list)
  
  grocery_names = df.filter(['name'])
  grocery_stores = df.filter(['geometry'])
  
  n = len(grocery_names)
  
  grocery_stores_locations = [[grocery_names['name'][i],
                               grocery_stores['geometry'][i]['location']['lat'],
                               grocery_stores['geometry'][i]['location']['lng']] for i in range(n)]
  
  grocery_stores_coords = [(grocery_stores_locations[i][1],
                            grocery_stores_locations[i][2]) for i in range(n)]
                            

  # We determine the distance and the travel time of each supermarket
  trip_list = []

  for i in range(n): 
    trip_list.append(map_client.distance_matrix(origins = user_coords,
                                                destinations = grocery_stores_coords[i]))
  
  trip_df = pd.DataFrame(trip_list) 
  
  travel_informations = [(grocery_names['name'][i], 
                          trip_df['rows'][i][0]['elements'][0]['distance']['text'],
                          trip_df['rows'][i][0]['elements'][0]['duration']['text']) for i in range(n)]
                          
  return travel_informations
  
  
# Test : 

# c = find_supermarkets('27 Boulevard Thomas Gobert, Palaiseau 91120')


