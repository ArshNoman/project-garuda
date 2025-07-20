# from perception.tracking import ObjectTracker
# import cv2
#
# tracker = ObjectTracker()
# tracker.start()
#
# while True:
#     frame, detections = tracker.get_detections()
#     cv2.imshow("YOLOv6 Detection", frame)
#
#     for det in detections:
#         print(det)
#
#     if cv2.waitKey(1) == ord('q'):
#         break
#
# tracker.stop()
# cv2.destroyAllWindows()

from navigation.slam_module import SLAMModule
import time

slam = SLAMModule()
slam.start()

for i in range(10):
    slam.update()  # frame will be passed here later
    print(slam.get_pose())
    time.sleep(0.5)

slam.stop()


# TEST COMMIT ON UBUNTU 24.02 VM

