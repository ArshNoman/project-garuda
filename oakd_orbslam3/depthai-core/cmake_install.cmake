# Install script for directory: /home/parallels/Desktop/projects/project-garuda/oakd_orbslam3/depthai-core

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Debug")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/home/parallels/Desktop/projects/project-garuda/oakd_orbslam3/depthai-core/libdepthai-core.a")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib" TYPE STATIC_LIBRARY FILES "/home/parallels/Desktop/projects/project-garuda/oakd_orbslam3/depthai-core/libdepthai-resources.a")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/parallels/Desktop/projects/project-garuda/oakd_orbslam3/depthai-core/include/")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/parallels/Desktop/projects/project-garuda/oakd_orbslam3/depthai-core/shared/depthai-shared/include/")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/depthai-shared/3rdparty" TYPE DIRECTORY FILES "/home/parallels/Desktop/projects/project-garuda/oakd_orbslam3/depthai-core/shared/depthai-shared/3rdparty/")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include" TYPE DIRECTORY FILES "/home/parallels/Desktop/projects/project-garuda/oakd_orbslam3/depthai-core/shared/depthai-bootloader-shared/include/")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/depthai/3rdparty" TYPE FILE FILES
    "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/XLink.h"
    "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/XLinkDispatcher.h"
    "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/XLinkDispatcherImpl.h"
    "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/XLinkErrorUtils.h"
    "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/XLinkLog.h"
    "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/XLinkMacros.h"
    "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/XLinkPlatform.h"
    "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/XLinkPlatformErrorUtils.h"
    "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/XLinkPrivateDefines.h"
    "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/XLinkPrivateFields.h"
    "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/XLinkPublicDefines.h"
    "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/XLinkStream.h"
    "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/XLinkStringUtils.h"
    "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/XLinkVersion.h"
    )
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/include/depthai/3rdparty/nlohmann" TYPE FILE FILES "/home/parallels/.hunter/_Base/062a19a/e017bc9/a65fa5a/Install/include/nlohmann/json.hpp")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  if(EXISTS "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/depthai-core/depthai-coreConfig.cmake")
    file(DIFFERENT _cmake_export_file_changed FILES
         "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/depthai-core/depthai-coreConfig.cmake"
         "/home/parallels/Desktop/projects/project-garuda/oakd_orbslam3/depthai-core/CMakeFiles/Export/05e87582f2b81a05d7cf0aef7c1a61ba/depthai-coreConfig.cmake")
    if(_cmake_export_file_changed)
      file(GLOB _cmake_old_config_files "$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/depthai-core/depthai-coreConfig-*.cmake")
      if(_cmake_old_config_files)
        string(REPLACE ";" ", " _cmake_old_config_files_text "${_cmake_old_config_files}")
        message(STATUS "Old export file \"$ENV{DESTDIR}${CMAKE_INSTALL_PREFIX}/lib/cmake/depthai-core/depthai-coreConfig.cmake\" will be replaced.  Removing files [${_cmake_old_config_files_text}].")
        unset(_cmake_old_config_files_text)
        file(REMOVE ${_cmake_old_config_files})
      endif()
      unset(_cmake_old_config_files)
    endif()
    unset(_cmake_export_file_changed)
  endif()
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/depthai-core" TYPE FILE FILES "/home/parallels/Desktop/projects/project-garuda/oakd_orbslam3/depthai-core/CMakeFiles/Export/05e87582f2b81a05d7cf0aef7c1a61ba/depthai-coreConfig.cmake")
  if(CMAKE_INSTALL_CONFIG_NAME MATCHES "^([Dd][Ee][Bb][Uu][Gg])$")
    file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/cmake/depthai-core" TYPE FILE FILES "/home/parallels/Desktop/projects/project-garuda/oakd_orbslam3/depthai-core/CMakeFiles/Export/05e87582f2b81a05d7cf0aef7c1a61ba/depthai-coreConfig-debug.cmake")
  endif()
endif()

