import cv2

class GUI:
    def __init__(self, camera_index=0):
        """Initialize GUI with camera.
        
        Args:
            camera_index: Index of the camera to use
        """
        self.cap = cv2.VideoCapture(camera_index)
        
    def get_frame(self):
        """Capture frame from camera.
        
        Returns:
            numpy.ndarray: Captured frame or None if failed
        """
        ret, frame = self.cap.read()
        if ret:
            return frame
        return None
        
    def show_frame(self, frame):
        """Display frame in window.
        
        Args:
            frame: Frame to display
        """
        cv2.imshow('YOLOv9 Detection', frame)
        
    def release(self):
        """Release camera resources."""
        self.cap.release()