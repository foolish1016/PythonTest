import re
import requests
import os

class Down(object):

    def _init_(self):
        pass

    def downloadPic(self,html):
        pic_url = re.findall('"objURL":"(.*?)",',html,re.S)
        index = 0
        for i in range(0,5,1):
            each = pic_url[i]
            try:
                pic =requests.get(each,timeout =10)
            except requests.exceptions.ConnectionError:
                continue
        current = os.getcwd()
        string = current+'/'+'picture'+'/'+'doutu'+str(i)+'.jpg'
        fp = open(string,'wb')
        fp.write(pic.content)
        fp.close()
        index= index+1


downobj = Down();
word = raw_input("Input key word python2 : ")
url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&ct=201326592&v=flip'
result = requests.get(url)
# dowmloadPic(result.text,word)

downobj.downloadPic(downobj,result)





