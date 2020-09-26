import random

d={1:'周嘉铖',3:'钱珑超',4:'徐展',5:'尤桉哲',6:'钱涛',7:'黄舒怡',8:'胡志辉',9:'吴昭耀',10:'陈萌萌',11:'郑巧悦',12:'陈艳',13:'梁明皓',14:'蒋俊超',15:'徐颖',16:'倪宏涛',17:'潘梦倩',18:'俞靖庐',19:'王中阳',20:'毛贞强',21:'张嫒',23:'朱速航',24:'陈涛',25:'陆元超',26:'叶振雄',27:'奚申杰',28:'叶梦婷',29:'徐丽丽',30:'潘艳'}

picknumber=random.randint(1,28)
print("一共取" + str(picknumber) + "个人")
s=random.sample(d.keys(), picknumber)
print(s)
list_1=s
list_2=[]
for i in list_1:
    list_2.append(d[i])
print(list_2)