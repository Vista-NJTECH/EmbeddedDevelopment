# Learning GUI
## 在学习本章之前，你需要掌握以下基础知识：  

## 你需要在本章节学会以下内容：
||
|---|
|OpenCV基本用户界面|
|OpenCV GUI界面|
|滑块与按钮|
|高级用户界面：OpenCL|
|颜色转换|
|基本滤波器|

如果上述条件你都满足，那么现在让我们开始吧！

---
## OpenCV用户界面介绍
OpenCV拥有自己的跨操作系统用户界面，提供两种用户界面选项：

    1.基于原生用户界面的基本界面，在编译OpenCV时被默认选择；
    2.基于Qt库的略微更高级的界面，这是跨平台的界面，必须在编译OpenCV之前在CMake中手动启用Qt选项。
## OpenCV的基本图形用户界面
下面我们将使用OpenCV创建和显示两个图像，具体来说，可以在桌面上通过按键来显示多个窗口，并使图像移入这些窗口中。下面我们来看看代码：
```c++
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

//导入highgui模块
#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
using namespace cv;

int main()
{
    //将上级目录中的lena.jpg读入矩阵lena中
    Mat lena=imread("../lena.jpg");

    //有效性检测
    if(!lena.data){
        cout <<"Lena image missing!"<<endl;
        return -1;
    }
    
    //将上级目录中的photo.jpg读入矩阵photo中
    Mat photo =imread("../photo.jpg");

    //有效性检测
    if(!photo.data){
        cout << "Lena image missing!"<<endl;
        return -1;
    }

    //创建窗口使用nameWindow函数，我们在Note中进行详细介绍
    namedWindow("Lena",WINDOW_NORMAL);
    namedWindow("Photo",WINDOW_AUTOSIZE);

    //当创建多个窗口时，它们是叠加的，但我们可以使用moveWindow函数将窗口移动到桌面的任何区域
    //在这里，我们将Lena窗口向左移动了10个像素，向上移动了10个像素
    moveWindow("Lena",10,10);
    moveWindow("Photo",520,10);

    //在窗口中加载lena和photo矩阵
    imshow("Lena",lena);
    imshow("Photo",photo);

    //将Lena窗口大小调整为512像素，详见Note
    resizeWindow("Lena",512,512);

    waitKey(0);

    //删除刚刚的两个窗口
    destroyWindow("Lena");
    destroyWindow("Photo");

    //创建十个窗口
    for(int i=0;i<10;i++)
    {
        ostringstream ss;
        ss<<"Photo"<<1;
        namedWindow(ss.str());
        moveWindow(ss.str(),20*i,20*i);
        imshow(ss.str(),photo);
    }

    waitKey(0);

    //删除这些窗口
    destroyAllWindows();
    return 0;
}
```
Note：  
1.nameWindow函数，第一个参数是带有窗口名称的字符串，第二个参数是我们需要的标志，第二个参数是可选的，有下面几种类型：

    WINDOW_NORMAL：此标志允许用户调整窗口的大小；
    WINDOW_AUTOSIZE：如果设置了此标志，窗口大小为自动调整适应显示图像
    WINDOW_OPENGL：此标志启用OpenGL支持

2.resizeWindow函数，有三个参数：window name、width和height，注意，工具栏不计算在内。  
3.destroyWindow函数删除这个窗口，唯一需要的参数是窗口名称。  

### 将滑块和鼠标时间添加到界面
接下来我们将介绍用于基本交互的鼠标事件和滑块控件。
下面的代码将使用书表示家在图像中绘制绿色圆圈，并使用滑块对图像进行模糊处理：
```c++
#include <iostream>
#include <string>
#include <sstream>
using namespace std;

#include <opencv2/core.hpp>
#include <opencv2/highgui.hpp>
#include "opencv2/imgproc.hpp"
using namespace cv;

//创建一个变量来保存滑块位置，一边从其他函数访问它
int blurAmount=15;

//为滑块和鼠标事件定义回调函数，这是setMouseCallback函数和createTrackbar所必需的
static void onChange(int pos,void* userInput);

static void onMouse(int event,int x,int y,int,void* userInput);

int main(int argc,const char** argv)
{
    //将图片读入矩阵
    Mat lena=imread("../lena.jpg");

    //创建新窗口
    namedWindow("Lena");

    //生成滑块，详细参数见Note
    createTrackbar("Lena","Lena",&blurAmount,30,onChange,&lena);

    //


























    
    setMouseCallback("Lena",onMouse,&lena);


    onChange(blurAmount,&lena);

    waitKey(0);

    destroyWindow("Lena");

    return 0;

}

static void onChange(int pos, void* userInput)
{
	if(pos <= 0)
		return;
	// Aux variable for result
	Mat imgBlur;

	// Get the pointer input image
	Mat* img= (Mat*)userInput;

	// Apply a blur filter
	blur(*img, imgBlur, Size(pos, pos));	

	// Show the result
	imshow("Lena", imgBlur);
}

//Mouse callback
static void onMouse( int event, int x, int y, int, void* userInput )
{
	if( event != EVENT_LBUTTONDOWN )
	        return;

	// Get the pointer input image
	Mat* img= (Mat*)userInput;
	
	// Draw circle
	circle(*img, Point(x, y), 10, Scalar(0,255,0), 3);

	// Call on change to get blurred image
	onChange(blurAmount, img);

}
