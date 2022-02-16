import requests
from lxml import etree
import pymongo

class FaBiaoQing(object):
    # 项目初始化
    def __init__(self):
        self.url = 'https://fabiaoqing.com/biaoqing'
        self.header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36",
            "Cookie": "PHPSESSID=jvud5tqo42f3q73pv8q3drjgvt; __gads=ID=e3b7a73814923679-228edf89a6d000e3:T=1645022217:RT=1645022217:S=ALNI_MY6u9P0MpT9dp-EQffHMTKmfFQ5QQ; UM_distinctid=17f02f7082618-00726a9623d506-a3e3164-1fa400-17f02f7082728c; CNZZDATA1260546685=195505447-1645012492-%7C1645012492",
            "Host": "fabiaoqing.com",
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"'
        }
    # 获取数据
    def getData(self,url):
        res = requests.get(url,headers=self.header)
        try:
            if res.status_code == '200':
                return res.content
        except:
            return res.status_code
    # 解析数据
    def parseData(self,response):
        html = etree.HTML(response)
        img = html.xpath('')
        return img
    # 存储数据
    def savaData(self,data):
        client = pymongo.MongoClient(host='localhost',port=27017)
        db = client['studytest']
        return db
    # 项目运行
    def run(self):
        res = self.getData(self.url)
        print(res)

if __name__ == '__main__':
    biaoqing = FaBiaoQing()
    biaoqing.run()
