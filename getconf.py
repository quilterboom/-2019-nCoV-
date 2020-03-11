from configparser import ConfigParser

class Conf:
    def __init__(self,filename):
        self.conf = ConfigParser()
        self.conf.read(filename,encoding='utf-8')

    def get_str(self,data1,data2):
        return self.conf.get(data1,data2)

# if __name__ == '__main__':
#     a = Conf('config.conf').get_str('cc','country')
#     print(a)