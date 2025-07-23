with open("../ThirdParty/ORB-SLAM3/live_stream/mav0/times.txt", "w") as f:
    for i in range(30):
        ts = 0.03 * i  # simulate 30 Hz spacing
        f.write(f"{ts:.9f}\n")