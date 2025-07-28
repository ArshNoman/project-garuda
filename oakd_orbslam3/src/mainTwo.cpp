#include <iostream>
#include "depthai/depthai.hpp"
#include <thread>
#include <chrono>

int main() {
    std::cout << "Minimal Oak-D Stereo Test (safe metadata only)" << std::endl;

    dai::Pipeline pipeline;

    auto monoLeft = pipeline.create<dai::node::MonoCamera>();
    monoLeft->setResolution(dai::MonoCameraProperties::SensorResolution::THE_400_P);
    monoLeft->setBoardSocket(dai::CameraBoardSocket::LEFT);
    monoLeft->setFps(20);

    auto monoRight = pipeline.create<dai::node::MonoCamera>();
    monoRight->setResolution(dai::MonoCameraProperties::SensorResolution::THE_400_P);
    monoRight->setBoardSocket(dai::CameraBoardSocket::RIGHT);
    monoRight->setFps(20);

    auto stereo = pipeline.create<dai::node::StereoDepth>();
    stereo->setOutputRectified(true);
    stereo->setRectifyMirrorFrame(false);
    stereo->setOutputDepth(false);

    monoLeft->out.link(stereo->left);
    monoRight->out.link(stereo->right);

    auto xoutLeft = pipeline.create<dai::node::XLinkOut>();
    xoutLeft->setStreamName("left");
    stereo->rectifiedLeft.link(xoutLeft->input);

    auto xoutRight = pipeline.create<dai::node::XLinkOut>();
    xoutRight->setStreamName("right");
    stereo->rectifiedRight.link(xoutRight->input);

    std::cout << "Pipeline created. Connecting to device..." << std::endl;

    dai::Device device(pipeline);

    std::cout << "Pipeline started. Waiting for frames..." << std::endl;

    auto leftQ = device.getOutputQueue("left", 4, false);
    auto rightQ = device.getOutputQueue("right", 4, false);

    while (true) {
        auto leftFrame = leftQ->get<dai::ImgFrame>();
        auto rightFrame = rightQ->get<dai::ImgFrame>();

        if (!leftFrame || !rightFrame) {
            std::cerr << "no flipping frames" << std::endl;
            continue;
        }

        std::cout << "Left: " << leftFrame->getWidth() << "x" << leftFrame->getHeight() << std::endl;
        std::cout << "Right: " << rightFrame->getWidth() << "x" << rightFrame->getHeight() << std::endl;

        std::this_thread::sleep_for(std::chrono::milliseconds(200));
    }

    return 0;
}