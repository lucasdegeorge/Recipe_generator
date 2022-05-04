import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from math import *

### Databases


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
        
    def allergies(self, list_of_allergies, list_of_ingredients):
        for i in range(len(list_of_allergies)):
            list_of_ingredients.remove(list_of_allergies[i])
        
    def nearest_shops(self):
        supermarkets = c    #find_supermarkets(self.adress)
        return shops_and_stocks(supermarkets, list_of_ingredients)
        
    def which_recipe(self):
        '''
        Determine the best recipe to eat
        Return the recipe (class object) which gets the best value, the shop where to buy and the errand
        '''
        recipes = recipe_generator()
        shops = self.nearest_shops()
        best_recipe = -1
        best_value = (-1)*np.inf 
        for i in range(len(recipes)):
            if recipes[i].recipe_value(self,shops) > best_value:
                best_recipe = i
                best_value = recipes[i].recipe_value(self,shops)
        if best_recipe != -1:
            shop_id = recipes[best_recipe].best_shop(self,shops)[0]
            return (recipes[best_recipe]  , shops[shop_id], 
                    recipes[best_recipe].food_needed(self) )
        else:
            raise NoRecipeFound
            



class shop:
    ''' 
    stocks is a dataframe which contains data (name, quantity, price, expiry_date) on a specific food 
    '''
    def __init__(self, name, stocks, distance, time):
        self.name = name
        self.stocks = stocks
        self.distance = float(distance[:-3])
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
            
    def food_value(self, df = df_food):
        '''
        return a list containing the sum of the values of energy, fat, etc of the foods of the recipe
        '''
        res = np.zeros(len(df.columns)-1)
        for i in self.ingredients.index:
            l = df.index[ df["name"] == self.ingredients["ingredient"][i] ].tolist()
            # For each energy, fat, etc ...
            for j in range(1,len(df.columns)):
                res[j-1] = res[j-1] + df.iloc[l[0]][j]
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
            return (-1)*np.inf
        
           
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



## Test 

fridge_t = recipe_generator(tries=1)[0].ingredients
fridge_t.rename(columns = {"ingredient":"name"}, inplace = True) 
        
profil = user([], "28 boulevard Gaspard Monge, Palaiseau 91120", 0, fridge_t
                , [0.14,0.14,0.14,0.14,0.14,0.14,0.14])


        
A = profil.which_recipe()


print(A[0].ingredients)
print("---")
print(A[1].name)
print("---")
print(A[2])
