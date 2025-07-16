# src/perception/tracking.py

import depthai as dai
import blobconverter
import cv2
import numpy as np

class ObjectTracker:
    COCO_LABELS = {
        0: "person", 1: "bicycle", 2: "car", 3: "motorbike", 4: "aeroplane",
        5: "bus", 6: "train", 7: "truck", 8: "boat", 9: "traffic light",
        10: "fire hydrant", 11: "stop sign", 12: "parking meter", 13: "bench",
        14: "bird", 15: "cat", 16: "dog", 17: "horse", 18: "sheep", 19: "cow",
        20: "elephant", 21: "bear", 22: "zebra", 23: "giraffe", 24: "backpack",
        25: "umbrella", 26: "handbag", 27: "tie", 28: "suitcase", 29: "frisbee",
        30: "skis", 31: "snowboard", 32: "sports ball", 33: "kite", 34: "bat",
        35: "glove", 36: "skateboard", 37: "surfboard", 38: "tennis racket",
        39: "bottle", 40: "wine glass", 41: "cup", 42: "fork", 43: "knife",
        44: "spoon", 45: "bowl", 46: "banana", 47: "apple", 48: "sandwich",
        49: "orange", 50: "broccoli", 51: "carrot", 52: "hot dog", 53: "pizza",
        54: "donut", 55: "cake", 56: "chair", 57: "sofa", 58: "potted plant",
        59: "bed", 60: "dining table", 61: "toilet", 62: "tv", 63: "laptop",
        64: "mouse", 65: "remote", 66: "keyboard", 67: "phone", 68: "microwave",
        69: "oven", 70: "toaster", 71: "sink", 72: "fridge", 73: "book",
        74: "clock", 75: "vase", 76: "scissors", 77: "teddy bear", 78: "hair drier",
        79: "toothbrush"
    }

    def __init__(self):
        self.pipeline = dai.Pipeline()

        # Mono cameras (for stereo)
        cam_left = self.pipeline.createMonoCamera()
        cam_right = self.pipeline.createMonoCamera()
        cam_left.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
        cam_left.setBoardSocket(dai.CameraBoardSocket.LEFT)
        cam_right.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
        cam_right.setBoardSocket(dai.CameraBoardSocket.RIGHT)

        # Stereo depth
        stereo = self.pipeline.createStereoDepth()
        stereo.setDefaultProfilePreset(dai.node.StereoDepth.PresetMode.HIGH_DENSITY)
        cam_left.out.link(stereo.left)
        cam_right.out.link(stereo.right)

        # RGB camera
        cam_rgb = self.pipeline.createColorCamera()
        cam_rgb.setPreviewSize(640, 352)
        cam_rgb.setInterleaved(False)
        cam_rgb.setBoardSocket(dai.CameraBoardSocket.RGB)
        cam_rgb.setColorOrder(dai.ColorCameraProperties.ColorOrder.BGR)
        cam_rgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
        cam_rgb.setPreviewKeepAspectRatio(False)

        # YOLOv6 detection network
        detection_nn = self.pipeline.createYoloDetectionNetwork()
        detection_nn.setBlobPath("models/yolov6nr3_coco_640x352.blob")
        detection_nn.setConfidenceThreshold(0.5)
        detection_nn.setNumClasses(80)
        detection_nn.setCoordinateSize(4)
        detection_nn.setAnchors([
            10,13, 16,30, 33,23, 30,61, 62,45, 59,119, 116,90, 156,198, 373,326
        ])
        detection_nn.setAnchorMasks({
            "side52": [0,1,2],
            "side26": [3,4,5],
            "side13": [6,7,8]
        })
        detection_nn.setIouThreshold(0.5)
        detection_nn.input.setBlocking(False)

        cam_rgb.preview.link(detection_nn.input)

        # Output links
        xout_rgb = self.pipeline.createXLinkOut()
        xout_rgb.setStreamName("rgb")
        cam_rgb.preview.link(xout_rgb.input)

        xout_nn = self.pipeline.createXLinkOut()
        xout_nn.setStreamName("detections")
        detection_nn.out.link(xout_nn.input)

        xout_depth = self.pipeline.createXLinkOut()
        xout_depth.setStreamName("depth")
        stereo.depth.link(xout_depth.input)

        self.device = None
        self.rgb_queue = None
        self.detection_queue = None
        self.depth_queue = None

    def start(self):
        self.device = dai.Device(self.pipeline)
        self.rgb_queue = self.device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
        self.detection_queue = self.device.getOutputQueue(name="detections", maxSize=4, blocking=False)
        self.depth_queue = self.device.getOutputQueue(name="depth", maxSize=4, blocking=False)
        print("[INFO] ObjectTracker with Depth started.")

    def get_detections(self):
        frame = self.rgb_queue.get().getCvFrame()
        detections = self.detection_queue.get().detections
        depth_frame = self.depth_queue.get().getFrame()

        results = []
        for det in detections:
            label_id = det.label
            label = self.COCO_LABELS.get(label_id, f"label_{label_id}")
            x1 = int(det.xmin * frame.shape[1])
            y1 = int(det.ymin * frame.shape[0])
            x2 = int(det.xmax * frame.shape[1])
            y2 = int(det.ymax * frame.shape[0])
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            # mm to m
            patch_size = 5
            half = patch_size // 2
            h, w = depth_frame.shape

            # clamp window bounds to image size
            x_start = max(cx - half, 0)
            x_end = min(cx + half + 1, w)
            y_start = max(cy - half, 0)
            y_end = min(cy + half + 1, h)

            depth_patch = depth_frame[y_start:y_end, x_start:x_end]
            valid_depths = depth_patch[depth_patch > 0]  # filter out zeros

            depth_m = None
            if valid_depths.size > 0:
                depth_m = np.median(valid_depths) / 1000.0  # convert mm → meters

            result = {
                "label": label,
                "bbox": (x1, y1, x2, y2),
                "center": (cx, cy),
                "depth_m": depth_m,
                "confidence": det.confidence
            }
            results.append(result)

            # Draw
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
            text = f"{label} {det.confidence:.2f}"
            if depth_m:
                text += f" {depth_m:.2f}m"
            cv2.putText(frame, text, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)

        return frame, results

    def stop(self):
        if self.device:
            self.device.close()
            print("[INFO] ObjectTracker stopped.")
