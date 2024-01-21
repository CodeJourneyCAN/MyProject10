# dishes.py

class Dish:
    def __init__(self, name, color, shape, price):
        self.name = name
        self.color = color
        self.shape = shape
        self.price = price

class FoodGroup:
    def __init__(self, group_name, dishes):
        self.group_name = group_name
        self.dishes = dishes