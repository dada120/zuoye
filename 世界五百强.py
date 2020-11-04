from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import re
url="http://www.fortunechina.com/fortune500/c/2020-08/10/content_372148.htm"
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36'}
ret=Request(url,headers=headers)
html=urlopen(ret)
bs=BeautifulSoup(html,"html.parser")
titles = bs.find_all('span')
tds = bs.find_all('td')
td_1 = []
paiming_list=['排名']
shouru_list=['营业收入']
lirun_list=['利润']
country_list=['国家']
company_name=['公司名称']
for td in tds:
    td = td.get_text()
    td1 = td.strip()
    td_1.append(td1)

a1,a2,a3,a4,a5=0,1,2,3,4
while a1 < len(td_1):
    paiming_list.append(td_1[0+a1])
    a1 = a1+6
while a2 < len(td_1):
    company_name.append(td_1[0+a2])
    a2 = a2+6
while a3 < len(td_1):
    shouru_list.append(td_1[0+a3])
    a3 = a3+6
while a4 < len(td_1):
    lirun_list.append(td_1[0+a4])
    a4 = a4+6
while a5 < len(td_1):
    country_list.append(td_1[0+a5])
    a5 = a5+6

def standard_string(s,length):
    Count=0
    for aim in s:
        if('\u4e00' <= aim <= '\u9fff'):
            Count+=1
    flag=length-len(s)-Count
    return s+' '*flag
for paiming,company,shouru,lirun,country in zip(paiming_list,company_name,shouru_list,lirun_list,country_list):
    print(paiming.ljust(3),"{0:^60}".format(company),shouru.ljust(10),lirun.ljust(10),country)