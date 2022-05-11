# Python Quick Start

## 1.四则运算

```python
print (2+1)
print (2-1)
print (2*1)
print (2/1)  
print (2//1)
```

## 2.变量

- 不能以数字开头，但能以数字结尾
- 区分大小写

```python
box_width = 3
box_height = 4
box_s = width * height 
print(s)
```

## 3.if语句

### if-else

```python
age = 16
if age > 18:
    print("禁止观看")
else age:
    print("可以观看")
```

### if-elif-else

```python
socre = 80
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 60:
    print('C')
else:
    print('E')
```

## 4.for循环

从0到4

```python
for i in range(5):
    print(i)
```

输出：

```
0
1
2
3
4
```

---

从2到4

```python
for i in range(2,5):
    print(i)
```

输出：

```
2
3
4
```

---

从1到4，步长为2

```python
for i in range(1,5,2):
    print(i)
```

输出：

```
1
3
```

#### for循环嵌套

打印九九乘法表

```python
#python >= 3.6
for i in range(1,10):
    for j in range(1, i + 1):
        print(f'{j}*{i}={j*i}',end = ' ')
    print()             #print()表示换行
```

## 5.while循环

```python
n = 1
while n < 10 :
    print(n)
    n += 1
else :
    print("循环结束！")
```

#### while循环嵌套

打印九九乘法表

```python
n = 1
while n <= 9:
    m = 1
    while m <= n:
        print(f'{m}*{n}={m*n}', end =' ')
        m += 1
    n += 1
    print()
```

## 6.break

```python
while(1):
    s = input('输入：（0） 来退出')
    if s == "0" :
        break
    else : print("你输入的是：",s)
```

## 7.continue

```python
for s in 'python':
    if s == 't' or s == 'h' or s == 'o' or s == 'n':
        continue
    else :
        print(s,end = '')
for n in ['g','T','r','a','d','e']:
    if n == 'g':
        continue
    else :
        print(n, end = '')
```

Guess what id output?

## Gap game

Ues

```python
import ramdon
```

to import ramdom moduel
Example:

```python
import random
target = random.randint(1,100)
```

Ok,now you can write a game- Guess a number.
1Z!
By the way,what you input in the `input` function is a string variable.

## 8.字符串

你可能注意到了在上述笔记中print()函数中使用到 `“”`和 `''`，因为它们并无什么区别，那么为什么这样呢？

```python
s1 = 'We all know that \'A\' and \'B\' are two capital letters.'
s2 = "We all know that 'A' and 'B' are two capital letters."
```

懂？

### 转义

C++学过了，布鞋了。

### 字符串的索引

见笔记第七条。

```python
s = 'JW真帅'
for i in range(4):
      print(s[i],end="")
```

输出：

```
JW真帅
```

### 字符串的切片

字符串s[开始:结束:歩长]

```python
s = 'GJAWA真A帅A'
print(s[1:8:2])
```

输出：

```
JW真帅
```

### 格式化输出

```python
name1 = 'GJW'
name2 = 'ZH'
print('{}对{}说:"Don\'t leave me!"'.format(name2,name1))
```

输出：

```
ZH对GJW说:"Don't leave me!"
```

```python
name1 = 'GJW'
name2 = 'ZH'
print(f'{name1}对{name2}说:"Don\'t leave me!"')
```

### 拼接字符串

```python
print("Are " + 'you ' + 'OK?')
```

## 9.列表[]

```python
my_list = [1, 'J' , '真']
my_list.append('帅')
my_list.insert(2,'W')
print(my_list)
my_list.extend([12,23])
my_list.extend("walawala")
print(my_list)
my_list.pop(0)          #移除第几个元素
my_list.remove("a")     #移除第一个匹配项
print(my_list)
print(my_list[0:4])
```

输出:

```
[1, 'J', 'W', '真', '帅']
[1, 'J', 'W', '真', '帅', 12, 23, 'w', 'a', 'l', 'a', 'w', 'a', 'l', 'a']
['J', 'W', '真', '帅', 12, 23, 'w', 'l', 'a', 'w', 'a', 'l', 'a']
['J', 'W', '真', '帅']
```

## 10.元组 ()

不可变的列表，与列表差不多，（）表示.

## 11.字典{}

```python
user = {
    'name' : 'GJW',
    'gender' : 'male',
    'beloved' : 'ZH'
}
user['beloved'] = 'None'
user['fav'] = 'CSGO'    #增加新的键
print(user['beloved'])
print(user)
```

输出:

```
None
{'name': 'GJW', 'gender': 'male', 'beloved': 'None', 'fav': 'CSGO'}
```

## 12.函数

```python
def sum_between(n, m):
    s = 0
    while n <= m:
        s += n
        n += 1
    return s

print(sum_between(14,80))
```

## 13.文件操作

#### 读取

```python
f = open('pythonRead.txt',encoding='utf-8')
s = f.read()
print(s)
f.close()
```

#### 写入

```python
f = open('pythonWrite.txt', mode = 'write, encoding = 'utf-8')
f.write('帘外蝉声急，\n')
f.write('长鸣噪人心。')
f.close()
```

## 14.第三方库安装

Install libraries in terminal

```shell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple    #设置清华源提提速
pip install opencv-python   #以安装python版opencv为例
```

## 15.类和对象

python也是一个面向对象的编程语言

```python
class Person:
    def __init__(self, name, sex, beloved):
        self.name = name
        self.sex = sex
        self.beloved = beloved
  
    def say(self, word):
        print(f'{self.name}说："{word}"')

GJW = Person('GJW', 'male', 'ZH')  	#实例化一个对象

GJW.say('Forget her.')			#调用该对象的函数
```
