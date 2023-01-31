### Modules ##

from tkinter import *
import pandas as pd
from ttkwidgets.autocomplete import AutocompleteCombobox
import random as rd
import os
import numpy as np
import matplotlib.pyplot as plt
from math import *
import googlemaps as gm
import geopy as gp
import time

# to be modified ...
path = "C:/Users/lucas/Documents/GitHub/projet_python"

# to be modified ...
os.chdir(path)

# to be modified
images_path = path + "/Pictures/"


######## Ingredients Data #########

nb_coefs = 5


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
                       ,'Tomato','Red Meat', 'White meat' ,'Salmon','Tuna','Mackerel']


### Geolocalization

API_Key = 'AIzaSyDgsXVXBLQ9FEN72hXLHtTVe_-nnhghhds'
map_client = gm.Client(API_Key)
adress = '27 Boulevard Thomas Gobert, Palaiseau 91120'
radius = 4e3


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

#-c = find_supermarkets('27 Boulevard Thomas Gobert, Palaiseau 91120')

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
            if list_of_allergies[i] != '':
                list_of_ingredients.remove(list_of_allergies[i])

    def nearest_shops(self):
        supermarkets = find_supermarkets(self.adress)
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
        best_value = profil.coefs[nb_coefs]*best_price + profil.coefs[nb_coefs+1]*best_distance
        for i in range(len(shops)):
            try:
                pri = food_to_purchase.price(shops[i])
                cost = profil.coefs[nb_coefs]*pri + profil.coefs[nb_coefs+1]*shops[i].distance
                if cost < best_value or isnan(best_value):
                    best_id = i
                    best_price = pri
                    best_distance = shops[i].distance
                    best_value = profil.coefs[nb_coefs]*best_price + profil.coefs[nb_coefs+1]*best_distance
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
        value = value + np.dot(self.food_value(), profil.coefs[:nb_coefs])
        # Then, we determine the value due to the errand, the route and the budget
        try:
            value = value + np.dot(profil.coefs[nb_coefs:],np.array(self.best_shop(profil,shops)[1:]))
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


### Generators

def recipe_generator(tries = 100):
    res = []

    for i in range(tries):

        ingredients = []
        quantities = []

        # Vegetables
        nb = rd.randint(1,2)
        n = len(df_vegetables.index)
        for i in range(nb):
            ingredients.append(df_vegetables["name"].iloc[rd.randint(0,n-1)])
            quantities.append(rd.randint(0,quantity_max))

        # Meats eggs and fish
        n = len(df_mef.index)
        ingredients.append(df_mef["name"].iloc[rd.randint(0,n-1)])
        quantities.append(rd.randint(0,quantity_max))

        # Cereal
        n = len(df_Cereal.index)
        ingredients.append(df_Cereal["name"].iloc[rd.randint(0,n-1)])
        quantities.append(rd.randint(0,quantity_max))

        # Fruits
        n = len(df_fruits.index)
        ingredients.append(df_fruits["name"].iloc[rd.randint(0,n-1)])
        quantities.append(rd.randint(0,quantity_max))

        # Fat
        n = len(df_fat.index)
        ingredients.append(df_fat["name"].iloc[rd.randint(0,n-1)])
        quantities.append(rd.randint(0,quantity_max))

        res.append( recipe( pd.DataFrame({ "ingredient" : ingredients,
                              "quantity" : quantities }),
                      0, 0)  )

    return res


price_max = 15
quantity_max = 200

def shops_and_stocks(list_shops,ingredients):
    '''
    return a list of shops (class object)
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
# shops_and_stocks( L , ["pasta","rice","tomato"] )

def find_coefs(prot):
    if prot==1:
        return [0.08, 0.5, 0.08, 0.08, 0.08, 0.08, 0.08, 0.08]
    else:
        return [0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14]


### MenuPage ###

def MenuPage():

    global NutriBoys

    NutriBoys.destroy()

    #Initialization

    NutriBoys = Tk()
    NutriBoys.geometry("600x400")
    NutriBoys.title("NutriBoys")
    background_image = PhotoImage(file = images_path+"MenuPageBackground.png")
    title_font = ("Times bold", 14)
    font = ("Times bold", 10)

    #Background Image

    Label(
        NutriBoys,
        image = background_image
    ).place(x=0, y=0)

    #Title

    Label(
        NutriBoys,
        text = "NutriBoys",
        padx = 0,
        pady = 0,
        font = title_font,
        bg = "#F3F3F3",
        fg = "Black"
    ).place(x=250, y=140)

    #Navigation Buttons

    Button(
        NutriBoys,
        text = 'User Preferences',
        font = font,
        command = PreferencesPage
    ).place(x=50, y=200)

    Button(
        NutriBoys,
        text = "Meal Request",
        font = font,
        command=MealRequestPage
    ).place(x=250, y=200)

    Button(
        NutriBoys,
        text = "Macro Calculator",
        font = font,
        command = MacroCalculatorPage
    ).place(x=450, y=200)

    #Execution

    NutriBoys.mainloop()

### PreferencesPage ###

def PreferencesPage():

    global NutriBoys
    NutriBoys.destroy()

    #Inizatitialion

    NutriBoys = Tk()
    NutriBoys.geometry("400x600")
    NutriBoys.title("NutriBoys")
    background_image = PhotoImage(file = images_path+"user_background.png")
    title_font = ("Times bold", 14)
    font = ('Times bold', 10)

    # Input Functions

    def submit_parameters():

        global Name
        Name = N.get()

        global Adress
        Adress = A.get()

        global Height
        Height = H.get()

        global Weight
        Weight = W.get()

        global Allergies
        Allergies  = [Al1.get(),Al2.get(),Al3.get(),Al4.get()]

        global Age
        Age = Ag.get()

        global MassBuilding

        MassBuilding = M_value.get()

        MenuPage()

    #Background Image

    Label(
        NutriBoys,
        image = background_image
    ).place(x=0, y=0)

    #Title

    Label(
        NutriBoys,
        text = "User Preferences",
        padx = 0,
        pady = 0,
        font = title_font,
        bg = 'white',
        fg = "Black"
    ).place(x=35, y=35)

    #Name

    Label(
        NutriBoys,
        text = "Name :",
        padx = 0,
        pady = 0,
        font = font,
        bg = 'white',
        fg = 'black'
    ).place(x=15, y = 100)

    N = Entry(
        NutriBoys,
        textvariable="texte par défaut",
        width = 20
    )

    N.place(x=70, y=100)

    #Adress

    Label(
        NutriBoys,
        text = "Adress :",
        padx = 0,
        pady = 0,
        font = font,
        bg = 'white',
        fg = 'black'
    ).place(x=15, y = 130)


    A = Entry(
        NutriBoys,
        textvariable="",
        width = 18
    )

    A.place(x=83, y=130)

    #Height

    Label(
        NutriBoys,
        text = "Height :",
        padx = 0,
        pady = 0,
        font = font,
        bg = 'white',
        fg = 'black'
    ).place(x=15, y=170)


    H_value = StringVar()

    H = Scale(
        NutriBoys,
        variable = H_value,
        from_ = 130,
        to = 210,
        orient = HORIZONTAL,cursor = "dot"
    )

    H.place(x=90, y=160)

    #Weight

    Label(
        NutriBoys,
        text = "Weight :",
        padx = 0,
        pady = 0,
        font = font,
        bg = 'white',
        fg = 'black'
    ).place(x=15, y=220)

    W_value = StringVar()
    W = Scale(
        NutriBoys,
        variable = W_value,
        from_ = 50,
        to = 200,
        orient = HORIZONTAL
        )

    W.place(x=90, y=210)

    #Allergies

    Label(
        NutriBoys,
        text = "Allergies :",
        padx = 0,
        pady = 0,
        font = font,
        bg = 'white',
        fg = 'black'
    ).place(x=15, y = 270)

    Al1=AutocompleteCombobox(
        NutriBoys,
        width=7,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Al1.place(x=90,y=260)

    Al2 =  AutocompleteCombobox(
        NutriBoys,
        width=7,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Al2.place(x=90,y=300)

    Al3 =  AutocompleteCombobox(
        NutriBoys,
        width=7,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Al3.place(x=90, y=340)


    Al4 =  AutocompleteCombobox(
        NutriBoys,
        width=7,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Al4.place(x=90,y=380)

    #Age

    Label(
        NutriBoys,
        text = "Age :",
        padx = 0,
        pady = 0,
        font = font,
        bg = 'white',
        fg = 'black'
    ).place(x=15, y = 420)


    Ag = Entry(
        NutriBoys,
        textvariable="",
        width = 18
    )

    Ag.place(x=83, y=420)

    #Mass Building

    Label(
        NutriBoys,
        text = "Mass Building :",
        padx = 0,
        pady = 0,
        font = font,
        bg = 'white',
        fg = 'black'
    ).place(x=15, y = 450)

    M_value = IntVar()

    M = Checkbutton(
        NutriBoys,
        variable = M_value,
        onvalue=1,
        offvalue=0,
        width = 0,
        padx = 10
    )

    M.place(x=120, y=447)
    #

    # Submit Button

    Button(
        NutriBoys,
        text = 'Submit',
        font = font,
        command = submit_parameters,
    ).place(x=90, y=500)

    # Menu Button

    Button(
        NutriBoys,
        text = 'Menu Page',
        font = font,
        command = MenuPage
    ).place(x=75, y=550)

    # Execution

    NutriBoys.mainloop()
###


### MealRequestPage

def MealRequestPage():

    global NutriBoys


    NutriBoys.destroy()

    #Initialization

    NutriBoys = Tk()
    NutriBoys.geometry()
    NutriBoys.title('NutriBoys')
    'background_image ='
    title_font = ("Times bold", 14)
    font = ('Times bold', 10)

    #Background Image

    def print_df(df,n):
        for i in range(len (df)):
            for j in range(len(df.columns)):
                Label(NutriBoys, text = df.loc[i].iloc[j]).grid(row = i+n, column=1+j)




    #display results
    def display_results2(fridge):

        global NutriBoys
        global profil


        NutriBoys.destroy()
        NutriBoys = Tk()
        profil = user([],adress,0,fridge,find_coefs(MassBuilding))

        profil.allergies(Allergies,list_of_ingredients)
        recette,store, food_to_buy=profil.which_recipe()
        Label(NutriBoys, text = "Recipe :").grid(row = 0, column=0)
        Label(NutriBoys, text = "Name").grid(row = 0, column=1)
        Label(NutriBoys, text = "Quantity").grid(row = 0, column=2)
        print_df(recette.ingredients,1)
        n=len(recette.ingredients)
        Label(NutriBoys, text = "").grid(row = n+1, column=1)
        Label(NutriBoys, text = store.name).grid(row = n+2, column=2)
        Label(NutriBoys, text = "Store name").grid(row = n+2, column=1)
        Label(NutriBoys, text = f"{store.distance}km").grid(row = n+3, column=2)
        Label(NutriBoys, text = "Distance from your home ").grid(row = n+3, column=1)
        Label(NutriBoys, text = store.time).grid(row = n+4, column=2)
        Label(NutriBoys, text = "Minutes away").grid(row = n+4, column=1)
        Label(NutriBoys, text = "").grid(row = n+5, column=1)
        Label(NutriBoys, text = "What to buy:").grid(row = n+6, column=0)
        Label(NutriBoys, text = "Name").grid(row = n+6, column=1)
        Label(NutriBoys, text = "Quantity").grid(row = n+6, column=2)
        print_df(food_to_buy,n+7)
        n2=len(food_to_buy)

        Button(
            NutriBoys,
            text = 'Menu Page',
            font = font,
            command= MenuPage
        ).grid(row = n+n2+9, column=1)

        NutriBoys.mainloop()
    #Input Functions

    def fridge_parameters():
        i_1 = Ingr1.get()
        q_1 = qt1.get()
        i_2 = Ingr2.get()
        q_2 = qt2.get()
        i_3 = Ingr3.get()
        q_3 = qt3.get()
        i_4 = Ingr4.get()
        q_4 = qt4.get()
        i_5 = Ingr5.get()
        q_5 = qt5.get()
        i_6 = Ingr6.get()
        q_6 = qt6.get()
        l=[q_1,q_2,q_3,q_4,q_5,q_6]
        l1=[]
        v=[i_1,i_2,i_3,i_4,i_5,i_6]
        v1=[]
        for i in range(len(l))   :
            if l[i] != ''and v[i] != '':
                l1=l1+[int(l[i])]
                v1=v1+[str(v[i])]
        global fridge
        fridge=pd.DataFrame({"name":v1,
                              "quantity":l1  })
        if v1==[] and l1==[]:
            fridge = pd.DataFrame({"name" : ["Banana"], "quantity":[0]})


    Label(NutriBoys, text = "Fridge : Food item").grid(row = 0, column=0)
    Label(NutriBoys, text = "How Much (in grams)").grid(row = 0, column=2)


    Ingr1=AutocompleteCombobox(
        NutriBoys,
        width=15,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Ingr1.grid(row=0,column=1)
    qt1 = Entry(NutriBoys)
    qt1.grid(row = 0, column = 3)
    Ingr2 =  AutocompleteCombobox(
        NutriBoys,
        width=15,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Ingr2.grid(row = 1, column = 1)
    qt2 = Entry(NutriBoys)
    qt2.grid(row = 1, column = 3)

    Ingr3 =  AutocompleteCombobox(
        NutriBoys,
        width=15,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Ingr3.grid(row = 2, column = 1)
    qt3= Entry(NutriBoys)
    qt3.grid(row = 2, column = 3)

    Ingr4 =  AutocompleteCombobox(
        NutriBoys,
        width=15,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Ingr4.grid(row = 3, column = 1)
    qt4 = Entry(NutriBoys)
    qt4.grid(row = 3, column = 3)

    Ingr5 =  AutocompleteCombobox(
        NutriBoys,
        width=15,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Ingr5.grid(row = 4, column = 1)
    qt5 = Entry(NutriBoys)
    qt5.grid(row = 4, column = 3)

    Ingr6 =  AutocompleteCombobox(
        NutriBoys,
        width=15,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Ingr6.grid(row = 5, column = 1)
    qt6 = Entry(NutriBoys)
    qt6.grid(row = 5, column = 3)


    Button(
        NutriBoys,
        text = "submit",
        command = lambda:[fridge_parameters(),display_results2(fridge)]).place(x=200, y=200)

    Button(
        NutriBoys,
        text = 'Menu Page',
        font = font,
        command= MenuPage
    ).grid(row = 8, column=2)

    mainloop()
    #


### MacroCalculatorPage

def MacroCalculatorPage():

    global NutriBoys
    NutriBoys.destroy()

    #Initialization

    NutriBoys = Tk()
    NutriBoys.geometry("600x400")
    NutriBoys.title("NutriBoys")
    background_image = PhotoImage(file = images_path+"MacroCalculatorPageBackground.png")
    title_font = ("Times bold", 14)
    font = ('Times bold', 10)

    #Background Image

    Label(
        NutriBoys,
        image = background_image
    ).place(x=0, y=0)

    def Calc_Intake(list):
        energy=0
        protein=0
        fat=0
        carbohydrates=0
        sugar=0
        for x in list:
            if x[0]!='':
                (name,qt)=x
                print(qt)
                qt=float(qt)
                row=df_food.loc[df_food['name']==name]
                energy+= float(row['energy'])*qt / 100
                protein+= float(row['protein'])*qt / 100
                fat+= float(row['lipid'])*qt / 100
                carbohydrates+= float(row['carbohydrates'])*qt / 100
                sugar+= float(row['sugar'])*qt / 100
        return energy , protein , fat, carbohydrates, sugar

    def display_results(list):

        global NutriBoys

        x=Calc_Intake(list)

        NutriBoys.destroy()
        NutriBoys = Tk()

        Label(NutriBoys, text = "energy").grid(row = 0, column=0)
        Label(NutriBoys, text = x[0]).grid(row = 0, column=1)
        Label(NutriBoys, text = "protein").grid(row = 1, column=0)
        Label(NutriBoys, text = x[1]).grid(row = 1, column=1)
        Label(NutriBoys, text = "fat").grid(row = 2, column=0)
        Label(NutriBoys, text = x[2]).grid(row = 2, column=1)
        Label(NutriBoys, text = "carbohydrates").grid(row = 3, column=0)
        Label(NutriBoys, text = x[3]).grid(row = 3, column=1)
        Label(NutriBoys, text = "sugar").grid(row = 4, column=0)
        Label(NutriBoys, text = x[4]).grid(row = 4, column=1)

        Button(
            NutriBoys,
            text = 'Menu Page',
            font = font,
            command= MenuPage
        ).grid(row = 5, column=1)

        NutriBoys.mainloop()

    def getInput():
        i_1 = Ingr1.get()
        q_1 = qt1.get()
        i_2 = Ingr2.get()
        q_2 = qt2.get()
        i_3 = Ingr3.get()
        q_3 = qt3.get()
        i_4 = Ingr4.get()
        q_4 = qt4.get()
        i_5 = Ingr5.get()
        q_5 = qt5.get()
        i_6 = Ingr6.get()
        q_6 = qt6.get()
        global params
        params=[(i_1,q_1),(i_2,q_2),(i_3,q_3),(i_4,q_4),(i_5,q_5),(i_6,q_6)]


    Label(NutriBoys, text = "What have you eaten").grid(row = 0, column=0)
    Label(NutriBoys, text = "How Much (in grams)").grid(row = 0, column=2)
    Label(NutriBoys, text = "What have you eaten").grid(row = 1, column=0)
    Label(NutriBoys, text = "How Much(in grams)").grid(row = 1, column=2)
    Label(NutriBoys, text = "What have you eaten").grid(row = 2, column=0)
    Label(NutriBoys, text = "How Much(in grams)").grid(row = 2, column=2)
    Label(NutriBoys, text = "What have you eaten").grid(row =3, column=0)
    Label(NutriBoys, text = "How Much(in grams)").grid(row = 3, column=2)
    Label(NutriBoys, text = "What have you eaten").grid(row = 4, column=0)
    Label(NutriBoys, text = "How Much(in grams)").grid(row = 4, column=2)
    Label(NutriBoys, text = "What have you eaten").grid(row = 5, column=0)
    Label(NutriBoys, text = "How Much(in grams)").grid(row = 5, column=2)

    Ingr1=AutocompleteCombobox(
        NutriBoys,
        width=15,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Ingr1.grid(row=0,column=1)
    qt1 = Entry(NutriBoys)
    qt1.grid(row = 0, column = 3)
    Ingr2 =  AutocompleteCombobox(
        NutriBoys,
        width=15,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Ingr2.grid(row = 1, column = 1)
    qt2 = Entry(NutriBoys)
    qt2.grid(row = 1, column = 3)

    Ingr3 =  AutocompleteCombobox(
        NutriBoys,
        width=15,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Ingr3.grid(row = 2, column = 1)
    qt3= Entry(NutriBoys)
    qt3.grid(row = 2, column = 3)

    Ingr4 =  AutocompleteCombobox(
        NutriBoys,
        width=15,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Ingr4.grid(row = 3, column = 1)
    qt4 = Entry(NutriBoys)
    qt4.grid(row = 3, column = 3)

    Ingr5 =  AutocompleteCombobox(
        NutriBoys,
        width=15,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Ingr5.grid(row = 4, column = 1)
    qt5 = Entry(NutriBoys)
    qt5.grid(row = 4, column = 3)

    Ingr6 =  AutocompleteCombobox(
        NutriBoys,
        width=15,
        font=('Times', 18),
        completevalues=list_of_ingredients
    )

    Ingr6.grid(row = 5, column = 1)
    qt6 = Entry(NutriBoys)
    qt6.grid(row = 5, column = 3)


    Button(
        NutriBoys,
        text = "submit",
        command = lambda:[getInput(),display_results(params)]).place(x=200, y=200)

    Button(
        NutriBoys,
        text = 'Menu Page',
        font = font,
        command= MenuPage
    ).grid(row = 8, column=2)

    NutriBoys.mainloop()

### Initialization

#Initialization

NutriBoys = Tk()
NutriBoys.geometry("600x400")
NutriBoys.title("NutriBoys")
background_image = PhotoImage(file = images_path+"MenuPageBackground.png")
title_font = ("Times bold", 14)
font = ("Times bold", 10)

#Background Image

Label(
    NutriBoys,
    image = background_image
).place(x=0, y=0)

#Title

Label(
    NutriBoys,
    text = "NutriBoys",
    padx = 0,
    pady = 0,
    font = title_font,
    bg = "#F3F3F3",
    fg = "Black"
).place(x=250, y=140)

#Navigation Buttons

Button(
    NutriBoys,
    text = 'User Preferences',
    font = font,
    command = PreferencesPage
).place(x=50, y=200)

Button(
    NutriBoys,
    text = "Meal Request",
    font = font,
    command=MealRequestPage
).place(x=250, y=200)

Button(
    NutriBoys,
    text = "Macro Calculator",
    font = font,
    command = MacroCalculatorPage
).place(x=450, y=200)

#Execution

NutriBoys.mainloop()




