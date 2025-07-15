import depthai as dai
import blobconverter
import cv2


class ObjectTracker:
    def __init__(self):
        self.pipeline = dai.Pipeline()

        cam_rgb = self.pipeline.createColorCamera()
        cam_rgb.setPreviewSize(300, 300)
        cam_rgb.setInterleaved(False)
        cam_rgb.setBoardSocket(dai.CameraBoardSocket.RGB)

        detection_nn = self.pipeline.createMobileNetDetectionNetwork()
        detection_nn.setBlobPath(blobconverter.from_zoo(name='mobilenet-ssd', shaves=6))
        detection_nn.setConfidenceThreshold(0.5)

        cam_rgb.preview.link(detection_nn.input)

        xout_rgb = self.pipeline.createXLinkOut()
        xout_rgb.setStreamName("rgb")
        cam_rgb.preview.link(xout_rgb.input)

        xout_nn = self.pipeline.createXLinkOut()
        xout_nn.setStreamName("detections")
        detection_nn.out.link(xout_nn.input)

        self.device = None
        self.rgb_queue = None
        self.detection_queue = None

    def start(self):
        self.device = dai.Device(self.pipeline)
        self.rgb_queue = self.device.getOutputQueue(name="rgb", maxSize=4, blocking=False)
        self.detection_queue = self.device.getOutputQueue(name="detections", maxSize=4, blocking=False)
        print("[INFO] ObjectTracker pipeline started.")

    def get_detections(self):
        frame = self.rgb_queue.get().getCvFrame()
        detections = self.detection_queue.get().detections

        results = []
        for det in detections:
            label = det.label
            x1 = int(det.xmin * frame.shape[1])
            y1 = int(det.ymin * frame.shape[0])
            x2 = int(det.xmax * frame.shape[1])
            y2 = int(det.ymax * frame.shape[0])
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            result = {
                "label": label,
                "bbox": (x1, y1, x2, y2),
                "center": (cx, cy),
                "confidence": det.confidence
                # We will add 'depth' later via stereo
            }
            results.append(result)

            # box drawing
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{label} {det.confidence:.2f}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

        return frame, results

    def stop(self):
        if self.device:
            self.device.close()
            print("[INFO] ObjectTracker stopped.")
