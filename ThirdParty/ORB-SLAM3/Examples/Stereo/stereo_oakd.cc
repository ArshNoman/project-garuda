#include <iostream>
#include <chrono>
#include <opencv2/opencv.hpp>
#include <System.h>
#include <depthai/depthai.hpp>

using namespace std;

int main(int argc, char **argv) {
    if (argc != 3) {
        cerr << endl << "Usage: ./stereo_oakd path_to_vocabulary path_to_settings" << endl;
        return 1;
    }

    // Load SLAM system
    ORB_SLAM3::System SLAM(argv[1], argv[2], ORB_SLAM3::System::STEREO, true);

    // Create Oak-D pipeline
    dai::Pipeline pipeline;

    // Stereo camera nodes
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

    // Start device
    dai::Device device(pipeline);
    auto qLeft = device.getOutputQueue("left", 8, false);
    auto qRight = device.getOutputQueue("right", 8, false);
