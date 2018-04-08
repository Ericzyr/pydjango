#!/usr/bin/evn python3
# -*-coding:utf-8-*-

# import pymysql
# pymysql.install_as_MySQLdb()
import pymysql

# 打开数据库连接
db = pymysql.connect("localhost", "root", "new_pass", "student")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
cursor.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchone()

print("Database version : %s " % data)

# 关闭数据库连接
db.close()

# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "new_pass", "student")
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()

# # SQL 查询语句
# sql = "SELECT * FROM EMPLOYEE \
#        WHERE INCOME > '%d'" % (1000)
# try:
#     # 执行SQL语句
#     cursor.execute(sql)
#     # 获取所有记录列表
#     results = cursor.fetchall()
#     for row in results:
#         fname = row[0]
#         lname = row[1]
#         age = row[2]
#         sex = row[3]
#         income = row[4]
#         # 打印结果
#         print("fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
#               (fname, lname, age, sex, income))
# except:
#     print("Error: unable to fetch data")
#
# # 关闭数据库连接
# db.close()