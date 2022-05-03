# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:44:15 2022

@author: lucas
"""

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
    print("recipe_food_value")
    print(ut_recipe_food_value())
    print("recipe_value")
    print(ut_recipe_value1())
    print(ut_recipe_value2())
    print(ut_recipe_value3())
    
    

def ut_errand_price1():
    errand_test = errand( pd.DataFrame( {"name" : ["pasta","rice"], "quantity" : [10,3]}) )
    store_test = shop("", df_shops["stocks"][0], 0, 0)
    return errand_test.price(store_test) == 12.25

def ut_errand_price2():
    errand_test = errand( pd.DataFrame( {"name" : ["pasta"], "quantity" : [10]}) )
    store_test = shop("", df_shops["stocks"][0], 0, 0)
    return errand_test.price(store_test) == 10.0

def ut_errand_price3():
    errand_test = errand( pd.DataFrame( {"name" : ["pasta","rice"], "quantity" : [10,4]}) )
    store_test = shop("", df_shops["stocks"][0], 0, 0)
    try:
        errand_test.price(store_test)
        return False
    except ProductNotAvailable:
        return True
    
def ut_recipe_food_needed1():
    recipe_test = recipe(df_recipes["ingredients"][0], df_recipes["prep_time"][0],df_recipes["guests"][0] )
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["pasta","rice"], "quantity" : [10,3]}),
                     coefficients = []) 
    res = pd.DataFrame({ "name" : ["pasta", "tomato"],
                            "quantity" : [140, 2] })
    return res.equals(recipe_test.food_needed(user_test))

def ut_recipe_food_needed2():
    recipe_test = recipe(df_recipes["ingredients"][2], df_recipes["prep_time"][2],df_recipes["guests"][2] )
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["pasta","rice"], "quantity" : [10,3]}),
                     coefficients = []) 
    res = pd.DataFrame({ "name" : ["pasta", "rice"],
                            "quantity" : [90, 97] })
    return res.equals(recipe_test.food_needed(user_test))

def ut_recipe_best_shop1():
    recipe_test = recipe(df_recipes["ingredients"][0], df_recipes["prep_time"][0],df_recipes["guests"][0] )
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["pasta","rice"], "quantity" : [10,3]}),
                     coefficients = [0,0,0,0,0,0.5,0.5]) 
    store_test0 = shop("", pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                                      "quantity" : [150,3,2],
                                      "price" : [1, 0.75, 0.4],
                                      "expiry_date" : ["","",""] }  )
                                   , 11, 0)
    store_test1 = shop("", pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                                      "quantity" : [210,12,6],
                                      "price" : [0.9, 1.25, 0.6],
                                      "expiry_date" : ["","",""] }  ) 
                                   , 8, 0)
    return recipe_test.best_shop(user_test, [store_test0,store_test1]) == (1, 127.2, 8)

def ut_recipe_best_shop2():
    recipe_test = recipe(df_recipes["ingredients"][0], df_recipes["prep_time"][0],df_recipes["guests"][0] )
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["pasta","rice"], "quantity" : [10,3]}),
                     coefficients = [0,0,0,0,0,0.5,0.5]) 
    store_test0 = shop("", pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                                      "quantity" : [150,3,2],
                                      "price" : [1, 0.75, 0.4],
                                      "expiry_date" : ["","",""] }  )
                                   , 11, 0)
    store_test1 = shop("", pd.DataFrame({"name" : ["pasta","rice","tomato"],
                                      "quantity" : [110,12,6],
                                      "price" : [0.9, 1.25, 0.6],
                                      "expiry_date" : ["","",""] }  ) 
                                   , 8, 0)
    return recipe_test.best_shop(user_test, [store_test0,store_test1]) == (0,140.8, 11)

def ut_recipe_best_shop3():
    recipe_test = recipe(df_recipes["ingredients"][0], df_recipes["prep_time"][0],df_recipes["guests"][0] )
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["pasta","rice"], "quantity" : [10,3]}),
                     coefficients = [0,0,0,0,0,0.5,0.5]) 
    store_test0 = shop("", pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                                      "quantity" : [120,3,2],
                                      "price" : [1, 0.75, 0.4],
                                      "expiry_date" : ["","",""] }  )
                                   , 11, 0)
    store_test1 = shop("", pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                                      "quantity" : [110,12,6],
                                      "price" : [0.9, 1.25, 0.6],
                                      "expiry_date" : ["","",""] }  ) 
                                   , 8, 0)
    try:
        recipe_test.best_shop(user_test, [store_test0,store_test1])
        return False
    except NoWhereToBuy:
        return True
    
def ut_recipe_food_value():
    recipe_test = recipe(df_recipes["ingredients"][0], df_recipes["prep_time"][0],df_recipes["guests"][0] )
    exp_res = [647.1, 5.43, 25.49, 3.28, 2.26]
    return np.allclose(exp_res, recipe_test.food_value())

def ut_recipe_value1():
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["pasta","rice"], "quantity" : [10,3]}),
                     coefficients = [0,0,0,0,0,0.5,0.5]) 
    store_test0 = shop("", pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                                      "quantity" : [150,3,5],
                                      "price" : [1, 0.75, 0.4],
                                      "expiry_date" : ["","",""] }  )
                      , 11, 0)
    store_test1 = shop("", pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                                      "quantity" : [110,12,6],
                                      "price" : [0.9, 1.25, 0.6],
                                      "expiry_date" : ["","",""] }  )
                       , 8, 0)
    recipe_test = recipe(df_recipes["ingredients"][0], df_recipes["prep_time"][0],df_recipes["guests"][0] )
    return recipe_test.recipe_value(user_test,[store_test0,store_test1]) == 75.9

def ut_recipe_value2():
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["pasta","rice"], "quantity" : [10,3]}),
                     coefficients = [0,0,0,0,0,0.5,0.5]) 
    store_test0 = shop("", pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                                      "quantity" : [150,3,5],
                                      "price" : [1, 0.75, 0.4],
                                      "expiry_date" : ["","",""] }  )
                      , 11, 0)
    store_test1 = shop("", pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                                      "quantity" : [110,12,6],
                                      "price" : [0.9, 1.25, 0.6],
                                      "expiry_date" : ["","",""] }  )
                       , 8, 0)
    recipe_test = recipe(df_recipes["ingredients"][1], df_recipes["prep_time"][1],df_recipes["guests"][1] )
    return recipe_test.recipe_value(user_test,[store_test0,store_test1]) == np.inf

def ut_recipe_value3():
    user_test = user(health = {}, adress = "", budget = 100, 
                     fridge = pd.DataFrame( {"name" : ["pasta","rice"], "quantity" : [10,3]}),
                     coefficients = [0,0,0,0,0,0.5,0.5]) 
    store_test0 = shop("", pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                                      "quantity" : [150,203,5],
                                      "price" : [1, 0.75, 0.4],
                                      "expiry_date" : ["","",""] }  )
                      , 11, 0)
    store_test1 = shop("", pd.DataFrame( {"name" : ["pasta","rice","tomato"],
                                      "quantity" : [110,212,6],
                                      "price" : [0.9, 1.25, 0.6],
                                      "expiry_date" : ["","",""] }  )
                       , 8, 0)
    recipe_test = recipe(df_recipes["ingredients"][1], df_recipes["prep_time"][1],df_recipes["guests"][1] )
    return recipe_test.recipe_value(user_test,[store_test0,store_test1]) == 79.775


unit_tests()

