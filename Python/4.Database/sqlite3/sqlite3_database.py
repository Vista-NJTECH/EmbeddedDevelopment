import sqlite3

#########################################################
#                       创建数据库                        #
#########################################################
def createDB():
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
        cur.close()
        con.close()


#########################################################
#                       添加数据                         #
#########################################################
def insertDB():
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


#########################################################
#                       删除数据                         #
#########################################################
def deleteDB():
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


#########################################################
#                       查询数据                         #
#########################################################
def checkDB():
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


#########################################################
#                       修改数据                         #
#########################################################
def updateDB():
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

checkDB()
deleteDB()
updateDB()
checkDB()