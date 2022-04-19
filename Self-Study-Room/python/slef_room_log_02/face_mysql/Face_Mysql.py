import datetime
import time
import re

import numpy as np
import pymysql

class Face_Mysql():
    def in_mysql(self,score,picdata):
        db = pymysql.connect(host='106.14.32.207',
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
        db = pymysql.connect(host='106.14.32.207',
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

    def find_(self,stu):
        curr_time = datetime.datetime.now()
        timestamphour = curr_time.hour
        data=curr_time.year
        datano=str(data)
        if(curr_time.month<10):
            datano+="0"
        datano+=str(curr_time.month)
        if (curr_time.day< 10):
            datano += "0"
        datano += str(curr_time.day)


        if(timestamphour<8 or timestamphour>21):
            return False
        elif(timestamphour==8):
            datano += "01"
        elif(timestamphour==9):
            datano += "02"
        elif(timestamphour==10):
            datano += "03"
        elif(timestamphour==11):
            datano += "04"
        elif(timestamphour==12):
            datano += "05"
        elif(timestamphour==14):
            datano += "06"
        elif(timestamphour==15):
            datano += "07"
        elif(timestamphour==16):
            datano += "08"
        elif(timestamphour==17):
            datano += "09"
        elif(timestamphour==18):
            datano += "10"
        elif (timestamphour==19):
            datano += "11"
        sql1="select * from `reserveinformation` where score="+stu+" and seatNumber like '301%' and timequantum='"+datano+"'"

        db = pymysql.connect(host='106.14.32.207',
                             user='root',
                             password='123456',
                             database='test')
        cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
        cursor.execute(sql1)
        data = cursor.fetchall()
        db.close()
        if(data):
            return True
        else:
            return False