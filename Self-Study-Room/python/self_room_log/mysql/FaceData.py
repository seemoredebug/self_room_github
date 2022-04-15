import pymysql
class FaceData():
    def inFaceData(self,score,picdata):
        db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='123456',
                                  database='test')
        cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
        insql= "INSERT INTO pypic(score,picData) VALUES ('"+score+"','"+picdata+"')"
        cursor.execute(insql)
        db.commit()
        db.close()

    def inFaceURL(self, score, picurl):
        db = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             database='test')
        cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
        picurl =picurl.replace("\\","/")
        insql = "INSERT INTO picurl(score,url) VALUES ('" + score + "','" + picurl + "')"
        cursor.execute(insql)
        db.commit()
        db.close()

    def outFaceData(self):
        db = pymysql.connect(host='localhost',
                                  user='root',
                                  password='123456',
                                  database='test')
        cursor = db.cursor()  # 使用 cursor() 方法创建一个游标对象 cursor
        selectsql= "SELECT * FROM `pypic`"
        cursor.execute(selectsql)
        data = cursor.fetchall()
        db.close()
        return data


# 关闭数据库连接
