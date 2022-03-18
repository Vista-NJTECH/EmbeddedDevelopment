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
    VideoCapture capture;
    capture.open("../sample.avi");

    while(true)
    {
        Mat frame;
        capture>>frame;
       
        if (frame.empty())
        {
            cout << "**** ****"<<endl;
            cout << "播放结束"<<endl;
            cout <<endl;
            cout << "**** ****"<<endl;
            break;
        }
         imshow("读取视频",frame);
        waitKey(30);
    }
    capture.release();
}