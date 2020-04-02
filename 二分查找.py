#二分查找  
def BinarySearch(lists, left, right, key, tag, mid = 0, found = False):  
    count = len(lists[left:right+1]) + 1  
    if tag == 0:  
        mid = count // 2  
    elif tag == 1:  
        mid += count // 2  
    else:  
        mid -= count // 2  
  
    if lists[mid] == key:  
        found = True  
    else:  
        while left < right:  
            if lists[mid] > key:  
                right = mid  
                tag = 2  
                return BinarySearch(lists, left, right, key, tag, mid, found)  
            elif lists[mid] < key:  
                left = mid + 1  
                tag = 1  
                return BinarySearch(lists, left, right, key, tag, mid, found)  
    if found:  
        print("{}found, index is {}".format(key, mid))  
    elif left >= right and not found:  
        print("{}is not found in lists".format(key)) 
  
L = [1, 2, 3, 4, 5, 6, 7, 8, 9]  
for i in range(0, 11):  
    BinarySearch(L, key = i, left = 0, right=len(L)-1, tag = 0)
