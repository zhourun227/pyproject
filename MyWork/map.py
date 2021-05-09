import sys

# 从标准输入过来的数据
for line in sys.stdin:
    # 把首位的空格去掉
    line = line.strip()
    # 把这一行文本切分成单词(按照空格)
    words = line.split()
    # 对见到的单词进行次数标注(出现1次)
    for word in words:
        print('%s\t%s' % (word, 1))

       