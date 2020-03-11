import requests
from workforsql import ws

class GetDate:
    def __init__(self,province,city):
        """

        :param province: 省份
        :param city: 城市名
        """
        self.city = city
        self.province=province
        self.url = 'https://api.inews.qq.com/newsqa/v1/query/pubished/daily/list?province={}&city={}'.format(self.province,self.city)
        self.dataall = []

    # 获取到网络上的数据
    def get_data(self):
        head = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400"}
        # 进行请求
        # 设置代理让fiddler抓包，requests中proxies=proxies verify=False
        # proxies={"https":"https://localhost:8888"}
        rq = requests.get(self.url,headers=head)
        # 对数据进行解析
        self.dataall = rq.json()['data']
        return self.dataall

    # 往数据库添加数据
    def insert_data(self):
        # 获取网络上的最新数据，去掉前面的0
        datall = self.get_data()
        # 从数据库中读取数据，确认是否存在最新时间的数据
        sql = 'select data,confirm_add from  feiyanpd WHERE city="{}" ORDER BY data desc LIMIT 1'.format(self.city)
        db_data = ws().do_sql_one(sql)
        # 如果出现异常，那就是说没有相关数据，执行增加操作
        try:
            # 数据库时间
            db_date =db_data['data']
            # 数据库新增人数
            db_priadd = db_data['confirm_add']
            # 网络时间
            da = datall[-1]['date'].lstrip('0')
            # 网络上新增人数
            daadd = datall[-1]['confirm_add']
            if daadd is '':
                daadd=0
            # 判断时间是否相等
            if db_date == da:
                # 判断新增人数是否一致
                if int(db_priadd) == int(daadd):
                    print('数据一致')
                else:
                    print('修改数据')
                    # for i in datall:
                    #     data, city, confirm, dead, heal, confadd = self.get_onerow_data(i)
                    #     # 先清空数据库
                    #     print('清空数据库')
                    #     self.delete_data(city)
                    # 先清空数据库
                    print('清空数据库')
                    self.delete_data(self.city)
                    # 再添加数据
                    print('添加数据库')
                    self.get_all_new_data(datall)
                    #data, city, confirm, dead, heal, confadd = self.get_onerow_data(datall[-1])
                    #self.updata_data(confirm,dead,heal,confadd,data,self.province,city)
            # 时间不相等，那就全部重新更新
            else:
                # for i in datall:
                #     data, city, confirm, dead, heal, confadd = self.get_onerow_data(i)
                #     # 先清空数据库
                #     print('清空数据库')
                #     self.delete_data(city)
                # 先清空数据库
                print('清空数据库')
                self.delete_data(self.city)
                # 再添加数据
                print('添加数据库')
                self.get_all_new_data(datall)

        except TypeError as e:
            # 执行新增操作
            self.get_all_new_data(datall)

    # 全部覆盖
    def get_all_new_data(self,datall):
        for i in datall:
            data = i['date']  # 时间

            city = i['city']  # 城市
            confirm = i['confirm']  # 确证人数
            dead = i['dead']  # 死亡人数
            heal = i['heal']  # 治愈人数
            confadd = i['confirm_add']  # 新增人数
            if confadd is '':
                confadd = 0
            sql = 'insert into feiyanpd(data,country,confirm,dead,heal,confirm_add,city) values ({},"{}",{},{},{},{},"{}")'.format(
                data, self.province, confirm, dead, heal, confadd, city)
            ws().do_insert_data(sql)

    # 修改数据
    def updata_data(self,confirm,dead,heal,confadd,data,country,city):
        sql_updat = 'UPDATE feiyanpd set ' \
                    'confirm={},dead={},heal={},confirm_add={} ' \
                    'where data={} and country="{}" and city="{}"'.format(confirm, dead, heal, confadd, data,country,city)
        ws().do_updata(sql_updat)

    def delete_data(self,city):
        sql_delete = 'DELETE from feiyanpd WHERE city="{}"'.format(city)
        ws().do_updata(sql_delete)

    # 取出一个字典里面的数据
    def get_onerow_data(self,date):
        data = date['date']  # 时间
        city = date['city'] # 城市
        confirm = date['confirm'] # 确证人数
        dead = date['dead'] # 死亡人数
        heal = date['heal'] # 治愈人数
        confadd = date['confirm_add'] # 新增人数
        if confadd is '':
            confadd=0
        return data,city,confirm,dead,heal,confadd


if __name__ == '__main__':
    a = GetDate('广东','深圳').insert_data()