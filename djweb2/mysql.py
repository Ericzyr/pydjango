#!/usr/bin/evn python3
# -*-coding:utf-8-*-
import MySQLdb



import pymysql
pymysql.install_as_MySQLdb()
import pymysql

#
# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "new_pass", "pydata")
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# # 使用 execute()  方法执行 SQL 查询
# cursor.execute("SELECT VERSION()")
#
# # 使用 fetchone() 方法获取单条数据.
# data = cursor.fetchone()
#
# print("Database version : %s " % data)
#
# # 关闭数据库连接
# db.close()
#
# conn = pymysql.connect(host='localhost' , port=3306 , user='root' , passwd='root' , db='ecshop' , charset='UTF8')
# cur = conn.cursor()


conn = pymysql.connect(host="localhost", user="root", passwd="new_pass", db="student",charset='UTF8')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = conn.cursor()
# 新增
#   cur.execute("insert into tab1(tab1_id,val) VALUES (3,3)");
# 查询mysql版本  cur.execute("SELECT VERSION()");

# SQL 查询语句
sql = "select * from tb_stu1 "
cursor.execute(sql)
# 获取所有记录列表
results = cursor.fetchall()
print(results)
for row in results:
      # print(row,"：result")
      print('result:', row)
      print('result:', row[1])


print("")

# 获取所有数据库列表

cursor.execute("show databases")
r = cursor.fetchall()
for i in iter(r):
      print(list(i)[0])
# print(r)
#
# cursor.close()
# conn.close()


insert ="INSERT INTO tb_stu1(id,name,sex,birthday) VALUES ( 2,'小小', '女', '2012-11-02')"

cursor.execute(insert)
rtt = cursor.fetchall()
print(rtt)
# for i in iter(r):
#       print(list(i)[0])
# print(r)

cursor.close()
conn.close()