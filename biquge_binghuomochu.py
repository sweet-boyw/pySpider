import requests
import pymongo
from lxml import etree

class BiqugeBinghuomochu(object):
    # 初始化项目
    def __init__(self):
        self.url = 'https://www.xbiquge.la/9/8179/'
        self.header = {}
        self.data = {}
        self.Baseurl = 'https://www.xbiquge.la/'
    # 获取数据
    def getdata(self,url):
        try:
            res = requests.get(url)
            if res.status_code == 200:
                return res.text
        except:
            return res.status_code
    # 解析数据
    def parsePage(self,data):
        html = etree.HTML(data)
        list = html.xpath('//div[@id="list"]/dl/dd')
        page = []
        for li in list:
            temp = {}
            temp['title'] = li.xpath('./a/text()')[0]
            temp['url'] = self.Baseurl + li.xpath('./a/@href')[0]
            page.append(temp)
        return page
    # 连接mongo数据库
    def savedata(self):
        client = pymongo.MongoClient(host='localhost',port=27017)
        db = client['studytest']
        return db
    # 主任务
    def run(self):
        res = self.getdata(self.url)
        page = self.parsePage(res)
        sheet = self.savedata()
        pageSheet = sheet['binghuomochu']
        result = pageSheet.insert_many(page)
        print(result)


if __name__ == '__main__':
    binghuo = BiqugeBinghuomochu()
    res = binghuo.run()
