class RealDish:
    def __init__(self, name, color, shape, price, image_path):
        self.name = name
        self.color = color
        self.shape = shape
        self.price = price
        self.image_path = image_path

# Gerçek menüyü oluşturun
real_menu = [
    RealDish("Soup", "green", "square", 15, "/Users/canacar/Desktop/lego.images/Soup.jpg"),
    RealDish("Cheese Platter", "green", "rectangle", 20, "/Users/canacar/Desktop/lego.images/Cheese_Platter.jpg"),
    RealDish("Garlic", "green", "rectangle", 15, "/Users/canacar/Desktop/lego.images/Garlic.jpg"),
    RealDish("Chicken", "red", "square", 20, "/Users/canacar/Desktop/lego.images/Chicken.jpg"),
    RealDish("Fish", "red", "rectangle", 20, "/Users/canacar/Desktop/lego.images/Fish.jpg"),
    RealDish("Omelet", "red", "rectangle", 20, "/Users/canacar/Desktop/lego.images/Omelet.jpg"),
    RealDish("Meatballs", "blue", "square", 20, "/Users/canacar/Desktop/lego.images/Meatballs.jpg"),
    RealDish("Casserole", "blue", "rectangle", 20, "/Users/canacar/Desktop/lego.images/Casserole.jpg"),
    RealDish("Fajitas", "blue", "rectangle", 20, "/Users/canacar/Desktop/lego.images/Fajitas.jpg"),
    RealDish("Souffle", "yellow", "square", 20, "/Users/canacar/Desktop/lego.images/Souffle.jpg"),
    RealDish("Tiramisu", "yellow", "rectangle", 20, "/Users/canacar/Desktop/lego.images/Tiramisu.jpg"),
    RealDish("Cheesecake", "yellow", "rectangle", 20, "/Users/canacar/Desktop/lego.images/Cheesecake.jpg"),
]
