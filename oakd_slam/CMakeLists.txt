cmake_minimum_required(VERSION 3.10)
project(oakd_stereo_live)

set(CMAKE_CXX_STANDARD 14)

find_package(OpenCV REQUIRED)
find_package(Pangolin REQUIRED)

# === Include directories ===
include_directories(
    ${PROJECT_SOURCE_DIR}/../ThirdParty/depthai-bootloader-shared/include
    ${PROJECT_SOURCE_DIR}/../ThirdParty/depthai-core/include
    ${PROJECT_SOURCE_DIR}/../ThirdParty/libnop/include
    ${PROJECT_SOURCE_DIR}/../ThirdParty/XLink/include
    ${PROJECT_SOURCE_DIR}/../ThirdParty/eigen3
    ${PROJECT_SOURCE_DIR}/../ThirdParty

    ${PROJECT_SOURCE_DIR}/../ThirdParty/ORB-SLAM3/include/CameraModels
    ${PROJECT_SOURCE_DIR}/../ThirdParty/ORB-SLAM3/Thirdparty/Sophus
    ${PROJECT_SOURCE_DIR}/../ThirdParty/ORB-SLAM3/Thirdparty/DBoW2
    ${PROJECT_SOURCE_DIR}/../ThirdParty/ORB-SLAM3/Thirdparty/g2o
    ${PROJECT_SOURCE_DIR}/../ThirdParty/ORB-SLAM3/Thirdparty
    ${PROJECT_SOURCE_DIR}/../ThirdParty/ORB-SLAM3/include
    ${PROJECT_SOURCE_DIR}/../ThirdParty/ORB-SLAM3

    ${OpenCV_INCLUDE_DIRS}
)


add_executable(oakd_stereo_live oakd_stereo_live.cpp)
target_link_libraries(oakd_stereo_live
    ${OpenCV_LIBS}
    ${Pangolin_LIBRARIES}
    ${PROJECT_SOURCE_DIR}/../ThirdParty/ORB-SLAM3/lib/libORB_SLAM3.so
)