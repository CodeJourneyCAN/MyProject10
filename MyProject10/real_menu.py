class RealDish:
    def __init__(self, name, color, shape, price, image_path):
        self.name = name
        self.color = color
        self.shape = shape
        self.price = price
        self.image_path = image_path

# Gerçek menüyü oluşturun
real_menu = [
    RealDish("Soup", "green", "square", 15, "/Users/canacar/Desktop/lego.images/soup.jpg"),
    RealDish("Cheese Platter", "green", "rectangle", 20, "/Users/canacar/Desktop/lego.images/cheese.jpg"),
    RealDish("Garlic", "green", "rectangle", 15, "/Users/canacar/Desktop/lego.images/garlic.jpg"),
    RealDish("Chicken", "red", "square", 20, "/Users/canacar/Desktop/lego.images/chicken.jpg"),
    RealDish("Fish", "red", "rectangle", 20, "/Users/canacar/Desktop/lego.images/fish.jpg"),
    RealDish("Omelet", "red", "rectangle", 20, "/Users/canacar/Desktop/lego.images/omelet.jpg"),
    RealDish("Meatballs", "blue", "square", 20, "/Users/canacar/Desktop/lego.images/meatballs.jpg"),
    RealDish("Casserole", "blue", "rectangle", 20, "/Users/canacar/Desktop/lego.images/casserole.jpg"),
    RealDish("Fajitas", "blue", "rectangle", 20, "/Users/canacar/Desktop/lego.images/fajitas.jpg"),
    RealDish("Souffle", "yellow", "square", 20, "/Users/canacar/Desktop/lego.images/souffle.jpg"),
    RealDish("Tiramisu", "yellow", "rectangle", 20, "/Users/canacar/Desktop/lego.images/tiramisu.jpg"),
    RealDish("Cheesecake", "yellow", "rectangle", 20, "/Users/canacar/Desktop/lego.images/cheesecake.jpg"),
]