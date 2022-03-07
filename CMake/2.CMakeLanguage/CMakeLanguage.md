# 语句
### CMAKE_MINIMUN_REQUIRED
指出CMake所支持的最小版本
```
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
```
SET(SRC_LIST main.cpp other.cpp)
```

### Message
可输出错误信息，具体不写了，我也不用。
```
MESSAGE(STSTUS "THIS IS BINARY DIR" ${HELLO_BINARY_DIR})
MESSAGE(STATUS "THIS IS SOURCE DIR" ${HELLO_SOURCE_DIR})
```
### ADD_EXECUTABLE
生成可执行文件
```
ADD_EXECUTABLE(可执行文件名 ${SRC_LIST})
```
# 语法基本原则
- 指令不区分大小写，推荐全大写。
- 参数间可用空格
- 参数含空格要添加“”

#内部/外部构建
### example1为内部构建
生成许多临时文件，不方便看
### example2为外部构建
一般编译方式
新建build，进入build
```
mkdir build && cd build
cmake ..
```
