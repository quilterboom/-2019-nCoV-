import pymysql

class ws:
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',
                               user='root',
                               password='123456',
                               db='test1',
                               port=3306,
                               charset='utf8',
                               cursorclass=pymysql.cursors.DictCursor)
        self.cursor = self.conn.cursor()

    def do_insert_data(self,sql,args=None):
        self.cursor.execute(sql,args=args)
        self.conn.commit()
        self.do_close()

    def do_updata(self,sql,args=None):
        self.cursor.execute(sql,args)
        self.conn.commit()
        self.do_close()

    def do_sql_one(self,sql,args=None):
        """
        :param sql:
        :param args:输入元组，给sql传参
     :return:
        """
        self.cursor.execute(sql,args)
        self.do_close()
        return self.cursor.fetchone()

    def do_sql_all(self,sql,args=None):
        """

        :param sql:
        :param args: 输入元组，给sql传参
        :return:
        """

        self.cursor.execute(sql,args)
        self.do_close()
        return self.cursor.fetchall()

    def do_close(self):
        self.cursor.close()
        self.conn.close()

    #sql="insert into datafenx(name) values (%s)"
    #cursor.execute(sql,args=('hao2',))
   # conn.commit()
   # res = cursor.fetchall()
   # print(res)
    #cursor.close()
   # conn.close()

if __name__ == '__main__':
    a = ws()
    sql = "select * from datafenx"
    c = a.do_sql_all(sql)
    print(c)