# menu.py
from dishes import Dish, FoodGroup
from color_definitions import color_ranges
from color_definitions import dish_ratios
def create_menu():
    starters = FoodGroup("Starters", [
        Dish("Soup", "green", "square", 15),
        Dish("Cheese Platter", "green", "rectangle", 20),
        Dish("Garlic Bread", "green", "rectangle", 10)
    ])

    snacks = FoodGroup("Snacks", [
        Dish("Crispy Chicken", "red", "square", 25),
        Dish("Fish & Chips", "red", "rectangle", 30),
        Dish("Omlet", "red", "rectangle", 20)
    ])

    main_course = FoodGroup("Main Course", [
        Dish("Meatballs", "blue", "square", 35),
        Dish("Casseroles", "blue", "rectangle", 40),
        Dish("Fajitas", "blue", "rectangle", 45)
    ])

    desserts = FoodGroup("Desserts", [
        Dish("Souffle", "yellow", "square", 20),
        Dish("Tiramisu", "yellow", "rectangle", 25),
        Dish("Cheesecake", "yellow", "rectangle", 30)
    ])

    return [starters, snacks, main_course, desserts]