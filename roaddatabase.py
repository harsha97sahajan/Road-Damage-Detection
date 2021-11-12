import pymysql
def select(qry,values):
    con=pymysql.connect(host="localhost", port=3306,user="root", password="Root_root1",db='road')
    cmd=con.cursor()
    cmd.execute(qry,values)
    res=cmd.fetchone()
    con.close()
    return res
def insert(qry,values):
    con = pymysql.connect(host="localhost", port=3306, user="root", password="Root_root1", db='road')
    cmd = con.cursor()
    cmd.execute(qry,values)
    id=cmd.lastrowid
    con.commit()
    con.close()
    return id
def selectall(qry):
    con=pymysql.connect(host="localhost",port=3306, user="root", password="Root_root1",db='road')
    cmd = con.cursor()
    cmd.execute(qry)
    res=cmd.fetchall()
    con.close()
    return res
