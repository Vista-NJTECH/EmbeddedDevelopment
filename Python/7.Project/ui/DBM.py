from cmath import log
import sqlite3
import sys

db_dir = sys.path[0] + '/login.db'
print(db_dir)
#print(db_dir)
class loginDB():
    def __init__(self) -> None:
        pass
    def createDB(self):
        con = sqlite3.connect(db_dir)
        cur = con.cursor()
        sql = '''
        CREATE TABLE t_login(                               
            p_no INTEGER PRIMARY KEY AUTOINCREMENT, 
            p_account VARCHAR(30) NOT NULL,
            p_passwd VARCHAR(30) NOT NULL,
            createTimeStamp Date DEFAULT CURRENT_TIME)
        '''
        try:
            cur.execute(sql)
        except BaseException as e:
            print(e)
            print("Create failed")
        finally:
            cur.close()
            con.close()

    def insertDB(self,account, passwd):
        con = sqlite3.connect(db_dir)
        cur = con.cursor()

        sql = '''
        INSERT 
        INTO t_login(p_account, p_passwd) 
        values(?,?)'''
        try:        
            cur.execute(sql,(account, passwd))
            con.commit()
            print("commit success!")
        except BaseException as e:
            print(e)
            print("commit failed")
            con.rollback()
        finally:
            cur.close()
            con.close()

    def deleteDB(self):
        con = sqlite3.connect(db_dir)
        cur = con.cursor()

        try:
            sql = '''
            DELETE FROM t_login
            WHERE pno = ?
            '''
            cur.execute(sql,(1,))
            con.commit()
            print("delete success")
        except BaseException as e:
            print(e)
            print("delete failed")
            con.rollback()
        finally:
            cur.close()
            con.close()

    def checkDB(self, account, passwd):
        con = sqlite3.connect(db_dir)
        cur = con.cursor()
        sql = '''
        SELECT p_passwd 
        FROM t_login
        WHERE p_account = ?
        '''
        try:
            cur.execute(sql,(account,))
            log = cur.fetchall()
            for p in log:
                for q in p:
                    if q == passwd:
                        return 1
                    else:
                        return 0
        except BaseException as e:
            print(e)
            print("check failed")
            con.rollback()
        finally:
            cur.close()
            con.close()

    def getPasswd(self, account):
        con = sqlite3.connect(db_dir)
        cur = con.cursor()
        sql = '''
        SELECT p_passwd 
        FROM t_login
        WHERE p_account = ?
        '''
        try:
            cur.execute(sql,(account,))
            log = cur.fetchall()
            for p in log:
                return p[0]
        except BaseException as e:
            print(e)
            print("check failed")
            con.rollback()
        finally:
            cur.close()
            con.close()

    def getAllData(self):
        con = sqlite3.connect(db_dir)
        cur = con.cursor()
        sql = '''
        SELECT * 
        FROM t_login
        '''
        try:
            cur.execute(sql)
            log = cur.fetchall()
            return log
        except BaseException as e:
            print(e)
            print("check failed")
            con.rollback()
        finally:
            cur.close()
            con.close()

    def updateDB(self):
        con = sqlite3.connect(db_dir)
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

#a = loginDB()
#a.createDB()