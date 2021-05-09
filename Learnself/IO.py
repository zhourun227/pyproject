f=open('','r') #标示符'r'表示读
f.read() #Python把内容读到内存，用一个str对象表示
f.close()

#由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现

with open('/', 'r') as f:
    print(f.read())      #替代try... ,自动帮我们调用close()

#调用read()会一次性读取文件的全部内容,调用read(size)方法，每次最多读取size个字节的内容
#readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list

for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉


f = open('test.jpg', 'rb')
f = open('gbk.txt', 'r', encoding='gbk', errors='ignore')

#写文件
f = open('', 'w')
f.write('Hello, world!')
f.close()

with open('', 'w') as f:
    f.write('Hello, world!')

#以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
with open('', 'w','a') as f:
    f.write('Hello, world!')