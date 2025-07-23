#include <iostream>
#include <chrono>
#include <opencv2/opencv.hpp>
#include <System.h>
#include <depthai/depthai.hpp>

using namespace std;

int main(int argc, char **argv) {
    if (argc != 3) {
        cerr << "Usage: ./stereo_oakd path_to_vocabulary path_to_settings" << endl;
        return 1;
    }

    // Load SLAM
    ORB_SLAM3::System SLAM(argv[1], argv[2], ORB_SLAM3::System::STEREO, true);

    // Set up DepthAI pipeline
    dai::Pipeline pipeline;
    auto camLeft = pipeline.create<dai::node::MonoCamera>();
    auto camRight = pipeline.create<dai::node::MonoCamera>();
    auto xoutLeft = pipeline.create<dai::node::XLinkOut>();
    auto xoutRight = pipeline.create<dai::node::XLinkOut>();

    camLeft->setBoardSocket(dai::CameraBoardSocket::LEFT);
    camRight->setBoardSocket(dai::CameraBoardSocket::RIGHT);
    camLeft->setResolution(dai::MonoCameraProperties::SensorResolution::THE_400_P);
    camRight->setResolution(dai::MonoCameraProperties::SensorResolution::THE_400_P);
    camLeft->setFps(30);
    camRight->setFps(30);

    xoutLeft->setStreamName("left");
    xoutRight->setStreamName("right");
    camLeft->out.link(xoutLeft->input);
    camRight->out.link(xoutRight->input);

    dai::Device device(pipeline);
    auto qLeft = device.getOutputQueue("left", 8, false);
    auto qRight = device.getOutputQueue("right", 8, false);

    cout << "Starting Oak-D SLAM..." << endl;

    while (true) {
        auto leftFrame = qLeft->get<dai::ImgFrame>();
        auto rightFrame = qRight->get<dai::ImgFrame>();

        if (!leftFrame || !rightFrame) continue;

        cv::Mat left = leftFrame->getCvFrame();
        cv::Mat right = rightFrame->getCvFrame();
        double timestamp = chrono::duration_cast<chrono::duration<double>>(
                               chrono::steady_clock::now().time_since_epoch()).count();

        SLAM.TrackStereo(left, right, timestamp);

        cv::imshow("Left", left);
        cv::imshow("Right", right);
        if (cv::waitKey(1) == 27) break;  // ESC
    }

    SLAM.Shutdown();
    SLAM.SaveTrajectoryEuRoC("Live_CameraTrajectory.txt");
    SLAM.SaveKeyFrameTrajectoryEuRoC("Live_KeyFrameTrajectory.txt");
    return 0;
}
