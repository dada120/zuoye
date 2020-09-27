lst= eval(input('请输入列表list：'))
def qiuou(x):
    sum=0  # can't assign to function call
    # 圆括号()表示函数调用 方括号[]表示列表值的引用 你当然应该用方括号了,这是一个容易犯的错误
    for i in x:
        if i%2==0:
            sum+=1
    return sum
cishu=qiuou(lst)
print(cishu)


