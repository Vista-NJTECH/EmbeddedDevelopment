# FileIO
Python中一切都是对象
利用 `open()` 来创建文件对象
```
open('文件名' [,打开方式])
```
|模式|描述|
|---|---|
|r|读取|
|w|覆盖性写入|
|a|追加性写入|
|b|二进制|
|+|读写|

## 1.编码介绍
- ASCII
  - ISO8859-1
    - UTF-8
    - GB2312
      - GBK
      - GB18030
  - Unicode

向下兼容

## 2.二进制文件读写
图片文件拷贝
```python
with open('copyFrom.jpg', 'rb') as f:
    with open('copyTo.jpg', 'wb') as g:
        for line in f.readlines():
            w.write(line)
```

## 3.文件指针
#### seek(offset [,whence])
```
offset - 往正方向移动的偏移量

whence - 0:文件头开始
         1：当前位置开始
         2：文件尾开始
```
Example:
```python
with open('test.txt', 'r',encoding = 'utf-8') as f:
  print("文件名是{0}".format(f.name))
```
#### tell
```python
with open('./test.txt', 'r',encoding = 'utf-8') as f:
  print("文件名是{0}".format(f.name))
  print(f.tell())
  f.seek(15,0)
  print(f.tell())
```