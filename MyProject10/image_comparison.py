#image_comparison
import cv2
import numpy as np
from image_processing import contour_matches




def compare_with_lego_images(customer_image_path, lego_images, color_ranges):
    customer_image = cv2.imread(customer_image_path)
    if customer_image is None:
        print("Error: Customer image not found.")
        return []

    customer_hsv = cv2.cvtColor(customer_image, cv2.COLOR_BGR2HSV)
    matched_items = []

    for dish_name, lego_image_path in lego_images.items():
        # Renk aralığını al
        color_range = color_ranges[dish_name]
        lower, upper = color_range
        lower = np.array(lower, dtype=np.uint8)
        upper = np.array(upper, dtype=np.uint8)

        # Müşteri resmindeki renk aralığına sahip alanları maskele
        mask = cv2.inRange(customer_hsv, lower, upper)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Konturlar içinde eşleşme olup olmadığını kontrol et
        for contour in contours:
            if contour_matches(contour):  # Bu fonksiyon konturun şeklini kontrol eder
                matched_items.append(dish_name)
                break  # Eşleşme bulundu, diğer konturlara bakmaya gerek yok

    return matched_items
