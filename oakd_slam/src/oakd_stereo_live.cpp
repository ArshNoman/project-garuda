#include <iostream>
#include <chrono>

#include <opencv2/opencv.hpp>
#include <depthai/depthai.hpp>

#include "System.h"

int main(int argc, char** argv) {
    if(argc != 3){
        std::cerr << "Usage: ./oakd_stereo_live path_to_vocabulary path_to_settings" << std::endl;
        return 1;
    }

    std::string vocabPath = argv[1];
    std::string configPath = argv[2];

    dai::Pipeline pipeline;

    auto camLeft = pipeline.create<dai::node::MonoCamera>();
    auto camRight = pipeline.create<dai::node::MonoCamera>();
    auto stereo = pipeline.create<dai::node::StereoDepth>();

    camLeft->setResolution(dai::MonoCameraProperties::SensorResolution::THE_400_P);
    camLeft->setBoardSocket(dai::CameraBoardSocket::LEFT);
    camRight->setResolution(dai::MonoCameraProperties::SensorResolution::THE_400_P);
    camRight->setBoardSocket(dai::CameraBoardSocket::RIGHT);

    camLeft->out.link(stereo->setInputMonoLeft());
    camRight->out.link(stereo->setInputMonoRight());

    stereo->setRectifyEdgeFillColor(0); // black, to better see the cut
    stereo->setLeftRightCheck(true);
    stereo->setExtendedDisparity(false);
    stereo->setSubpixel(false);

    auto xoutLeft = pipeline.create<dai::node::XLinkOut>();
    auto xoutRight = pipeline.create<dai::node::XLinkOut>();

    xoutLeft->setStreamName("left");
    xoutRight->setStreamName("right");

    stereo->rectifiedLeft.link(xoutLeft->input);
    stereo->rectifiedRight.link(xoutRight->input);

    dai::Device device(pipeline);
    auto leftQueue = device.getOutputQueue("left", 4, false);
    auto rightQueue = device.getOutputQueue("right", 4, false);

    ORB_SLAM3::System SLAM(vocabPath, configPath, ORB_SLAM3::System::STEREO, true);

    while(true) {
        auto leftFrame = leftQueue->get<dai::ImgFrame>();
        auto rightFrame = rightQueue->get<dai::ImgFrame>();

        cv::Mat left = leftFrame->getCvFrame();
        cv::Mat right = rightFrame->getCvFrame();

        double timestamp = std::chrono::duration_cast<std::chrono::duration<double>>(
            std::chrono::steady_clock::now().time_since_epoch()).count();

        SLAM.TrackStereo(left, right, timestamp);

        if(cv::waitKey(1) == 27) break;
    }

    SLAM.Shutdown();
    SLAM.SaveTrajectoryEuRoC("LiveCameraTrajectory.txt");

    return 0;
}
