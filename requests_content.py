import requests

class GithubImg(object):
    def __init__(self):
        self.url = "https://github.com/favicon.ico"

    def getdata(self):
        try:
            return requests.get(self.url).content
        except:
            print("fail")

    def savedata(self):
        res = self.getdata()
        with open('favicon.ico', 'wb') as f:
            f.write(res)
        f.close()

if __name__ == '__main__':
    getgithubimg = GithubImg()
    getgithubimg.savedata()
    print("成功")