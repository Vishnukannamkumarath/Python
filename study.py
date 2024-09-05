import cv2
import numpy as np

# Define a set of known colors and their BGR values
colors = {
    'Red': ([0, 0, 100], [100, 100, 255]),  # Lower and upper bounds for Red
    'Green': ([0, 100, 0], [100, 255, 100]),  # Lower and upper bounds for Green
    'Blue': ([100, 0, 0], [255, 100, 100]),  # Lower and upper bounds for Blue
    'Yellow': ([0, 100, 100], [100, 255, 255]),  # Lower and upper bounds for Yellow
}

def get_dominant_color(frame):
    # Resize the frame to reduce the number of pixels (and thus the processing time)
    small_frame = cv2.resize(frame, (64, 64))
    avg_color_per_row = np.average(small_frame, axis=0)
    avg_color = np.average(avg_color_per_row, axis=0)
    return avg_color

def find_closest_color(avg_color):
    min_diff = float('inf')
    best_color_name = None
    best_accuracy = 0.0

    for color_name, (lower, upper) in colors.items():
        lower = np.array(lower)
        upper = np.array(upper)
        
        # Calculate the distance from the average color to this color range
        diff = np.linalg.norm(avg_color - np.average([lower, upper], axis=0))

        # Calculate accuracy (how close the color is)
        accuracy = 100 - (diff / np.linalg.norm([255, 255, 255]) * 100)
        
        if diff < min_diff:
            min_diff = diff
            best_color_name = color_name
            best_accuracy = accuracy

    return best_color_name, best_accuracy

# Start capturing video from the webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    # Get the dominant color
    avg_color = get_dominant_color(frame)
    
    # Find the closest known color and its accuracy
    color_name, accuracy = find_closest_color(avg_color)

    # Display the result
    cv2.putText(frame, f"Color: {color_name}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f"Accuracy: {accuracy:.2f}%", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Show the frame
    cv2.imshow('Color Detection', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
