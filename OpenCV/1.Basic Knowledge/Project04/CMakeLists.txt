cmake_minimum_required(VERSION 3.0)
project(PROJECT04)
#Requires OpenCV（找包）
    FIND_PACKAGE(OpenCV REQUIRED)
#Show a message with the opencv version detected
    MESSAGE("OpenCV version : ${OpenCV_VERSION}")
#Add the paths to the include directories/to the header files（包含相关头文件的目录）
    include_directories(${OpenCV_INCLUDE_DIRS})
#Add the paths to the compiled libraries/objects（指定第三方库的路径）
    link_directories(${OpenCV_LIB_DIR})
#Create a variable called SRC
    SET(SRC "project04.cpp")
#Create our executable
    ADD_EXECUTABLE( PROJECT04 ${SRC} )
#Link our library    
    TARGET_LINK_LIBRARIES( PROJECT04 ${OpenCV_LIBS})