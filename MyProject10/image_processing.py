import cv2
import numpy as np
from real_menu import real_menu
from color_definitions import color_ranges, dish_ratios

def calculate_ratio(w, h):
    return w / float(h) if h != 0 else 0


def contour_matches(contour):
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)

    # Otomatik olarak kenar sayısına göre şekli belirleyin
    if len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)

        if aspect_ratio >= 0.95 and aspect_ratio <= 1.05:
            return "square"
        else:
            return "rectangle"
    else:
        return "unknown"


def capture_image_from_camera(save_path='image.jpg'):
    cap = cv2.VideoCapture(0)  # Kamerayı aç
    if not cap.isOpened():
        print("Error: Camera not found.")
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Cannot read frame.")
            continue

        cv2.imshow("Camera", frame)

        # 'q' tuşuna basıldığında döngüyü kır
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.imwrite(save_path, frame)  # Son görüntüyü kaydet
            print(f"Image successfully saved to {save_path}")
            break

    cap.release()
    cv2.destroyAllWindows()
    return save_path



def match_dish(ratio, dish_ratios_for_color):
    # Bu fonksiyon yemeklerin oranlarını içeren dish_ratios_for_color sözlüğünü kullanarak
    # en yakın oranı bulacak şekilde güncellendi.
    closest_dish = None
    min_diff = float('inf')
    for dish_name, dish_ratio in dish_ratios_for_color.items():
        diff = abs(dish_ratio - ratio)
        if diff < min_diff:
            min_diff = diff
            closest_dish = dish_name
    return closest_dish


def detect_color(hsv, contour):
    # Create a mask where the contours are going to be drawn
    mask = np.zeros(hsv.shape[:2], dtype=np.uint8)

    # Ensure that contours are in a list as expected by drawContours function
    cv2.drawContours(mask, [contour], -1, color=(255, 255, 255), thickness=-1)

    color_detected = None
    for color_name, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        color_mask = cv2.inRange(hsv, lower, upper)
        if cv2.countNonZero(color_mask) > 0:
            color_detected = color_name
            break
    return color_detected

# Renk ve şekil tespiti yapan fonksiyon
def detect_shapes_and_colors(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    detected_items = []
    min_contour_area = 100  # Nesne boyutuna göre ayarlayın

    for color_name, (lower, upper) in color_ranges.items():
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)
        mask = cv2.inRange(hsv, lower, upper)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for contour in contours:
            if cv2.contourArea(contour) > min_contour_area:
                shape = contour_matches(contour)
                x, y, w, h = cv2.boundingRect(contour)
                ratio = calculate_ratio(w, h)
                detected_items.append({
                    'color': color_name,
                    'shape': shape,
                    'ratio': ratio
                })

    return detected_items



def match_dishes(detected_items, real_menu, dish_ratios):
    matched_dishes = []
    total_price = 0

    for item in detected_items:
        detected_color = item['color']
        detected_shape = item['shape']
        detected_ratio = item['ratio']

        closest_match = None
        smallest_diff = float('inf')

        for dish in real_menu:
            dish_ratio = dish_ratios[detected_color][dish.name.lower()]
            diff = abs(dish_ratio - detected_ratio)

            if diff < smallest_diff and dish.color == detected_color and dish.shape == detected_shape:
                smallest_diff = diff
                closest_match = dish

        if closest_match:
            matched_dishes.append(closest_match)
            total_price += closest_match.price

    return matched_dishes, total_price





def detect_shape(contour):
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)
    if len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        aspect_ratio = w / float(h)
        if aspect_ratio >= 0.8 and aspect_ratio <= 1.2:
            return "Square"
        return "Rectangle"
    return "Unknown"


def process_image(image_path, real_menu, dish_ratios):
    img = cv2.imread(image_path)
    if img is None:
        raise FileNotFoundError("The image file was not found at the path: " + image_path)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    detected_items = detect_shapes_and_colors(hsv)

    return detected_items

def test_image_processing(image_path):
    detected_items = process_image(image_path, real_menu, dish_ratios)
    matched_dishes, total_price = match_dishes(detected_items, real_menu)
    print_matched_dishes(matched_dishes)



def process_detected_shapes(detected_items, real_menu):
    matched_dishes = []
    for item in detected_items:
        detected_color = item['color']
        detected_shape = item['shape']
        detected_ratio = item['ratio']

        closest_match = None
        smallest_diff = float('inf')

        for dish in real_menu:
            dish_ratio = dish_ratios[detected_color][dish.name.lower()]
            diff = abs(dish_ratio - detected_ratio)

            if diff < smallest_diff and dish.color == detected_color and dish.shape == detected_shape:
                smallest_diff = diff
                closest_match = dish

        if closest_match:
            matched_dishes.append(closest_match)

    return matched_dishes



def print_matched_dishes(matched_dishes):
    total_price = 0
    for dish in matched_dishes:
        print(f"{dish.name} - {dish.color} color, {dish.shape} shape, Price: {dish.price} TL")
        total_price += dish.price
    print(f"Total price: {total_price} TL")



if __name__ == "__main__":
    image_path = '/Users/canacar/Desktop/lego.images/image.jpg'  # Replace with your actual image path
    detected_items = process_image(image_path, real_menu, dish_ratios)
    # Eşleşen yemekleri bul ve yazdır
    matched_dishes, total_price = match_dishes(detected_items, real_menu, dish_ratios)
    print_matched_dishes(matched_dishes, total_price)