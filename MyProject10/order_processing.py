# order_processing.py
from image_processing import calculate_ratio
import cv2
from color_definitions import color_ranges
from color_definitions import dish_ratios
def check_selection_rules(selections):
    has_starter = False
    has_main_course = False
    selected_colors = set()

    for selection in selections:
        color = selection.color  # 'color' özelliği kullanılıyor
        shape = selection.shape  # 'shape' özelliği kullanılıyor

        # Başlangıç yemeği (starter) kontrolü
        if color in ["red", "blue", "green", "yellow"]:
            has_starter = True

        # Ana yemek (main course) kontrolü
        if color in ["red", "blue", "green"]:
            has_main_course = True

        # Aynı renkte birden fazla yemek seçimi kontrolü
        if color in selected_colors:
            return False  # Aynı renkte birden fazla yemek seçilmiş

        selected_colors.add(color)

    # Başlangıç yemeği (starter) ve ana yemek (main course) kontrolü
    if not has_starter or not has_main_course:
        return False  # Hem başlangıç hem de ana yemek seçilmemiş

    return True  # Tüm kurallara uygun

def calculate_total(menu, selections):
    total = 0
    order = []
    menu_dict = {}  # Menüyü bir sözlük olarak saklayın

    for group in menu:
        for dish in group.dishes:
            menu_dict[(dish.color, dish.shape)] = dish

    for selection in selections:
        color = selection["color"]
        shape = selection["shape"]
        dish = menu_dict.get((color, shape))
        if dish:
            total += dish.price
            order.append(dish.name)

    return total, order


def match_dishes(detected_items, real_menu, dish_ratios):
    matched_dishes = []
    for detected_color, detected_shape, detected_ratio in detected_items:
        # Eşleşen yemeği bulmak için real_menu ve dish_ratios kullanılacak
        closest_match = None
        smallest_diff = float('inf')
        for dish_name, dish_info in real_menu.items():
            if dish_info['color'] == detected_color:
                # Burada, her renk için oranların saklandığı dish_ratios sözlüğünü kullanarak
                # beklenen oranı buluyoruz
                expected_ratio = dish_ratios[detected_color][dish_name.lower()]
                ratio_diff = abs(expected_ratio - detected_ratio)
                if ratio_diff < smallest_diff:
                    smallest_diff = ratio_diff
                    closest_match = dish_name
        if closest_match:
            matched_dishes.append((closest_match, detected_color, detected_ratio))
    return matched_dishes




def print_order(matched_dishes):
    total_price = 0
    print("Your order includes:")
    for dish in matched_dishes:
        print(f"- {dish.name}, Price: {dish.price} TL")
        total_price += dish.price
    print(f"The total amount you have to pay: {total_price} TL")



def confirm_order(order, total):
    print(f"Your order is {order}, do you confirm?")
    confirmation = input("Please enter 'yes' to confirm or 'no' to cancel: ")
    return confirmation.lower() == 'yes', total