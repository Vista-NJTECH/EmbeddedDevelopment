## 总结
OpenCV非常强大，你还有很多很多的算法需要学习，本章的内容只是提供了一个简单地参考，你应该独立的学会如何掌握一个函数的用法。

本章的一开始，我们学习了绘图函数，我们可以用它来打印文字、绘制形状。然后我们学习了图像滤镜，了解了腐蚀、膨胀、形态滤镜，尝试了简单的边缘检测算法。最后我们介绍了几何变换，引用了色彩表，你应该学会在网络上、在官方文档中寻找你需要的相关信息。

## Have A Try！
3.1.创建一个带有轨迹条的窗口，可改变medianBlur函数的ksize值。ksize取值范围为3～99。

3.2.使用cvtColor函数把彩色图像转换为灰度图，把最暗的100个灰度色阶用threshold函数过滤掉。并将过滤掉的像素在结果图像中设置为白色，其余像素设置为黑色。