from selenium import webdriver
import time
from getdata import GetDate
from workforsql import ws

class GetWebData:
    def __init__(self):
        # 因为页面修改，无法重页面获取span中的值，所以直接读数据库
        # self.wb = webdriver.Chrome()
        # self.wb.get('https://news.qq.com/zt2020/page/feiyan.htm')
        # time.sleep(1)
        # area = self.wb.find_elements_by_xpath(
        #     #'//div[@class="placeItemWrap"]/div[@class="clearfix placeItem placeArea"]/h2'
        #     # 2.25修改
        #     '//div[@id="listWraper"]/table[2]/tbody/tr[@class="areaBox"]/th/span'
        # )
        # for i in range(1, len(area) + 1):
        #     if i == 0:
        #         privince = '湖北'
        #     else:
        #         privince = self.wb.find_element_by_xpath(
        #             # '//div[@class="placeItemWrap"][{}]/div[@class="clearfix placeItem placeArea"]/h2'.format(i)
        #             '//div[@id="listWraper"]/table[2]/tbody[{}]/tr[@class="areaBox"]/th/span'.format(i)
        #         ).text
        #     a = self.wb.find_elements_by_xpath(
        #         #'//div[@area="{}"]/div'.format(privince)
        #         '//div[@id="listWraper"]/table[2]/tbody[{}]/tr[@class="city"]/th/span'.format(i)
        #     )
        #     for j in range(1, len(a) + 1):
        #         #city = self.wb.find_element_by_xpath('//div[@area="{}"]/div[{}]'.format(privince, j)).get_attribute('city')
        #         city = self.wb.find_element_by_xpath(
        #             '//div[@id="listWraper"]/table[2]/tbody[{}]/tr[@class="city"][{}]/th[@class="area"]/span'.format(i, j))
        #         b = city.text
        #         print(privince, b)
        #         # 获取到省份和城市，进行全部数据的获取
        #         #GetDate(privince,city).insert_data()
        # self.wb.quit()
        sql = 'select t.country,t.city FROM (select country,city,COUNT(1) from feiyanpd GROUP BY country,city) as t'
        a = ws().do_sql_all(sql)
        for i in a:
            privince=i.get('country')
            city = i.get('city')
            print(privince, city)
            GetDate(privince,city).insert_data()

if __name__ == '__main__':
    GetWebData()