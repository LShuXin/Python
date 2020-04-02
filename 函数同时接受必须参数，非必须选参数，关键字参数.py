#同时接受不确定个数位置参数和不确定个数关键字参数，并打印或对参数做操作
def greet(name,greeting='你好',pun='!'):
    print ('{0},{1}{2}'.format(name,greeting,pun))
greet('liushuxin')
greet('刘树信',greeting='你好呀',pun='。。。')
