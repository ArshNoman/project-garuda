# src/main.py
from perception.tracking import ObjectTracker
import cv2

tracker = ObjectTracker()
tracker.start()

while True:
    frame, detections = tracker.get_detections()
    cv2.imshow("YOLOv6 Detection", frame)

    for det in detections:
        print(det)

    if cv2.waitKey(1) == ord('q'):
        break

tracker.stop()
cv2.destroyAllWindows()
