import depthai as dai
import cv2

class OakDStream:
    def __init__(self):
        self.pipeline = dai.Pipeline()

        # Create camera node
        cam_rgb = self.pipeline.createColorCamera()
        cam_rgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
        cam_rgb.setBoardSocket(dai.CameraBoardSocket.RGB)
        cam_rgb.setInterleaved(False)
        cam_rgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)

        # Create output node
        xout = self.pipeline.createXLinkOut()
        xout.setStreamName("video")
        cam_rgb.video.link(xout.input)

        self.device = None
        self.video_queue = None

        def start(self):
            # Start device and get output queue
            print("[INFO] Starting Oak-D pipeline...")
            self.device = dai.Device(self.pipeline)
            self.video_queue = self.device.getOutputQueue(name="video", maxSize=4, blocking=False)
            print("[INFO] Oak-D stream started.")

        def get_frame(self):
            if self.video_queue:
                in_frame = self.video_queue.get()
                frame = in_frame.getCvFrame()
                return frame
            else:
                return None

        def stop(self):
            if self.device:
                self.device.close()
                print("[INFO] Oak-D stream stopped.")

