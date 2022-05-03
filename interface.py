### Menu Interface ###

### Modules ##

from tkinter import *

### MenuPage ###

def MenuPage(NutriBoys):

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
        command = PreferencesPage(NutriBoys)
    ).place(x=50, y=200)

    Button(
        NutriBoys,
        text = "Meal Request",
        font = font,
        command = MealRecommandationPage(NutriBoys)
    ).place(x=250, y=200)

    Button(
        NutriBoys,
        text = "Macro Calculator",
        font = font,
        command = MacroCalculatorPage(NutriBoys)
    ).place(x=450, y=200)

    #Execution

    NutriBoys.mainloop()

### PreferencesPage ###

def PreferencesPage(NutriBoys):

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
        command = MenuPage(NutriBoys)
    ).place(x=75, y=550)

    # Execution

    NutriBoys.mainloop()

###

'''def MealRecommandationPage(NutriBoys):
    NutriBoys.destroy()
    import MealRecommandationPage(NutriBoys)

###

def MacroCalculatorPage(NutriBoys):
    NutriBoys.destroy()
    import MacroCalculatorPage(NutriBoys)
    '''
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
    command = PreferencesPage(NutriBoys)
).place(x=50, y=200)

Button(
    NutriBoys,
    text = "Meal Request",
    font = font,
    command = MealRecommandationPage(NutriBoys)
).place(x=250, y=200)

Button(
    NutriBoys,
    text = "Macro Calculator",
    font = font,
    command = MacroCalculatorPage(NutriBoys)
).place(x=450, y=200)

#Execution

NutriBoys.mainloop()
