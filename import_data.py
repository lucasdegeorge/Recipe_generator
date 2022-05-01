# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:14:38 2022

@author: lucas
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from math import * 

## Data for unit tests 

dict_food = { "name" : ["pasta","rice","tomato"],
              "energy" : [566,615,81.1],
              "saturated_fatty_acid" : [0.34, 0.076, 0.056],
              "carbohydrates" : [23, 31.8,2.49],
              "sugar" : [0.8, 0.2, 2.48],
              "protein" : [4.57, 2.92,0.86],
              "lipid" : [2, 0.41, 0.26],
              }
df_food = pd.DataFrame(dict_food)

df_r1 = pd.DataFrame( { "ingredient" : ["pasta", "tomato"],
                        "quantity" : [150, 2] } )

df_r2 = pd.DataFrame( { "ingredient" : ["rice", "tomato"],
                        "quantity" : [200, 2] } )

df_r3 = pd.DataFrame( { "ingredient" : ["pasta", "rice"],
                        "quantity" : [100, 100] } )

dict_recipes = { "name" : ["tomato_pastas", "tomato_rice", "rice_pastas"],
                 "ingredients" : [ df_r1, df_r2, df_r3 ],
                 "prep_time" : [20, 20, 30],
                 "guests" : [1,1,1]
                }

df_recipes = pd.DataFrame(dict_recipes)

df_s1 = pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                     "quantity" : [20,3,1],
                     "price" : [1, 0.75, 0.4],
                     "expiry_date" : ["","",""]
                         }  ) 

df_s2 =  pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                     "quantity" : [1,12,6],
                     "price" : [0.9, 1.25, 0.6],
                     "expiry_date" : ["","",""]
                         }  ) 

df_s3 =  pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                     "quantity" : [4,16,23],
                     "price" : [1.2, 1, 0.5],
                     "expiry_date" : ["","",""]
                         }  ) 
dict_shops = { "name" : ["Casino", "Leclerc", "Franprix"],
               "adress" : ["","",""],
               "hours" : ["","",""],
               "stocks" : [ df_s1, df_s2, df_s3 ] 
               }
               
df_shops = pd.DataFrame(dict_shops)

grocery = [('Rapidmarket', '6.0 km', '11 mins'), 
           ('G 20 Supermarche', '9.4 km', '11 mins'),
           ('Your Saclay Market supermarket', '4.0 km', '7 mins'),
           ('Alimentation général Proxi', '7.8 km', '13 mins'),
           ('Djouher Market', '6.4 km', '11 mins'),
           ('Franprix', '4.5 km', '8 mins'),
           ('Superette De La Gare', '5.7 km', '9 mins'),
           ('Carrefour Express', '10.3 km', '11 mins')]

