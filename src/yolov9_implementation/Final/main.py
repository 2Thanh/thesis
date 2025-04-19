import os
import sys
import cv2
import time
import numpy as np
from datetime import datetime
from ultralytics import YOLO
from utils.get_coordinate import get_coordinate
from utils.get_rrt import rrt_path
from utils.gui import GUI

# Load YOLOv8 model
model = YOLO("yolov8x.pt")

def main():
    # Initialize GUI
    gui = GUI()

    # Process detection and path planning
    while True:
        start_time = time.time()
        
        # Capture frame from camera
        frame = gui.get_frame()
        if frame is None:
            continue

        # Run YOLOv8 inference on the frame
        results = model(frame)
        
        # Visualize the results on the frame
        annotated_frame = results[0].plot()

        # Get coordinates of detected objects
        coordinates = get_coordinate(results)
        
        if coordinates:
            # Get path using RRT algorithm
            path = rrt_path(coordinates)
            
            # Draw path on frame if available
            if path:
                for i in range(len(path) - 1):
                    pt1 = (int(path[i][0]), int(path[i][1]))
                    pt2 = (int(path[i + 1][0]), int(path[i + 1][1]))
                    cv2.line(annotated_frame, pt1, pt2, (0, 255, 0), 2)

        # Display the annotated frame
        gui.show_frame(annotated_frame)
        
        # Calculate and display FPS
        fps = 1.0 / (time.time() - start_time)
        print(f"FPS: {fps:.2f}")

        # Save detection results periodically
        current_time = datetime.now().strftime("%Y%m%d-%H%M%S")
        cv2.imwrite(f"Final/detection_{current_time}.jpg", annotated_frame)
        
        # Break loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    gui.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()