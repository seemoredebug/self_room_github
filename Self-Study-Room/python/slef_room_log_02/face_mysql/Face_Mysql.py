import re

import numpy as np
import pymysql

class Face_Mysql():
    def in_mysql(self,score,picdata):
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='test')
        cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
        picdata=self.picdata_tostr(picdata)
        insql = "INSERT INTO pypic(score,picData) VALUES ('" + score + "','" + picdata + "')"
        cursor.execute(insql)
        db.commit()
        db.close()

    def out_mysql(self):
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='test')
        cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
        selectsql = "SELECT * FROM `pypic`"
        cursor.execute(selectsql)
        data = cursor.fetchall()
        label=[]
        picdata=[]
        for i in data:
            label.append(i[0])
            picdata.append(np.array(self.picdata_tolist(i[1])))
        db.close()
        return label,picdata

    def picdata_tolist(self,data):
        numbers = re.findall(r"\-?\d+\.\d*", data)
        new_numbers = []
        for n in numbers:
            new_numbers.append(float(n));
            # aaaa = []
            # aaaa.append(new_numbers)
        return new_numbers

    def picdata_tostr(self,data):
        str = ''.join('%s ' % id for id in data)
        return str