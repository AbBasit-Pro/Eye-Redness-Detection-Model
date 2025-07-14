import cv2
import numpy as np
from PIL import Image

def analyze_eye_condition(image: np.ndarray) -> str:
    """
    Basic heuristic to detect redness in the eye as a proxy for possible irritation.
    This is a very simple demo and not a medical diagnosis.
    """
    # Convert to HSV color space (better for color detection)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    # Define range for detecting red color in HSV
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])
    
    # Create masks for red regions
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    red_mask = cv2.bitwise_or(mask1, mask2)
    
    # Calculate percentage of red pixels
    red_ratio = np.sum(red_mask > 0) / (image.shape[0] * image.shape[1])
    
    # Threshold - if a significant amount of red pixels, flag irritation
    if red_ratio > 0.05:  # 5% red pixels or more
        return "Possible eye irritation or redness detected"
    else:
        return "Eye appears normal"

def check_eye_from_file(image_path: str):
    pil_image = Image.open(image_path).convert("RGB")
    open_cv_image = np.array(pil_image)
    open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
    result = analyze_eye_condition(open_cv_image)
    print(result)

if __name__ == "__main__":
    img_path = input("Enter the path of the eye image file: ")
    check_eye_from_file(img_path)

