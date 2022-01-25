# Exception

异常本质：程序中可能出现的错误情况

- 用户输入错误
- 除数为0
- 文件不存在
- 下标越界

## 异常类

Python中一切都是对象，包括异常
Python定义了异常类

* BaseException
  - KeyBoardInterrupt
  - Exception
    * NameError
    * ValueErroe
    * AttributerError
    * ......
  - SystemExit
  - GeneratorExit

## 1.try-except

```python
try:
    可能异常的语句块
except BaseException as e:
    异常处理语句块
```

Example1:

```python
try:
    print("step1")
    a = 3/0
    print("step2")
except BaseException as e:
    print("step3")
    print(e)
```

输出：

```
step1
step3
division by zero
```

Example2:

```python
try:
   num1 = input("输入一个被除数： ")
   num2 = input("输入一个除数： ")
   c = float(num1)/float(num2)
   print(c)
except ZeroDivisionError:
    print("不能除以0")
except ValueError:
    print("未将字符串转化为数字")
except NameError:
    print("变量不存在")
```

## 2.try-except-else

```python
try:
    可能异常的语句块
except BaseException as e:
    异常处理语句块
else:
    无异常语句块
```

## 3.try-except-else-finally

```python
try:
    可能异常的语句块
except BaseException as e:
    异常处理语句块
else:
    无异常语句块
finally:
    都执行
```

## 4.常见异常

| 类型           | 原因           |
| -------------- | -------------- |
| SyntaxError    | 语法错误       |
| AttributeError | 对象不存在属性 |
| IndexError     | 数组越界       |

## 5.with上下文管理

with内的代码执行完，整个with会关闭，此语句常用
因此不必考虑异常

```python
with open('../Basics/pythonRead.txt',encoding = 'utf-8') as f:
    for line in f:
        print(line)
```
