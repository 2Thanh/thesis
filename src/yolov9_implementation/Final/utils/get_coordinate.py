def get_coordinate(results):
    """Extract coordinates of detected objects from YOLO results.
    
    Args:
        results: YOLO detection results
        
    Returns:
        list: List of coordinates [(x1,y1), (x2,y2), ...]
    """
    coordinates = []
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x_center = (x1 + x2) / 2
            y_center = (y1 + y2) / 2
            coordinates.append((int(x_center), int(y_center)))
    return coordinates