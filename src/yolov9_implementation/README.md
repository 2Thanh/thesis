# YOLOv9 Implementation

This implementation combines YOLOv9 object detection with RRT (Rapidly-exploring Random Tree) path planning for real-time object detection and navigation.

## Features

- Real-time object detection using YOLOv9
- Path planning using RRT algorithm
- Live camera feed processing
- Visualization of detections and planned paths
- FPS monitoring
- Automatic saving of detection results

## Requirements

- Python 3.x
- OpenCV
- Ultralytics YOLOv8
- NumPy

## Structure

- `main.py`: Main script that combines object detection and path planning
- `utils/`
  - `get_coordinate.py`: Extracts coordinates from YOLO detections
  - `get_rrt.py`: Implements RRT path planning algorithm
  - `gui.py`: Handles camera interface and visualization

## Usage

1. Install dependencies:
```bash
pip install ultralytics opencv-python numpy
```

2. Run the main script:
```bash
python main.py
```

Press 'q' to quit the application.

## Output

- Detection results are saved as images with timestamp (format: `detection_YYYYMMDD-HHMMSS.jpg`)
- Real-time FPS is displayed in the console
- Visualization shows:
  - Object detection boxes
  - Planned path in green