import requests
from lxml import etree

class getMaoyan(object):
    def __init__(self):
        self.one_url = 'https://www.maoyan.com/board/4?timeStamp=1643269660431&channelId=40011&index=5&signKey=7d5a3728388346ea6a068faa6ca72f1f&sVersion=1&webdriver=false'
        self.base_url = 'https://www.maoyan.com/board/4?timeStamp=1643269660431&channelId=40011&index=5&signKey=7d5a3728388346ea6a068faa6ca72f1f&sVersion=1&webdriver=false&offset='
        self.page = 0
        self.header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69'
        }

    def getdata(self):
        for i in range(0,100,10):
            if i == 0:
                url = self.one_url
            else:
                url = self.base_url + i
            print(url)
            res = requests.get(url,headers=self.header)
            if res.status_code == 200:
                return  res.text
            else:
                print('------------------采集错误，错误page为%d---------------'%i)

    def pasedata(self):
        data = self.getdata()
        html = etree.HTML(data)
        list = html.xpath('')
        datalist = []
        for li in list:
            temp = {}
            temp['title'] = li.xpath('')
            temp['state'] = li.xpath('')
            datalist.append(temp)
        return datalist

if __name__ == '__main__':
    getmaoyan = getMaoyan()
    getmaoyan.pasedata()