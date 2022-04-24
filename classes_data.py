import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from math import *

### Databases

#  Energy, fat, saturated fatty acid, carbohydrates, sugar, protein, lipid
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
        self.fridge = fridge


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
        
    def food_needed(self, profil):
        '''function which returns a dataframe containing the foods needed for the recipe and which aren't owned by the profil'''
        name = []
        quantity = []
        for i in self.ingredients.index:
            # The index of the line containing the food is retrieved
            l = profil.fridge.index[ profil.fridge["name"] == self.ingredients["ingredient"][i] ].tolist()
            try:
                if profil.fridge["quantity"][l[0]] <= self.ingredients["quantity"][i]:
                    name.append(self.ingredients["ingredient"][i])
                    quantity.append( self.ingredients["quantity"][i] - profil.fridge["quantity"][l[0]] )
            except IndexError:
                name.append(self.ingredients["ingredient"][i])
                quantity.append( self.ingredients["quantity"][i] )
        return pd.DataFrame(list(zip(name, quantity)), columns=["name","quantity"])
    
    def best_price(self,profil,preference,shops):
        ''' 
        preference is a vector containing coefficient telling either the profil prefers time, money, quality, etc. 
        return a tuple with the shop where the best price is found and the price
        '''
        food_to_purchase = errand(self.food_needed(profil))
        best_price = np.inf
        best_shop = -1
        for i in range(len(shops)):
            try:
                p = food_to_purchase.price(shop[i])
                ## Here we can introduce additional costs in the price (routes, fuel, etc.)
                if p < best_price:
                    best_shop = i
                    best_price = p
            except ProductNotAvailable:
                pass
        if not(best_shop == -1):
            return (best_shop, best_price)
        else:
            raise NoWhereToBuy
            

recipe_test = recipe(df_recipes["ingredients"][0], df_recipes["prep_time"][0],df_recipes["guests"][0] )
user_test = user(health = {}, coord = 0, budget = 100, 
                 fridge = pd.DataFrame( {"name" : ["pasta","rice"], "quantity" : [10,3]}) ) 

store_test1 = shop(df_shops["stocks"][0], 0)
store_test2 = shop(df_shops["stocks"][1], 0)





class errand:
    '''
    shopping_list is a dataframe which contains data (name, quantity) on a specific food 
    '''
    def __init__(self,shopping_list):
        self.needs = shopping_list
        
    def price(self, store):
        p = 0
        for i in self.needs.index:
            # The index of the line containing the food is retrieved
            l = store.stocks.index[ store.stocks["name"] == self.needs["name"][i] ].tolist()
            try:
                if self.needs["quantity"][i] <= store.stocks["quantity"][l[0]]:
                    p = p + self.needs["quantity"][i]*store.stocks["price"][l[0]]
                else:
                    raise ProductNotAvailable("The shop doesn't have enough quantity")
            except IndexError:
                raise ProductNotAvailable
        return p

## Exception 

class NoWhereToBuy(Exception):
    pass

class ProductNotAvailable(Exception):
    pass 


