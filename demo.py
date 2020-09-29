filename='demo.py'    #格式错误在open（）函数的最后加上,encoding = ' utf-8 '
with open(filename, 'r') as fp:
    lines = fp.readlines()
maxLength = len(max(lines, key=len))

lines = [line.rstrip().ljust(maxLength)+'#'+str(index)+'\n'
         # string.rstrip()，可以删除 string 字符串末尾的指定字符（默认为空格）
         # string.ljust()， 返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
         for index, line in enumerate(lines)]
with open(filename[:-3]+'_new.py', 'w') as fp:
    fp.writelines(lines)

