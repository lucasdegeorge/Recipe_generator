# Recipe_generator


The objective of this project is to create a program that allows to suggest a meal and a recipe to a user based on the ingredients and products they have in their refrigerator. 

The program must be able to take into account the constraints and requirements of different types of diets. These may include vegetarian diets, gluten-free diets, weight loss diets or weight gain diets.


The specifications are as follows:
- Determine the most "profitable" recipe for the user
- Determine the most "beneficial" shop for the user
- Provide a shopping list to the user

"Advantageous" means the shop that allows the user to minimise the price and distance to the shop. 
"Profitable" means the recipe that best meets the user's preferences. 

We first determined the nutritional data on the various ingredients used in the recipes. ingredients taken into account in the recipes.
Then, we created a geolocation program to find the shops and supermarkets closest to the user.
Finally, we created a program to determine the most profitable recipe.



At the beginning of the program, the path of the folder where the images are located on the user's computer must be entered in the path variable in the first lines of the file NutriBoys.py.

The file NutriBoys.py is the one to be executed to launch the program and the graphic interface.

Requirements : 
— numpy
— pandas
— ramdom
— os
— math
— googlemaps
— geopy
— time
— tkinter
— ttkwidgets
