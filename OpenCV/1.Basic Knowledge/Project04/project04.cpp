#include <iostream>
#include <string>
#include <sstream>
using namespace std;

#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
using namespace cv;
    
    int main()
    {
    // 1.create our writter
	FileStorage fs("test.yml", FileStorage::WRITE);
	
	// 2.Save an int
	int imageWidth= 5;
	int imageHeight= 10;
	fs << "imageWidth" << imageWidth;
	fs << "imageHeight" << imageHeight;
 
	// 3.Write a Mat
	cv::Mat m1= Mat::eye(3,3, CV_8U);
	cv::Mat m2= Mat::ones(3,3, CV_8U);
	cv::Mat resultMat= (m1+1).mul(m1+2);
	fs << "resultMat" << resultMat;
 
	// 4.Write multi-variables 
	cv::Mat cameraMatrix = (Mat_<double>(3,3) << 1000, 0, 320, 0, 1000, 240, 0, 0, 1);
    cv::Mat distCoeffs = (Mat_<double>(5,1) << 0.1, 0.01, -0.001, 0, 0);
    fs << "cameraMatrix" << cameraMatrix << "distCoeffs" << distCoeffs;
 
	// 5.Save local time
	time_t rawtime; time(&rawtime); //#include <time.h>
	fs << "calibrationDate" << asctime(localtime(&rawtime));
 
	// 6.close the file opened
	fs.release();
    }