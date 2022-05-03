import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from math import *

### Databases

#  Energy, protein, carbohydrates, sugar, lipid
dict_food = { "name" : ["pasta","rice","tomato"],
              "energy" : [566,615,81.1],
              "protein" : [4.57, 2.92,0.86],
              "carbohydrates" : [23, 31.8,2.49],
              "sugar" : [0.8, 0.2, 2.48],
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
                     "quantity" : [150,3,2],
                     "price" : [1, 0.75, 0.4],
                     "expiry_date" : ["","",""]
                         }  ) 

df_s2 =  pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                     "quantity" : [210,12,6],
                     "price" : [0.9, 1.25, 0.6],
                     "expiry_date" : ["","",""]
                         }  ) 

df_s3 =  pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                     "quantity" : [400,16,23],
                     "price" : [1.2, 1, 0.5],
                     "expiry_date" : ["","",""]
                         }  ) 
dict_shops = { "name" : ["Casino", "Leclerc", "Franprix"],
               "adress" : ["","",""],
               "hours" : ["","",""],
               "stocks" : [ df_s1, df_s2, df_s3 ] 
               }
               
df_shops = pd.DataFrame(dict_shops)

### Constants : 
p = 5
d = 10


### Classes 

class user:
    ''' 
    health is a dict with data about weight, height, sex, body_fat, ...
    fridge is a dataframe which contains data (name, quantity, expiry_date, fondness) on a specific food
    coefficients is a vector of 
    '''
    def __init__(self,health, adress, budget, fridge, coefficients):
        self.health_data = health
        self.adress = adress
        self.budget = budget
        self.fridge = fridge
        self.coefs = coefficients
        
    def which_recipe(self, recipes, shops):
        '''
        coefficients is a vector containing the preferences of the user (energy, protein, bio, money, time, etc.)
        '''
        best_recipe = -1
        best_value = (-1)*np.inf 
        for i in range(len(recipes)):
            if recipes[i].recipe_value(self) > best_value:
                best_recipe = i
                best_value = recipes[i].recipe_value(self)
        if best_recipe != -1:
            return (best_recipe, best_value)
        else:
            raise NoRecipeFound
    

class shop:
    ''' 
    stocks is a dataframe which contains data (name, quantity, price, expiry_date) on a specific food 
    '''
    def __init__(self, name, stocks, distance, time):
        self.name = name
        self.stocks = stocks
        self.distance = distance
        self.time = time


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
    

    def best_shop(self,profil,shops):
        ''' 
        return a tuple with the shop where the best (price,distance) is found and the (price,distance)
        '''
        food_to_purchase = errand(self.food_needed(profil))
        best_price = np.inf
        best_distance = np.inf
        best_id = -1
        best_value = profil.coefs[p]*best_price + profil.coefs[p+1]*best_distance
        for i in range(len(shops)):
            try:
                pri = food_to_purchase.price(shops[i])
                cost = profil.coefs[p]*pri + profil.coefs[p+1]*shops[i].distance
                if cost < best_value or isnan(best_value):
                    best_id = i
                    best_price = pri
                    best_distance = shops[i].distance
                    best_value = profil.coefs[p]*best_price + profil.coefs[p+1]*best_distance
            except ProductNotAvailable:
                pass
        if best_id != -1:
            return (best_id, best_price, best_distance)
        else:
            raise NoWhereToBuy
            
    def food_value(self):
        '''
        return a list containing the sum of the values of energy, fat, etc of the foods of the recipe
        '''
        res = np.zeros(len(df_food.columns)-1)
        for i in self.ingredients.index:
            l = df_food.index[ df_food["name"] == self.ingredients["ingredient"][i] ].tolist()
            # For each energy, fat, etc ...
            for j in range(1,len(df_food.columns)):
                res[j-1] = res[j-1] + df_food.iloc[l[0]][j]
        return res   

    def recipe_value(self,profil,shops):
        value = 0 
        # First, we determine the value due to the nutritive properties of the foods in the recipe
        # i=0,...,p-1 in coefs
        value = value + np.dot(self.food_value(), profil.coefs[:p])
        # Then, we determine the value due to the errand, the route and the budget
        try:
            value = value + np.dot(profil.coefs[p:],np.array(self.best_shop(profil,shops)[1:]))
            return value 
        except NoWhereToBuy:
            return np.inf
        
           
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

class NoRecipeFound(Exception):
    pass

class NoWhereToBuy(Exception):
    pass

class ProductNotAvailable(Exception):
    pass 
