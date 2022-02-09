import requests
from lxml import etree
import json

class Baidu(object):

    # 定义请求头和url
    def __init__(self,name):
        self.url = 'https://tieba.baidu.com/f?ie=utf-8&kw={}'.format(name)
        self.header = {
            # "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69"
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0; DigExt)"
        }
    # 发送请求，拿到数据
    def get_data(self):
        res = requests.get(self.url,headers=self.header)
        print(res.status_code)
        return res.text
    # 解析数据
    def parse_data(self):
        data = self.get_data()
        html = etree.HTML(data)
        data_list = html.xpath('//li[@class=" j_thread_list clearfix thread_item_box"]/div/div[2]/div[1]/div[1]/a')
        dataList = []
        for li in data_list:
            temp = {}
            temp['title'] = li.xpath('./text()')[0]
            temp['url'] = 'https://tieba.baidu.com' + li.xpath('./@href')[0]
            dataList.append(temp)
        return dataList
    # 保存数据
    def savedata(self,data):
        with open('./baidu_data.txt','w',encoding='utf-8') as f:
            for d in data:
                f.write(json.dumps(d, ensure_ascii=True))
        f.close()

if __name__ == '__main__':
    baidu = Baidu('李易峰吧')
    res_text = baidu.parse_data()
    print(len(res_text))
    baidu.savedata(res_text)