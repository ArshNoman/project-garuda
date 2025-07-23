import depthai as dai
import cv2

# Create pipeline
pipeline = dai.Pipeline()

# Create mono cameras
cam_left = pipeline.create(dai.node.MonoCamera)
cam_right = pipeline.create(dai.node.MonoCamera)

# Set camera properties
cam_left.setBoardSocket(dai.CameraBoardSocket.LEFT)
cam_right.setBoardSocket(dai.CameraBoardSocket.RIGHT)
cam_left.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
cam_right.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)

# Create XLink outputs
xout_left = pipeline.create(dai.node.XLinkOut)
xout_right = pipeline.create(dai.node.XLinkOut)
xout_left.setStreamName("left")
xout_right.setStreamName("right")

# Link cameras to outputs
cam_left.out.link(xout_left.input)
cam_right.out.link(xout_right.input)

# Run pipeline
with dai.Device(pipeline) as device:
    q_left = device.getOutputQueue(name="left", maxSize=1, blocking=True)
    q_right = device.getOutputQueue(name="right", maxSize=1, blocking=True)

    print("Capturing stereo frame...")
    left_frame = q_left.get().getCvFrame()
    right_frame = q_right.get().getCvFrame()

    # Save frames
    cv2.imwrite("left.png", left_frame)
    cv2.imwrite("right.png", right_frame)
    print("Saved: left.png and right.png")
