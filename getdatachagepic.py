import jsonpath
from workforsql import ws
import pyecharts
from getdata import GetDate


class Get_DataChage_pic:
    def __init__(self,province,city):
        self.city=city
        self.province=province
        # 确保数据是最新的
        GetDate(self.province,self.city).insert_data()
        # 从数据库中获取数据并画图
        self.sql = 'SELECT * FROM feiyanpd where country="{}" and city="{}"'.format(self.province,self.city)
        self.dataall = ws().do_sql_all(self.sql)
        # 获取时间
        self.date = jsonpath.jsonpath(self.dataall, "$..data")
        # 确诊人数
        self.confirm = jsonpath.jsonpath(self.dataall, '$..confirm')
        # 死亡人数
        self.dead = jsonpath.jsonpath(self.dataall, '$..dead')
        # 治愈人数
        self.heal = jsonpath.jsonpath(self.dataall, '$..heal')
        # 新增人数
        self.confirm_add = jsonpath.jsonpath(self.dataall, '$..confirm_add')
        # 画图
        self.get_pic()


    def get_pic(self):
        # 创建折线图
        line = pyecharts.charts.Line()
        # 设置x轴的数据
        line.add_xaxis(self.date)
        # 设置y轴的数据
        line.add_yaxis('确诊人数', self.confirm)
        line.add_yaxis('死亡人数', self.dead)
        line.add_yaxis('治愈人数', self.heal)
        line.add_yaxis('新增人数', self.confirm_add)
        # 设置标题
        opts = pyecharts.options.TitleOpts(title='{}地区'.format(self.city), subtitle='肺炎人数情况')
        line.set_global_opts(title_opts=opts)
        line.render()

if __name__ == '__main__':
    Get_DataChage_pic('湖南','长沙')