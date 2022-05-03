# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 09:14:38 2022

@author: lucas
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from math import * 
import random as rd

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

######## Ingredients Data #########

### Vegetables
dict_vegetables = {"name" : ['Artichoke','Asparagus','Avocado','Beetroot','Broccoli','Carrot','Celeriac','Courgette ','Cucumber','Haricot','Lentil','Tomato'],
                   "energy" : [25.2, 26.6, 205, 42.8, 37.6, 18.9, 26.2, 15.5, 15.6, 112, 127, 81.1],
                   "protein" : [1.2, 2.69, 1.56, 1.74, 2.5, 0.55, 0.94, 0.93, 0.64, 6.75, 10.1, 0.86],
                   "carbohydrates" : [3.02, 1.73, 0.83, 9.1, 1.23, 2.6, 4.32, 1.4, 2.54, 12, 16.2, 2.49 ],
                   "sugar" : [0.8, 0.81, 0.4, 6.76, 0.8, 1.3, 1.2, 1.39, 1.67, 0.3, 0.2, 2.48],
                   "lipid" : [0, 0.32, 20.6, 0.24, 0.4, 0, 0, 0.36, 0.11, 1.1, 0.58, 0.26]
}
                      
df_vegetables = pd.DataFrame(dict_vegetables)
#print(df_vegetables)

### Fruits 
dict_fruits = {"name" : ['Apple', 'Apricot', 'Banana', 'Blueberry', 'Blackberry', 'Cherry', 'Clementine', 'Melon', 'Strawberry', 'Watermelon' ],
               "energy" : [54.9, 45.9, 90.5, 57.7, 47.3, 55.7, 47.3, 62.7, 38.6, 38.9],
               "protein" : [0, 0.81, 1.06, 0.87, 1.13, 0.81, 0.81, 1.13, 0.63, 0.69],
               "carbohydrates" : [11.7, 9.01, 19.7, 10.6, 6.53, 13, 9.17, 14.8, 6.03, 8.33], 
               "sugar" : [11.3, 6.7, 15.6, 9.96, 6.1, 10, 8.6, 10.6, 5.6, 7.9],
               "lipid" : [0, 0, 0, 0.33, 0.7, 0, 0, 0, 0, 0]   
}

df_fruits = pd.DataFrame(dict_fruits)
#print(df_fruits)

### Meats eggs and fish

df_mef=pd.DataFrame.from_dict({"name":['Red Meat', 'White meat' ,'Salmon','Tuna','Mackerel'],
                     "energy":[195,173,205,111,189],
                     "protein":[26,28,23,26.8,21],
                     "carbohydrates":[0,0,0,0,0],
                     "sugar":[0,0,0,0,0],
                     "lipid":[10,6.5,12.5,0.4,11],})
#print(df_mef)

### Cereal

df_Cereal=pd.DataFrame.from_dict({"name":['Rice', 'Pasta' ,'Oat flakes','Bread'],
                     "energy":[145,126,378,287],
                     "protein":[3,4,17,8],
                     "carbohydrates":[31,25,55,58],
                     "sugar":[0.2,0.6,1.2,2.3],
                     "lipid":[0.41,0.5,7,1.4],})

#print(df_Cereal)

### Fats and Oils

df_fat=pd.DataFrame.from_dict({"name":['Butter','Olive oil'],
                     "energy":[741,900],
                     "protein":[1,0.1],
                     "carbohydrates":[1,0],
                     "sugar":[1,0],
                     "lipid":[81,99]})
#print(df_fat)

### Generation of the stocks of the supermarkets 

price_max = 15
quantity_max = 200

def shops_and_stocks(list_shops,ingredients):
    '''
    
    '''
    res = []
    experity_date = ["" for i in range(len(ingredients))]
    for i in range(len(list_shops)):
        # giving stocks to the market
        quantities = []
        prices = []
        expery_date = ["" for i in range(len(ingredients))]
        for j in range(len(ingredients)):
            quantities.append(rd.randint(0,quantity_max))
            prices.append(rd.uniform(0,price_max))
        d = { "name" : ingredients, 
              "quantity" : quantities,
              "price" : prices,
              "expery_date" : expery_date}
        res.append(shop(list_shops[i][0], 
                        pd.DataFrame(d), 
                        list_shops[i][1], 
                        list_shops[i][2]))
    return res 
    
# Test 
# L = [('Rapidmarket', '6.0 km', '11 mins'), ('Franprix', '4.5 km', '8 mins'), ('G 20 Supermarche', '9.4 km', '11 mins'), ('Franprix', '4.0 km', '7 mins')]
# shops_and_stocks( L , ["pasta","rice","tomato"] )[0].stocks

    
