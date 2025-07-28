/**
 * @file util.cpp
 * @author Duncan Hamill (duncanrhamill@googlemail.com)
 * @brief General utilities for the experiments.
 * @version 0.1
 * @date 2021-01-13
 * 
 * @copyright Copyright (c) Duncan Hamill 2021
 */

/* -------------------------------------------------------------------------
 * INCLUDES
 * ------------------------------------------------------------------------- */

#include <opencv2/opencv.hpp>

#include "depthai/depthai.hpp"
#include <opencv2/opencv.hpp>
#include <vector>

/* -------------------------------------------------------------------------
 * FUNCTIONS
 * ------------------------------------------------------------------------- */

cv::Mat imgframe_to_mat(std::shared_ptr<dai::ImgFrame> frame, int = CV_8UC1) {
    std::vector<uint8_t> data = frame->getData();
    cv::Mat encoded(data);
    cv::Mat decoded = cv::imdecode(encoded, cv::IMREAD_GRAYSCALE);
    return decoded;
}



