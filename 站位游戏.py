import random           #引入库
s=random.randint(10,50) #随机生成
print("一共有" + str(s) + "个人参加")         #此处为界面设计
m =(input("请选择你的站位："))
t=3 #报到3的人淘汰
list1=[i for i in range(1,s+1)]
                                              #形成一个move函数，移动进行循环
def move(list1, sep):
    for i in range (sep):
        a = list1.pop(0)
        list1.append(a)
while len(list1) > 2:                         #最后剩余的两人为赢家
    move(list1, 2)
    list1.pop(0)
c,d =list1
print("最后剩下的两个站位：" + str(c) + "，" + str(d))
if m == c or m == d:
    print("You win")                          #此处为页面设计
else:
    print("You lost")