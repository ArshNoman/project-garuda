from perception.oakd_stream import OakDStream
import cv2

stream = OakDStream()
stream.start()

while True:
    frame = stream.get_frame()
    if frame is not None:
        cv2.imshow("Oak-D Lite", frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
stream.stop()
