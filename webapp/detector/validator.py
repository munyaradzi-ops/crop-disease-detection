import cv2
import numpy as np
from PIL import Image

def verify_leaf_integrity(file_path):
    """
    Professional CV preprocessing check.
    Ensures the image contains an organic leaf signature using HSV segmentation.
    Returns: (is_valid, error_message_or_metrics)
    """
    try:
        # 1. Load image matrix natively via OpenCV
        img = cv2.imread(str(file_path))
        if img is None:
            return False, "Unable to read or parse image file matrix."

        height, width, _ = img.shape
        total_pixels = height * width

        # Convert to HSV color space (highly stable for lighting variance)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # 2. Define the Color Range for Organic Foliage (Greens, Yellows, Browns)
        # Lower bound catches deep browns and yellow blights
        lower_foliage = np.array([5, 30, 30])
        # Upper bound catches vibrant greens and deep forest hues
        upper_foliage = np.array([85, 255, 255])

        # Create a binary mask (pixels in range turn White, others turn Black)
        mask = cv2.inRange(hsv, lower_foliage, upper_foliage)

        # 3. Calculate Foliage Density Score
        foliage_pixels = cv2.countNonZero(mask)
        foliage_ratio = (foliage_pixels / total_pixels) * 100

        # Enforce that at least 20% of the photo contains leaf matter
        if foliage_ratio < 20.0:
            return False, "Foliage verification failed: No prominent plant matter detected."

        # 4. Contour Area Verification (Ensures it's a solid leaf structure, not noise)
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not contours:
            return False, "Structural layout check failed: Missing organic contour lines."

        # Get the largest solid shape in the frame
        largest_contour = max(contours, key=cv2.contourArea)
        largest_area_ratio = (cv2.contourArea(largest_contour) / total_pixels) * 100

        # The primary leaf must represent at least 8% of the continuous frame size
        if largest_area_ratio < 8.0:
            return False, "Foliage framing issue: Plant leaf is too far or small."

        # 🎉 PASSED VISUAL METRICS: Valid Leaf
        return True, {
            "foliage_coverage": f"{foliage_ratio:.2f}%",
            "primary_contour": f"{largest_area_ratio:.2f}%"
        }

    except Exception as e:
        return False, f"Preprocessing runtime anomaly: {str(e)}"
