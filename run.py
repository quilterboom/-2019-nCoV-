from getdatachagepic import Get_DataChage_pic
from getcoupcityfromweb import GetWebData

class RunData:
    def __init__(self,proivce,city):
        """

        :param proivce:
        :param city:
        """
        self.province = proivce
        self.city = city

    def chage_data(self):
        # 更新数据
        GetWebData()

    def get_data_chage_pic(self):
        # 画图
        Get_DataChage_pic(self.province,self.city)

if __name__ == '__main__':
    run = RunData('广东','惠州')
    #run.chage_data()
    run.get_data_chage_pic()
