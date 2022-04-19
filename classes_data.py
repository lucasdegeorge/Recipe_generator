import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from math import * 

### Databases

#  Energy, fat, saturated fatty acid, carbohydrates, sugar, protein, lipid
dict_food = { "name" : ["pasta","riz","tomato"],
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

df_r2 = pd.DataFrame( { "ingredient" : ["riz", "tomato"],
                        "quantity" : [200, 2] } )

df_r3 = pd.DataFrame( { "ingredient" : ["pasta", "riz"],
                        "quantity" : [100, 100] } )

dict_recipes = { "name" : ["tomato_pastas", "tomato_riz", "riz_pastas"],
                 "ingredients" : [ df_r1, df_r2, df_r3 ],
                 "prep_time" : [20, 20, 30],
                 "guests" : [1,1,1]
                }

df_recipes = pd.DataFrame(dict_recipes)

df_s1 = pd.DataFrame( {"name" : ["pasta","riz","tomato"],
                     "quantity" : [20,3,1],
                     "price" : [1, 0.75, 0.4],
                     "expiry_date" : ["","",""]
                         }  ) 

df_s2 =  pd.DataFrame( {"name" : ["pasta","riz","tomato"],
                     "quantity" : [1,12,6],
                     "price" : [0.9, 1.25, 0.6],
                     "expiry_date" : ["","",""]
                         }  ) 

df_s3 =  pd.DataFrame( {"name" : ["pasta","riz","tomato"],
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

### Classes 

class user:
    ''' 
    health is a dict with data about weight, height, sex, body_fat, ...
    fridge is a dataframe which contains data (name, quantity, expiry_date, fondness) on a specific food
    '''
    def __init__(self,health, coord, budget, fridge):
        self.health_data = health
        self.adress = coord
        self.budget = budget
        self.fidge = fridge


class shop:
    ''' 
    stocks is a dataframe which contains data (name, quantity, price, expiry_date) on a specific food 
    '''
    def __init__(self, stocks, coord):
        self.stocks = stocks
        self.hours = []
        self.adress = coord


class recipe:
    ''' 
    ingredients is a dataframe which contains data (name, quantity) on a specific food 
    '''
    def __init__(self, ingredients, prep_time, guests):
        self.ingredients = ingredients
        self.prep_time = prep_time
        self.guests = guests
       

class errand:
    '''
    shopping_list is a dataframe which contains data (name, quantity) on a specific food 
    '''
    def __init__(self,shopping_list):
        self.needs = shopping_list
        
    def price(self, store):
        p = 0
        for i in self.needs.index:
            df = store.stocks.loc[store.stocks["name"] == self.needs[i] ]
            
        return df
    

errand_test = errand( pd.DataFrame( {"name" : ["pasta"], "quantity" : [10]}) )
store_test = shop(df_shops["stocks"][0], 0)



