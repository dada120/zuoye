filename='demo.py'    #格式错误在open（）函数的最后加上,encoding = ' utf-8 '
with open(filename, 'r') as fp:
    lines = fp.readlines()   #赋值给lines的内容为列表,列表的第一个元素是第一行，第一行的类型为字符串
    #print（lines）
maxLength = len(max(lines, key=len))
#readlines()
#   for line in lines:
#       line_code=i+1
#       line.rstrip
#       line1_new=line1+"line_code"
#with open() as fp:   write写入
lines = [line.rstrip().ljust(maxLength)+'#'+str(index)+'\n'
         # string.rstrip()，可以删除 string 字符串末尾的指定字符（默认为空格）,string.lstrip()删前面的
         # string.ljust()， 返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
         for index, line in enumerate(lines)]#emulate（）函数为枚举函数，此处为取行号，index序号，line，内容
with open(filename[:-3]+'_new.py', 'w') as fp:
    fp.writelines(lines)

