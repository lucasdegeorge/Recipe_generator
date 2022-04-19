# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 17:44:15 2022

@author: lucas
"""

def unitary_tests():
    print(ut_errand_price1())
    print(ut_errand_price2())
    print(ut_errand_price3())
    

def ut_errand_price1():
    errand_test = errand( pd.DataFrame( {"name" : ["pasta","riz"], "quantity" : [10,3]}) )
    store_test = shop(df_shops["stocks"][0], 0)
    return errand_test.price(store_test) == 12.25

def ut_errand_price2():
    errand_test = errand( pd.DataFrame( {"name" : ["pasta"], "quantity" : [10]}) )
    store_test = shop(df_shops["stocks"][0], 0)
    return errand_test.price(store_test) == 10.0

def ut_errand_price3():
    errand_test = errand( pd.DataFrame( {"name" : ["pasta","riz"], "quantity" : [10,4]}) )
    store_test = shop(df_shops["stocks"][0], 0)
    try:
        errand_test.price(store_test)
        return False
    except ProductNotAvailable:
        return True

unitary_tests()
