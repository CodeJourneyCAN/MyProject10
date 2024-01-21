# user_input.py
from color_definitions import color_ranges
from color_definitions import dish_ratios
def get_user_selection():
    # Bu örnekte, kullanıcı girdisini terminal üzerinden alıyoruz.
    print("Please select your dishes by entering the color and shape (e.g., 'red circle').")
    selections = []
    while True:
        choice = input("Enter your choice (or 'done' to finish): ")
        if choice == "done":
            break
        color, shape = choice.split()
        selections.append({"color": color, "shape": shape})

    return selections