#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <stdio.h>

using namespace cv;
using namespace std;

int main(int, char**)
{
    Mat src;
    VideoCapture cap(0);
    if (!cap.isOpened()) {
        cerr << "ERROR! Unable to open camera\n";
        return -1;
    }
    cap >> src;
    if (src.empty()) {
        cerr << "ERROR! blank frame grabbed\n";
        return -1;
    }
    bool isColor = (src.type() == CV_8UC3);
    VideoWriter writer;
    int codec = VideoWriter::fourcc('M', 'J', 'P', 'G');
    double fps = 25.0;                        
    string filename = "./live.avi";
    writer.open(filename, codec, fps, src.size(), isColor);
    if (!writer.isOpened()) {
        cerr << "Could not open the output video file for write\n";
        return -1;
    }
    cout << "Writing videofile: " << filename << endl
         << "Press any key to terminate" << endl;
    for (;;)
    {
        if (!cap.read(src)) {
            cerr << "ERROR! blank frame grabbed\n";
            break;
        }
        writer.write(src);
        imshow("Live", src);
        if (waitKey(5) >= 0)
            break;
    }
    return 0;
}