#include <iostream>
#include <string>
#include <sstream>
using namespace std;

#include "opencv2/core/core.hpp"
#include "opencv2/highgui/highgui.hpp"
using namespace cv;

int main(int,char** argv)
{
    FileStorage fs("test.yml",FileStorage::WRITE);
    int fps=5;
    fs<<"fps"<<fps;

    Mat m1=Mat::eye(2,3,CV_32F);
    Mat m2=Mat::ones(3,2,CV_32F);
    Mat result=(m1+1).mul(m1+3);

    fs<<"Result"<<result;
    fs.release();

    FileStorage fs2("test.yml",FileStorage::READ);

    Mat r;
    fs2["Result"]>>r;
    std::cout <<r<<std::endl;

    fs2.release();

    return 0;

}