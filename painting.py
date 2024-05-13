import cv2
import numpy as np
from collections import deque
DEFAULT_RADIUS = 5
MAX_POINTS = 1000  
drawing = False
color = (255, 0, 0)  
radius = DEFAULT_RADIUS
points = deque(maxlen=MAX_POINTS)  

def draw(event, x, y, flags, param):
    global drawing, color, radius
    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        points.append((x, y, color, radius)) 
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            points.append((x, y, color, radius)) 
    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False

def main():
    canvas = np.zeros((800, 800, 3), dtype=np.uint8)  
    cv2.namedWindow("Custom Painting Application")
    cv2.setMouseCallback("Custom Painting Application", draw)
    while True:
        cv2.imshow("Custom Painting Application", canvas)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if points:
            for i in range(1, len(points)):
                x1, y1, col, rad = points[i-1]
                x2, y2, _, _ = points[i]
                cv2.line(canvas, (x1, y1), (x2, y2), col, rad * 2)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
