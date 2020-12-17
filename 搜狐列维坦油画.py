from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import os
from urllib.request import urlretrieve

# url='http://www.baidu.com'
# dir=os.path.abspath('.')
# work_path=os.path.join(dir,'baidu.html')
# urlretrieve(url,work_path)

# url='http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
# dir=os.path.abspath('.')
# work_path=os.path.join(dir,'Python-2.7.5.tar.bz2')
# urlretrieve(url,work_path)

url='https://www.sohu.com/a/286956359_301394'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
ret = Request(url, headers=header)
html = urlopen(ret)
bs = BeautifulSoup(html, 'html.parser')
pics = bs.find('article',{'class':"article"})
pic = pics.find_all('img')
t = 0
for link in pic:
    link = link.attrs['src']
    #print(link)
    t = t+1
    url = '{}'.format(link)
    dir = os.path.abspath(r'C:\Users\user\Desktop\列维坦画作')
    work_path=os.path.join(dir, '{}.jepg').format(t)
    urlretrieve(url, work_path)