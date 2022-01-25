# 数据库编程

## 1.SQLite3数据库

#### 1.创建数据库

```python
import sqlite3

#1.硬盘上创建连接
con = sqlite3.connect('sqlite3_first.db')

#2.获取游标对象
cur = con.cursor()

#3.执行sql创建表
sql = '''
CREATE TABLE t_login(
    pno INTEGER PRIMARY KEY AUTOINCREMENT, 
    pname VARCHAR(30) NOT NULL,
    timeStamp Date DEFAULT CURRENT_TIME)
'''

try:
    cur.execute(sql)
except BaseException as e:
    print(e)
    print("Create failed")
finally:
    #关闭游标
    cur.close()
    #关闭连接
    con.close()

```

- SQL语句

```sql
//创建 表 表名（
列名    类型 设置主键，
列名    类型 非空，
列名    类型 默认当前时间戳，
）
CREATE TABLE t_login(
pno INTEGER PRIMARY KEY AUTOINCREMENT, 
pname VARCHAR(30) NOT NULL,
timeStamp Date DEFAULT CURRENT_TIME)
```

emmm有点多，布鞋了，希望大家悟性好点，看懂上面满不错了。

#### 2.插入数据

```python
import sqlite3

con = sqlite3.connect('sqlite3_first.db')
cur = con.cursor()

sql = 'INSERT INTO t_login(pname) values(?)'

try:
    #插入一条
    cur.execute(sql,['JerryGu'])
    #插入多条          
    cur.executemany(sql,[['JerryGu'],['JerryGu']])
    #提交修改
    con.commit()
    print("commit success!")
except BaseException as e:
    print(e)
    print("commit failed")
    con.rollback()
finally:
    cur.close()
    con.close()
```

- SQL语句

```sql
//插入 表名（列名2，列名5）
//值（列名2值，列名5值）
INSERT INTO t_login(pname) 
values(?)
```

#### 3.删除数据

```python
import sqlite3

con = sqlite3.connect('sqlite3_first.db')
cur = con.cursor()

try:
    sql = '''
    DELETE FROM t_login
    WHERE pno = ?
    '''
    cur.execute(sql,(1,))
    #提交修改
    con.commit()
    print("delete success")
except BaseException as e:
    print(e)
    print("delete failed")
    con.rollback()
finally:
    cur.close()
    con.close()
```

- SQL语句
```sql
//删除 表名
//主键值为？的那一行
 DELETE FROM t_login
WHERE pno = ?
```

#### 4.查询数据

```python
import sqlite3

con = sqlite3.connect('sqlite3_first.db')
cur = con.cursor()

sql = 'SELECT * FROM t_login'
try:
    cur.execute(sql)
    log = cur.fetchall()
    for p in log:
        print(p)
except BaseException as e:
    print(e)
    print("check failed")
    con.rollback()
finally:
    cur.close()
    con.close()

```
- SQL语句
```sql
//选择 列名（*表示全部）[，列名]
//从 表名 
 SELECT * 
 FROM t_login
```

#### 5.修改数据

```python
import sqlite3

con = sqlite3.connect('sqlite3_first.db')
cur = con.cursor()

try:
    sql = '''
    UPDATE t_login
    SET pname = ?
    WHERE pno = ?
    '''
    cur.execute(sql,('JW', 2))
    con.commit()
    print("change success")
except BaseException as e:
    print(e)
    print("change failed")
    con.rollback()
finally:
    cur.close()
    con.close()
```
- SQL语句
```sql
//更新 表名
//修改 列2值为？
//在   列1值为？的行
UPDATE t_login
SET pname = ?
WHERE pno = ?
```

## 2.Mysql数据库
布鞋了布鞋了，用上面的就好了。