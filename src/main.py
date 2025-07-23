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

def stream_to_disk():
    import depthai as dai
    import cv2
    import os
    import time

    left_dir = "../ThirdParty/ORB-SLAM3/live_stream/mav0/cam0/data"
    right_dir = "../ThirdParty/ORB-SLAM3/live_stream/mav0/cam1/data"
    os.makedirs(left_dir, exist_ok=True)
    os.makedirs(right_dir, exist_ok=True)

    pipeline = dai.Pipeline()
    left = pipeline.createMonoCamera()
    right = pipeline.createMonoCamera()
    left.setBoardSocket(dai.CameraBoardSocket.LEFT)
    right.setBoardSocket(dai.CameraBoardSocket.RIGHT)
    left.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
    right.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)

    xout_left = pipeline.createXLinkOut()
    xout_right = pipeline.createXLinkOut()
    xout_left.setStreamName("left")
    xout_right.setStreamName("right")
    left.out.link(xout_left.input)
    right.out.link(xout_right.input)

    device = dai.Device(pipeline)
    q_left = device.getOutputQueue("left", maxSize=1, blocking=False)
    q_right = device.getOutputQueue("right", maxSize=1, blocking=False)

    print("[INFO] Writing stereo frames...")

    i = 0
    while i < 30:
        left_frame = q_left.get().getCvFrame()
        right_frame = q_right.get().getCvFrame()

        fname = f"{i:06d}.png"
        cv2.imwrite(f"{left_dir}/{fname}", left_frame)
        cv2.imwrite(f"{right_dir}/{fname}", right_frame)

        i += 1
        time.sleep(0.03)


stream_to_disk()

