from color_definitions import color_ranges
from color_definitions import dish_ratios
def get_user_selection():
    print("Please select your dishes by entering the color and shape (e.g., 'green square').")
    selections = []
    while True:
        choice = input("Enter your choice (or 'done' to finish): ").strip().lower()
        if choice == "done":
            break
        if ' ' in choice:
            color, shape = choice.split()
            selections.append({"color": color, "shape": shape})
        else:
            print("Invalid input format. Please enter in 'color shape' format.")
    return selections
