#使用递归方式完成对数字列表的二分查找
list1=[1,2,2,25,8,5,84,41644,2,5,4,65,2,4,4,5,5,449,4,6,]
search(list1, 250)
def search(seq,number,lower=0,upper=None):
    'search number from seq'
    if upper is None:
        upper=len(seq)-1
    if lower==upper:
        assert number==seq[upper]
        return upper;
    else:
        middle=(upper+lower)//2
        if number>seq[middle]:
            return search(seq,number,middle+1,upper)
        else:
            return search(seq, number, middle, upper)

