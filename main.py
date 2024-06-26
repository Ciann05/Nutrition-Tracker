from fatsecret import Fatsecret
from datetime import date
import macro_planner
import configparser
import food_ai
import food
import auth


# FatSecret API credentials
fs = Fatsecret('b11b1bef016949aaacc0b6f8cf6c93bd','6c82dcbe422042dc9fddb96d5759de23')
today = date.today()
# Format the date
configparser.formatted_date = today.strftime("%B_%d_%Y")
table_name = f"planner_{configparser.formatted_date}"
configparser.var = 0
def main():
    auth.create_user_table()
    configparser.account = str(input("Do you have an account?(y/n)"))
    auth.account_info() 
    if configparser.var == 1: 
        food.create_food_table()
        food.create_recipe_table()
        food.create_recipe_nutrition_table()
        configparser.food_item = input("Choose a food: ")
        foods = fs.foods_search(configparser.food_item)
        food.insert_food_data(foods)
        recipes = fs.recipes_search(configparser.food_item)
        food.insert_recipe_data(recipes)
        food.insert_recipe_nutrition(recipes)
        food.select_food()
        macro_planner.create_planner_table()
        macro_planner.insert_in_planner(configparser.user_id)




if __name__ == "__main__":
    main()
    
