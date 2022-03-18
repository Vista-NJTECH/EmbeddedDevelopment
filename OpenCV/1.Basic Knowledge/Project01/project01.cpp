#include <iostream>
#include <string>
#include <sstream>
using namespace std;

#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
#include "opencv2/imgproc/imgproc.hpp"
using namespace cv;

int main()
{
	//读取视频或摄像头
	VideoCapture capture(0);
	
	while (true)
	{
		Mat frame;
		capture >> frame;
		imshow("读取视频", frame);
		if (waitKey(1) == 27)//按ESC键
            {
                cout << "程序结束！" << endl;
                cout << "*** ***" << endl;
				break;
            }
	}
	return 0;
}
