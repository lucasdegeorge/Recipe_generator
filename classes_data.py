import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from math import * 

class user:
    ''' 
    health is a dict with data about weight, height, sex, body_fat, ...
    food is a np.array whose lines contain data (name, quantity, expiry_date, fondness) on a specific food
    '''
    def __init__(self,health, coord, budget, food):
        self.health_data = health
        self.adress = coord
        self.budget = budget
        self.fidge = pd.DataFrame(data=food, columns=["name","quantity","expiry_date","fondness"])


class shop:
    ''' 
    food is a np.array whose lines contain data (name, quantity, price, expiry_date) on a specific food 
    '''
    def __init__(self, food, coord):
        self.stocks = pd.DataFrame(data=food, columns=["name","quantity","price","expiry_date"])
        self.hours = []
        self.adress = coord


class recipe:
    def __init__(self, food, prep_time):
        self.ingredient = pd.DataFrame(data=food, columns=["name","quantity"])
        self.prep_time = prep_time
       

class errand:
    '''
    shpping_list is a np.array whose lines contain data (quantity, price) on a specific food 
    '''
    def __init__(self,shopping_list):
        self.needs = pd.DataFrame(data=shpping_list, columns=["name","quantity"])
        
    def price(self, store):
        p = 0
        for i in self.needs.index:
            df = store.stocks.loc[store.stocks["name"] == self.needs[i] ]
            
        return df



