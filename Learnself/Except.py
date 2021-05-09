#Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')

#断言
def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'  #assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错。
    return 10 / n

def main():
    foo('0')


#logging
#把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件：
import logging
logging.basicConfig(level=logging.INFO) #有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)