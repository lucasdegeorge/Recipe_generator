

from ttkwidgets.autocomplete import AutocompleteCombobox
import random as rd
import os
import numpy as np
import matplotlib.pyplot as plt
from math import *
import googlemaps as gm
import geopy as gp
import time


## Data for the unit tests 

#  Energy, protein, carbohydrates, sugar, lipid
dict_food_test = { "name" : ["Pasta","Rice","Tomato"],
              "energy" : [566,615,81.1],
              "protein" : [4.57, 2.92,0.86],
              "carbohydrates" : [23, 31.8,2.49],
              "sugar" : [0.8, 0.2, 2.48],
              "lipid" : [2, 0.41, 0.26],
              }
df_food_test = pd.DataFrame(dict_food)


df_r1 = pd.DataFrame( { "ingredient" : ["Pasta", "Tomato"],
                        "quantity" : [150, 2] } )

df_r2 = pd.DataFrame( { "ingredient" : ["Rice", "Tomato"],
                        "quantity" : [200, 2] } )

df_r3 = pd.DataFrame( { "ingredient" : ["Pasta", "Rice"],
                        "quantity" : [100, 100] } )

dict_recipes = { "name" : ["tomato_pastas", "tomato_rice", "rice_pastas"],
                 "ingredients" : [ df_r1, df_r2, df_r3 ],
                 "prep_time" : [20, 20, 30],
                 "guests" : [1,1,1]
                }

df_recipes = pd.DataFrame(dict_recipes)

df_s1 = pd.DataFrame( {"name" : ["Pasta","Rice","Tomato"],
                     "quantity" : [150,3,2],
                     "price" : [1, 0.75, 0.4],
                     "expiry_date" : ["","",""]
                         }  ) 

df_s2 =  pd.DataFrame( {"name" : ["Pasta","Rice","Tomato"],
                     "quantity" : [210,12,6],
                     "price" : [0.9, 1.25, 0.6],
                     "expiry_date" : ["","",""]
                         }  ) 

df_s3 =  pd.DataFrame( {"name" : ["Pasta","Rice","Tomato"],
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


## Unit tests 

def unit_tests():
    print("errand.price")
    print(ut_errand_price1())
    print(ut_errand_price2())
    print(ut_errand_price3())
    print("recipe.food_needed")
    print(ut_recipe_food_needed1())
    print(ut_recipe_food_needed2())
    print("recipe.best_shop")
    print(ut_recipe_best_shop1())
    print(ut_recipe_best_shop2())
    print(ut_recipe_best_shop3())
    print("recipe_value")
    print(ut_recipe_value1())
    print(ut_recipe_value2())
    print(ut_recipe_value3())
    
    

def ut_errand_price1():
    errand_test = errand( pd.DataFrame( {"name" : ["Pasta","Rice"], "quantity" : [10,3]}) )
    store_test = shop("", df_shops["stocks"][0], '0 km', 0)
    return errand_test.price(store_test) == 12.25

def ut_errand_price2():
    errand_test = errand( pd.DataFrame( {"name" : ["Pasta"], "quantity" : [10]}) )
    store_test = shop("", df_shops["stocks"][0], '0 km', 0)
    return errand_test.price(store_test) == 10.0

def ut_errand_price3():
    errand_test = errand( pd.DataFrame( {"name" : ["Pasta","Rice"], "quantity" : [10,4]}) )
    store_test = shop("", df_shops["stocks"][0],'0 km', 0)
    try:
        errand_test.price(store_test)
        return False
    except ProductNotAvailable:
        return True
    
def ut_recipe_food_needed1():
    recipe_test = recipe(df_recipes["ingredients"][0], df_recipes["prep_time"][0],df_recipes["guests"][0] )
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["Pasta","Rice"], "quantity" : [10,3]}),
                     coefficients = []) 
    res = pd.DataFrame({ "name" : ["Pasta", "Tomato"],
                            "quantity" : [140, 2] })
    return res.equals(recipe_test.food_needed(user_test))

def ut_recipe_food_needed2():
    recipe_test = recipe(df_recipes["ingredients"][2], df_recipes["prep_time"][2],df_recipes["guests"][2] )
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["Pasta","Rice"], "quantity" : [10,3]}),
                     coefficients = []) 
    res = pd.DataFrame({ "name" : ["Pasta", "Rice"],
                            "quantity" : [90, 97] })
    return res.equals(recipe_test.food_needed(user_test))

def ut_recipe_best_shop1():
    recipe_test = recipe(df_recipes["ingredients"][0], df_recipes["prep_time"][0],df_recipes["guests"][0] )
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["Pasta","Rice"], "quantity" : [10,3]}),
                     coefficients = [0,0,0,0,0,0.5,0.5]) 
    store_test0 = shop("", pd.DataFrame( {"name" : ["Pasta","Rice","Tomato"],
                                      "quantity" : [150,3,2],
                                      "price" : [1, 0.75, 0.4],
                                      "expiry_date" : ["","",""] }  )
                                   , '11 km', 0)
    store_test1 = shop("", pd.DataFrame( {"name" : ["Pasta","Rice","Tomato"],
                                      "quantity" : [210,12,6],
                                      "price" : [0.9, 1.25, 0.6],
                                      "expiry_date" : ["","",""] }  ) 
                                   , '8 km', 0)
    return recipe_test.best_shop(user_test, [store_test0,store_test1]) == (1, 127.2, 8)

def ut_recipe_best_shop2():
    recipe_test = recipe(df_recipes["ingredients"][0], df_recipes["prep_time"][0],df_recipes["guests"][0] )
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["Pasta","Rice"], "quantity" : [10,3]}),
                     coefficients = [0,0,0,0,0,0.5,0.5]) 
    store_test0 = shop("", pd.DataFrame( {"name" : ["Pasta","Rice","Tomato"],
                                      "quantity" : [150,3,2],
                                      "price" : [1, 0.75, 0.4],
                                      "expiry_date" : ["","",""] }  )
                                   , '11 km', 0)
    store_test1 = shop("", pd.DataFrame({"name" : ["Pasta","Rice","Tomato"],
                                      "quantity" : [110,12,6],
                                      "price" : [0.9, 1.25, 0.6],
                                      "expiry_date" : ["","",""] }  ) 
                                   , '8 km', 0)
    return recipe_test.best_shop(user_test, [store_test0,store_test1]) == (0,140.8, 11)

def ut_recipe_best_shop3():
    recipe_test = recipe(df_recipes["ingredients"][0], df_recipes["prep_time"][0],df_recipes["guests"][0] )
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["Pasta","Rice"], "quantity" : [10,3]}),
                     coefficients = [0,0,0,0,0,0.5,0.5]) 
    store_test0 = shop("", pd.DataFrame( {"name" : ["Pasta","Rice","Tomato"],
                                      "quantity" : [120,3,2],
                                      "price" : [1, 0.75, 0.4],
                                      "expiry_date" : ["","",""] }  )
                                   , '11 km', 0)
    store_test1 = shop("", pd.DataFrame( {"name" : ["Pasta","Rice","Tomato"],
                                      "quantity" : [110,12,6],
                                      "price" : [0.9, 1.25, 0.6],
                                      "expiry_date" : ["","",""] }  ) 
                                   , '8 km', 0)
    try:
        recipe_test.best_shop(user_test, [store_test0,store_test1])
        return False
    except NoWhereToBuy:
        return True
    

def ut_recipe_value1():
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["Pasta","Rice"], "quantity" : [10,3]}),
                     coefficients = [0,0,0,0,0,0.5,0.5]) 
    store_test0 = shop("", pd.DataFrame( {"name" : ["Pasta","Rice","Tomato"],
                                      "quantity" : [150,3,5],
                                      "price" : [1, 0.75, 0.4],
                                      "expiry_date" : ["","",""] }  )
                      , '11 km', 0)
    store_test1 = shop("", pd.DataFrame( {"name" : ["Pasta","Rice","Tomato"],
                                      "quantity" : [110,12,6],
                                      "price" : [0.9, 1.25, 0.6],
                                      "expiry_date" : ["","",""] }  )
                       , '8 km', 0)
    recipe_test = recipe(df_recipes["ingredients"][0], df_recipes["prep_time"][0],df_recipes["guests"][0] )
    return recipe_test.recipe_value(user_test,[store_test0,store_test1]) == 75.9

def ut_recipe_value2():
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["PAsta","Rice"], "quantity" : [10,3]}),
                     coefficients = [0,0,0,0,0,0.5,0.5]) 
    store_test0 = shop("", pd.DataFrame( {"name" : ["Pasta","Rice","Tomato"],
                                      "quantity" : [150,3,5],
                                      "price" : [1, 0.75, 0.4],
                                      "expiry_date" : ["","",""] }  )
                      , '11 km', 0)
    store_test1 = shop("", pd.DataFrame( {"name" : ["Pasta","Rice","Tomato"],
                                      "quantity" : [110,12,6],
                                      "price" : [0.9, 1.25, 0.6],
                                      "expiry_date" : ["","",""] }  )
                       , '8 km', 0)
    recipe_test = recipe(df_recipes["ingredients"][1], df_recipes["prep_time"][1],df_recipes["guests"][1] )
    return recipe_test.recipe_value(user_test,[store_test0,store_test1]) == np.inf

def ut_recipe_value3():
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["Pasta","Rice"], "quantity" : [10,3]}),
                     coefficients = [0,0,0,0,0,0.5,0.5]) 
    store_test0 = shop("", pd.DataFrame( {"name" : ["Pasta","Rice","Tomato"],
                                      "quantity" : [150,203,5],
                                      "price" : [1, 0.75, 0.4],
                                      "expiry_date" : ["","",""] }  )
                      , '11 km', 0)
    store_test1 = shop("", pd.DataFrame( {"name" : ["Pasta","Rice","Tomato"],
                                      "quantity" : [110,212,6],
                                      "price" : [0.9, 1.25, 0.6],
                                      "expiry_date" : ["","",""] }  )
                       , '8 km', 0)
    recipe_test = recipe(df_recipes["ingredients"][1], df_recipes["prep_time"][1],df_recipes["guests"][1] )
    return recipe_test.recipe_value(user_test,[store_test0,store_test1]) == 79.775



unit_tests()

