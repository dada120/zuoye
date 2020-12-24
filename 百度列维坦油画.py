from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import json
import os
from urllib.request import urlretrieve
path="C:\\Users\\Administrator\\Desktop\\"
os.mkdir(path + '列维坦画作2')  #创建文件夹
t = 0
for i in range(0,61,30):
    url='https://image.baidu.com/search/acjson?tn=resultjson_com&logid=9943426075809882082&ipn=rj&ct=201326592&is=&fp=result&queryWord=%E5%88%97%E7%BB%B4%E5%9D%A6%E9%A3%8E%E6%99%AF%E6%B2%B9%E7%94%BB&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&word=%E5%88%97%E7%BB%B4%E5%9D%A6%E9%A3%8E%E6%99%AF%E6%B2%B9%E7%94%BB&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=&fr=&expermode=&force=&pn='+str(1)+'&rn=30&gsm=1e&1608192154509='
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
    ret = Request(url, headers=header)
    html = urlopen(ret).read().decode('utf-8')
    bs = BeautifulSoup(html, 'html.parser')
    all = json.loads(html)
    # print(all)
    for i in all['data']:
        try:
            a=(i['thumbURL'])
            t = t+1
            urlretrieve(a, path + '列维坦画作2\\{}.jpg'.format(t))
        except:
            print('')

