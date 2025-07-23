cmake_minimum_required(VERSION 3.14)
project(oakd_slam)

set(CMAKE_CXX_STANDARD 17)

# === Find required packages ===
find_package(OpenCV REQUIRED)
find_package(Threads REQUIRED)

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

# === Source files ===
file(GLOB_RECURSE SRC_FILES src/*.cpp)

# === Build executable ===
add_executable(oakd_stereo_live ${SRC_FILES})

find_package(PkgConfig REQUIRED)
pkg_check_modules(LIBUSB REQUIRED libusb-1.0)

include_directories(${LIBUSB_INCLUDE_DIRS})
target_link_libraries(oakd_stereo_live ${LIBUSB_LIBRARIES})


link_directories(
    ${PROJECT_SOURCE_DIR}/../ThirdParty/ORB-SLAM3/lib
)

# === Link libraries ===
target_link_libraries(oakd_stereo_live
    ORB_SLAM3
    ${OpenCV_LIBS}
    Threads::Threads
    usb-1.0
)
