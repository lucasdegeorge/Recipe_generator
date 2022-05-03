### Menu Interface ###

### Modules ##

from tkinter import *
import pandas as pd
from ttkwidgets.autocomplete import AutocompleteCombobox

### MenuPage ###

def MenuPage():

    global NutriBoys

    NutriBoys.destroy()

    #Initialization

    NutriBoys = Tk()
    NutriBoys.geometry("600x400")
    NutriBoys.title("NutriBoys")
    background_image = PhotoImage(file = "C:\\Users\\Baptiste\\Pictures\\MenuPageBackground.png")
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

    #Initialization

    NutriBoys = Tk()
    NutriBoys.geometry("400x600")
    NutriBoys.title("NutriBoys")
    background_image = PhotoImage(file = "C:\\Users\\Baptiste\\Pictures\\user_background.png")
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

        NutriBoys.destroy()
        MenuPage(NutriBoys)

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
        bg = "white",
        fg = 'black'
    ).place(x=15, y=270)

    Al1 = Entry(
        NutriBoys,
        textvariable="",
        width = 18
    )

    Al1.place(x=83, y=270)

    Al2 = Entry(
        NutriBoys,
        textvariable="",
        width = 18
    )

    Al2.place(x=83, y=300)

    Al3 = Entry(
        NutriBoys,
        textvariable="",
        width = 18
    )

    Al3.place(x=83, y=330)

    Al4 = Entry(
        NutriBoys,
        textvariable="",
        width = 18
    )

    Al4.place(x=83, y=360)

    # Submit Button

    Button(
        NutriBoys,
        text = 'Submit',
        font = font,
        command = submit_parameters
    ).place(x=90, y=450)

    # Menu Button

    Button(
        NutriBoys,
        text = 'Menu Page',
        font = font,
        command = MenuPage
    ).place(x=75, y=550)

    # Execution

    NutriBoys.mainloop()

### MacroCalculatorPage

def MacroCalculatorPage():
    
    NutriBoys.destroy()
    
    #Initialization 
    
    NutriBoys = Tk()
    NutriBoys.geometry("400x600")
    NutriBoys.title("NutriBoys")
    background_image = PhotoImage(file = "C:\\Users\\Baptiste\\Pictures\\user_background.png")
    title_font = ("Times bold", 14)
    font = ('Times bold', 10)
    
    # Vegetables
    
    dict_vegetables = {"name" : ['Artichoke','Asparagus','Avocado','Beetroot','Broccoli','Carrot','Celeriac','Courgette','Cucumber','Haricot','Lentil','Tomato'],
                "energy" : [25.2, 26.6, 205, 42.8, 37.6, 18.9, 26.2, 15.5, 15.6, 112, 127, 81.1],
                "protein" : [1.2, 2.69, 1.56, 1.74, 2.5, 0.55, 0.94, 0.93, 0.64, 6.75, 10.1, 0.86],
                "carbohydrates" : [3.02, 1.73, 0.83, 9.1, 1.23, 2.6, 4.32, 1.4, 2.54, 12, 16.2, 2.49 ],
                "sugar" : [0.8, 0.81, 0.4, 6.76, 0.8, 1.3, 1.2, 1.39, 1.67, 0.3, 0.2, 2.48],
                "lipid" : [0, 0.32, 20.6, 0.24, 0.4, 0, 0, 0.36, 0.11, 1.1, 0.58, 0.26]
}

    df_vegetables = pd.DataFrame(dict_vegetables)

    # Fruits
    dict_fruits = {"name" : ['Apple', 'Apricot', 'Banana', 'Blueberry', 'Blackberry', 'Cherry', 'Clementine', 'Melon', 'Strawberry', 'Watermelon' ],
            "energy" : [54.9, 45.9, 90.5, 57.7, 47.3, 55.7, 47.3, 62.7, 38.6, 38.9],
            "protein" : [0, 0.81, 1.06, 0.87, 1.13, 0.81, 0.81, 1.13, 0.63, 0.69],
            "carbohydrates" : [11.7, 9.01, 19.7, 10.6, 6.53, 13, 9.17, 14.8, 6.03, 8.33],
            "sugar" : [11.3, 6.7, 15.6, 9.96, 6.1, 10, 8.6, 10.6, 5.6, 7.9],
            "lipid" : [0, 0, 0, 0.33, 0.7, 0, 0, 0, 0, 0]
    }

    df_fruits = pd.DataFrame(dict_fruits)
    
    # Meats eggs and fish
    
    df_mef=pd.DataFrame.from_dict({"name":['Red Meat', 'White meat' ,'Salmon','Tuna','Mackerel'],
                     "energy":[195,173,205,111,189],
                     "protein":[26,28,23,26.8,21],
                     "carbohydrates":[0,0,0,0,0],
                     "sugar":[0,0,0,0,0],
                     "lipid":[10,6.5,12.5,0.4,11],})
    # Cereal
    
    df_cereal=pd.DataFrame.from_dict({"name":['Rice', 'Pasta' ,'Oat flakes','Bread'],
                     "energy":[145,126,378,287],
                     "protein":[3,4,17,8],
                     "carbohydrates":[31,25,55,58],
                     "sugar":[0.2,0.6,1.2,2.3],
                     "lipid":[0.41,0.5,7,1.4],})
                     
    # Fats and Oils
    
    df_fat=pd.DataFrame.from_dict({"name":['Butter','Olive oil'],
                     "energy":[741,900],
                     "protein":[1,0.1],
                     "carbohydrates":[1,0],
                     "sugar":[1,0],
                     "lipid":[81,99]})
                     
    df_ingredients=pd.concat([df_vegetables,df_mef,df_fruits,df_fat,df_cereal]).reset_index(drop=True)
    ingredients= list(df_ingredients['name'])
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
                row=df_ingredients.loc[df_ingredients['name']==name]
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
        NutriBoys.geometry("600x400")
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
        i_7 = Ingr7.get()
        q_7 = qt7.get()
        i_8 = Ingr8.get()
        q_8 = qt8.get()
        root.destroy()
        global params
        params=[(i_1,q_1),(i_2,q_2),(i_3,q_3),(i_4,q_4),(i_5,q_5),(i_6,q_6),(i_7,q_7),(i_8,q_8)]
    root = Tk()
    
    Label(root, text = "What have you eaten").grid(row = 0, column=0)
    Label(root, text = "How Much (in grams)").grid(row = 0, column=2)
    Label(root, text = "What have you eaten").grid(row = 1, column=0)
    Label(root, text = "How Much(in grams)").grid(row = 1, column=2)
    Label(root, text = "What have you eaten").grid(row = 2, column=0)
    Label(root, text = "How Much(in grams)").grid(row = 2, column=2)
    Label(root, text = "What have you eaten").grid(row =3, column=0)
    Label(root, text = "How Much(in grams)").grid(row = 3, column=2)
    Label(root, text = "What have you eaten").grid(row = 4, column=0)
    Label(root, text = "How Much(in grams)").grid(row = 4, column=2)
    Label(root, text = "What have you eaten").grid(row = 5, column=0)
    Label(root, text = "How Much(in grams)").grid(row = 5, column=2)
    Label(root, text = "What have you eaten").grid(row = 6, column=0)
    Label(root, text = "How Much(in grams)").grid(row = 6, column=2)
    Label(root, text = "What have you eaten").grid(row = 7, column=0)
    Label(root, text = "How Much(in grams)").grid(row = 7, column=2)
    
    Ingr1=AutocompleteCombobox(
        root,
        width=30,
        font=('Times', 18),
        completevalues=ingredients
    )
        
    Ingr1.grid(row=0,column=1)
    qt1 = Entry(root)
    qt1.grid(row = 0, column = 3)
    Ingr2 =  AutocompleteCombobox(
        root,
        width=30,
        font=('Times', 18),
        completevalues=ingredients
    )
        
    Ingr2.grid(row = 1, column = 1)
    qt2 = Entry(root)
    qt2.grid(row = 1, column = 3)
    Ingr3 =  AutocompleteCombobox(
        root,
        width=30,
        font=('Times', 18),
        completevalues=ingredients
    )
        
    Ingr3.grid(row = 2, column = 1)
    qt3= Entry(root)
    qt3.grid(row = 2, column = 3)
    Ingr4 =  AutocompleteCombobox(
        root,
        width=30,
        font=('Times', 18),
        completevalues=ingredients
    )
    
    Ingr4.grid(row = 3, column = 1)
    qt4 = Entry(root)
    qt4.grid(row = 3, column = 3)
    Ingr5 =  AutocompleteCombobox(
        root,
        width=30,
        font=('Times', 18),
        completevalues=ingredients
    )
    
    Ingr5.grid(row = 4, column = 1)
    qt5 = Entry(root)
    qt5.grid(row = 4, column = 3)
    Ingr6 =  AutocompleteCombobox(
        root,
        width=30,
        font=('Times', 18),
        completevalues=ingredients
    )
    
    Ingr6.grid(row = 5, column = 1)
    qt6 = Entry(root)
    qt6.grid(row = 5, column = 3)
    Ingr7 =  AutocompleteCombobox(
        root,
        width=30,
        font=('Times', 18),
        completevalues=ingredients
    )
    
    Ingr7.grid(row = 6, column = 1)
    qt7 = Entry(root)
    qt7.grid(row = 6, column = 3)
    Ingr8 =  AutocompleteCombobox(
        root,
        width=30,
        font=('Times', 18),
        completevalues=ingredients
    )
    
    Ingr8.grid(row = 7, column = 1)
    qt8 = Entry(root)
    qt8.grid(row = 7, column = 3)
    Button(root, text = "submit",
           command = lambda:[getInput(),display_results(params)]).grid(row = 8, column=0)
        Button(
        NutriBoys,
        text = 'Menu Page',
        font = font,
        command= MenuPage
    ).grid(row = 8, column=2)       
    root.mainloop()

### Initialization

#Initialization

NutriBoys = Tk()
NutriBoys.geometry("600x400")
NutriBoys.title("NutriBoys")
background_image = PhotoImage(file = "C:\\Users\\Baptiste\\Pictures\\MenuPageBackground.png")
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
).place(x=250, y=200)

Button(
    NutriBoys,
    text = "Macro Calculator",
    font = font,
    command = MacroCalculatorPage
).place(x=450, y=200)

#Execution

NutriBoys.mainloop()




