import random

class SLAMModule:
    def __init__(self):
        self.tracking = False
        self.pose = {
            'position': (0.0, 0.0, 0.0),
            'orientation': (0.0, 0.0, 0.0),
            'status': 'NOT_STARTED'
        }

    def start(self):
        print("[INFO] SLAMModule started.")
        self.tracking = True
        self.pose['status'] = 'INITIALIZING'

    def update(self):
        # placeholder: simulate pose updates
        if not self.tracking:
            return

        # simulate pose drift
        dx = random.uniform(-0.01, 0.01)
        dy = random.uniform(-0.01, 0.01)
        dz = random.uniform(-0.01, 0.01)

        x, y, z = self.pose['position']
        x += dx
        y += dy
        z += dz

        # simulate orientation (in degrees)
        roll = random.uniform(-1, 1)
        pitch = random.uniform(-1, 1)
        yaw = random.uniform(-1, 1)

        self.pose['position'] = (x, y, z)
        self.pose['orientation'] = (roll, pitch, yaw)
        self.pose['status'] = 'OK'

    def get_pose(self):
        return self.pose

    def is_tracking(self):
        return self.tracking and self.pose['status'] == 'OK'

    def stop(self):
        self.tracking = False
        self.pose['status'] = 'STOPPED'
        print("[INFO] SLAMModule stopped.")
