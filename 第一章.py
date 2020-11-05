from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import re
url='https://www.uuzuowen.com/mingzhu/luanshijiaren/36213.html'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36'}
ret=Request(url,headers=headers)
html=urlopen(ret).read().decode('gbk')
bs=BeautifulSoup(html,"html.parser")
wenzi=bs.find('div',{'class':"articleContent"})
#    titles=bs.find('title')
#    for title in titles:
#        title = titles.get_text()
for wen in wenzi:
        wen = wenzi.get_text()
        print(wen)
with open('乱世佳人第一章.txt', 'w',encoding='utf-8') as file:  # 加入写入文件
    file.write(wen)