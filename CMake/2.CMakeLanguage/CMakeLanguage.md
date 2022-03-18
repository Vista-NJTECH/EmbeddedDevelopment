# 语句
### CMAKE_MINIMUN_REQUIRED
指出CMake所支持的最小版本
```cmake
CMAKE_MINIMUN_REQUIRED(VERSION 2.8.3)
```
### PROJECT
PROJECT (工程名字 [ 支持语言 ])  默认支持所有语言


```cmake
PROJECT (HELLO)

PROJECT (HELLO CXX)

PROJECT (HELLO C CXX)
```

### SET
将cpp，hpp等文件包含在变量`SRC_LIST`中，方便操作。
```cmake
SET(SRC_LIST main.cpp others.cpp)
```

### INCLUDE_DIRECTORIES
向工程添加多个特定的头文件搜索路径 --->相当于指定g++编译器的-I参数
```cmake
INCLUDE_DIRECTORIES(/usr/include/myincludefolder ./include)
```

### LINK_DREICTORIES
向工程添加多个特定的库文件搜索路径 --->相当于指定g++编译器的-L参数
```cmake
LINK_DREICTORIES(/usr/lib/mylibfolder ./lib)
```

### ADD_LIBRARY
生成库文件
```cmake
# 通过变量 SRC_LIST 生成 libhello.so 共享库
add_library(hello SHARED ${SRC_LIST})
```

### Message
可输出错误信息，具体不写了，我也不用。
```cmake
MESSAGE(STSTUS "THIS IS BINARY DIR" ${HELLO_BINARY_DIR})
MESSAGE(STATUS "THIS IS SOURCE DIR" ${HELLO_SOURCE_DIR})
```
### ADD_EXECUTABLE
生成可执行文件
```cmake
ADD_EXECUTABLE(可执行文件名 ${SRC_LIST})
```

### TARGET_LINK_LIBRARIES
为 TARGET 添加需要链接的共享库
```cmake
#将hello动态库文件链接到可执行文件main
TARGET_LINK_LIBRARIES(main hello)
```
# 语法基本原则
- 指令不区分大小写，推荐全大写。
- 参数间可用空格
- 参数含空格要添加“ ”

#内部/外部构建
### example1为内部构建
生成许多临时文件，不方便看
### example2为外部构建
一般编译方式
新建build，进入build
```shell
mkdir build && cd build
cmake ..
```
