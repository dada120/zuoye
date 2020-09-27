from math import *

he=0
fenshu=1000
dn=(2 * pi ) / fenshu #宽
for i in range(fenshu):
    he += abs(sin(i*dn))*dn #abs函数返回数字的绝对值
print(he)