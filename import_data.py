import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from math import * 
import random as rd


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

dict_mef = {"name":['Red Meat', 'White meat' ,'Salmon','Tuna','Mackerel'],
                     "energy":[195,173,205,111,189],
                     "protein":[26,28,23,26.8,21],
                     "carbohydrates":[0,0,0,0,0],
                     "sugar":[0,0,0,0,0],
                     "lipid":[10,6.5,12.5,0.4,11],}


df_mef=pd.DataFrame.from_dict(dict_mef)
#print(df_mef)

### Cereal

dict_cereal = {"name":['Rice', 'Pasta' ,'Oat flakes','Bread'],
                     "energy":[145,126,378,287],
                     "protein":[3,4,17,8],
                     "carbohydrates":[31,25,55,58],
                     "sugar":[0.2,0.6,1.2,2.3],
                     "lipid":[0.41,0.5,7,1.4],}

df_Cereal=pd.DataFrame.from_dict(dict_cereal)

#print(df_Cereal)

### Fats and Oils

dict_fat = {"name":['Butter','Olive oil'],
                     "energy":[741,900],
                     "protein":[1,0.1],
                     "carbohydrates":[1,0],
                     "sugar":[1,0],
                     "lipid":[81,99]}


df_fat=pd.DataFrame.from_dict(dict_fat)
#print(df_fat)


## Food 

dict_food = {}

dict_food["name"] = dict_vegetables.get("name") + dict_fruits.get("name") + dict_mef.get("name") + dict_cereal.get("name") + dict_fat.get("name")

dict_food["energy"] = dict_vegetables.get("energy") + dict_fruits.get("energy") + dict_mef.get("energy") + dict_cereal.get("energy") + dict_fat.get("energy")

dict_food["protein"] = dict_vegetables.get("protein") + dict_fruits.get("protein") + dict_mef.get("protein") + dict_cereal.get("protein") + dict_fat.get("protein")

dict_food["carbohydrates"] = dict_vegetables.get("carbohydrates") + dict_fruits.get("carbohydrates") + dict_mef.get("carbohydrates") + dict_cereal.get("carbohydrates") + dict_fat.get("carbohydrates")

dict_food["sugar"] = dict_vegetables.get("sugar") + dict_fruits.get("sugar") + dict_mef.get("sugar") + dict_cereal.get("sugar") + dict_fat.get("sugar")

dict_food["lipid"] = dict_vegetables.get("lipid") + dict_fruits.get("lipid") + dict_mef.get("lipid") + dict_cereal.get("lipid") + dict_fat.get("lipid")
              
df_food = pd.DataFrame(dict_food)



## List of ingredients

list_of_ingredients = ['Butter','Olive oil','Rice', 'Pasta' ,'Oat flakes','Bread',
                       'Apple', 'Apricot', 'Banana', 'Blueberry', 'Blackberry',
                       'Cherry', 'Clementine', 'Melon', 'Strawberry', 'Watermelon',
                       'Artichoke','Asparagus','Avocado','Beetroot','Broccoli',
                       'Carrot','Celeriac','Courgette ','Cucumber','Haricot','Lentil'
                       ,'Tomato']


    
