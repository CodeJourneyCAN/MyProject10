import cv2
import numpy as np
from image_processing import process_image
from real_menu import real_menu
from color_definitions import dish_ratios

def match_dishes(detected_items, real_menu):
    matched_dishes = []
    total_price = 0

    for item in detected_items:
        detected_color = item['color']
        detected_shape = item['shape']
        detected_ratio = item['ratio']

        closest_match = None
        smallest_diff = float('inf')

        for dish in real_menu:
            # Ensure the dish name is in the correct case
            dish_name_key = dish.name.lower() # or use .upper() based on your dictionary keys

            if dish_name_key in dish_ratios[detected_color]:
                dish_ratio = dish_ratios[detected_color][dish_name_key]
                diff = abs(dish_ratio - detected_ratio)

                if diff < smallest_diff and dish.color == detected_color and dish.shape == detected_shape:
                    smallest_diff = diff
                    closest_match = dish

        if closest_match:
            matched_dishes.append(closest_match)
            total_price += closest_match.price

    return matched_dishes, total_price


def print_order(matched_dishes, total_price):
    print("Your order includes:")
    for dish in matched_dishes:
        print(f"{dish.name} - {dish.color} color, {dish.shape} shape, Price: {dish.price} TL")
    print(f"The total amount you have to pay: {total_price} TL")

def main():
    # Kamerayı aç
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Hata: Kamera bulunamadı.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Hata: Görüntü okunamıyor.")
            continue

        # Burada frame'i işlemeye devam edebilirsiniz.
        # frame, işlenmiş görüntüyü temsil eder.

        cv2.imshow("Kamera", frame)

        # 'q' tuşuna basıldığında döngüyü sonlandır
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Görüntüyü işleyin ve yemekleri eşleştirin
    image_path = '/Users/canacar/Desktop/lego.images/image.jpg'  # Gerçek görüntü yoluyla değiştirin
    detected_items = process_image(image_path, real_menu, dish_ratios)
    matched_dishes, total_price = match_dishes(detected_items, real_menu)

    # Eşleşen yemekleri ve toplam fiyatı yazdırın
    print_order(matched_dishes, total_price)

if __name__ == "__main__":
    main()




