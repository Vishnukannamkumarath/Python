import cv2
import numpy as np

# Load the image from the user-provided path
image_path = '/Downloads/ch.jpeg'
image = cv2.imread(image_path)

# Define color ranges for the given scale (adjust these values based on the image)
color_ranges = {
    '5.0': ([0, 180, 180], [50, 255, 255]),
    '3.0': ([20, 180, 180], [70, 255, 255]),
    '1.5': ([30, 180, 180], [90, 255, 255]),
    '1.0': ([40, 180, 180], [110, 255, 255]),
    '0.6': ([50, 180, 180], [130, 255, 255])
}

def find_color_value(roi):
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    avg_color = np.mean(hsv_roi.reshape(-1, 3), axis=0)
    
    for value, (lower, upper) in color_ranges.items():
        lower = np.array(lower)
        upper = np.array(upper)
        if all(lower <= avg_color) and all(avg_color <= upper):
            return value
    return "Unknown"

# Crop the region of interest (adjust these coordinates based on the image)
# Here, I assume that the sample region is in the center of the image.
height, width, _ = image.shape
roi = image[int(height * 0.4):int(height * 0.6), int(width * 0.3):int(width * 0.7)]

# Find the value of the color in the region of interest
color_value = find_color_value(roi)

# Display the results
print(f"Detected color corresponds to the value: {color_value}")

# Display the ROI and the original image for reference
cv2.imshow("Region of Interest", roi)
cv2.imshow("Original Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
