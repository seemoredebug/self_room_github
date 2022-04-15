import pymysql

# 打开数据库连接
db = pymysql.connect(host='localhost',
                     user='root',
                     password='123456',
                     database='test')

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

cursor = db.cursor()

# SQL 查询语句
sql = "select * from `personal_information`"
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        print(row)
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()