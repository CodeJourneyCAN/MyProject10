# user_selection_processing.py
from color_definitions import color_ranges
from color_definitions import dish_ratios
from real_menu import real_menu

def process_user_selection(selections):
    matched_items = []
    for selection in selections:
        for dish in real_menu:
            if dish.color == selection["color"] and dish.shape == selection["shape"]:
                matched_items.append(dish)
    return matched_items