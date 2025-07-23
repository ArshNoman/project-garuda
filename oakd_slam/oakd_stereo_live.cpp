#include "System.h"
#include <opencv2/core/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <iostream>
#include <unistd.h>
#include <opencv2/core/persistence.hpp>

int main(int argc, char **argv) {
    if(argc != 4) {
        std::cerr << "Usage: ./test_stereo_single_frame path_to_vocabulary path_to_settings left_right_folder" << std::endl;
        return 1;
    }

    std::string vocabPath = argv[1];
    std::string settingsPath = argv[2];
    std::string imageDir = argv[3];

    cv::FileStorage fs(settingsPath, cv::FileStorage::READ);
    if (!fs.isOpened()) {
        std::cerr << "Failed to open settings file: " << settingsPath << std::endl;
        return 1;
    }
    std::cout << "YAML file opened successfully." << std::endl;

    int sensor_type = (int)fs["Camera.Sensor"];
    std::cout << "Camera.Sensor read from YAML: " << sensor_type << std::endl;

    if (sensor_type != 1) {
        std::cerr << "❌ Invalid Camera.Sensor value. It must be 1 for Stereo." << std::endl;
    }

    ORB_SLAM3::System SLAM(vocabPath, settingsPath, ORB_SLAM3::System::STEREO, true);

    cv::Mat imLeft = cv::imread("/home/parallels/Desktop/projects/project-garuda/oakd_slam/left.png", cv::IMREAD_UNCHANGED);
    cv::Mat imRight = cv::imread("/home/parallels/Desktop/projects/project-garuda/oakd_slam/right.png", cv::IMREAD_UNCHANGED);

    if(imLeft.empty() || imRight.empty()) {
        std::cerr << "Error loading stereo images" << std::endl;
        return 1;
    }

    SLAM.TrackStereo(imLeft, imRight, 0.0);
    sleep(2);  // Let the viewer show the result

    SLAM.Shutdown();
    return 0;
}
