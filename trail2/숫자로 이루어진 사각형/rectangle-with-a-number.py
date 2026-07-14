
def s(n):
    a = [1,2,3,4,5,6,7,8,9,0]
#        0,1,2,3,4,5,6,7,8
    c=0
    for i in range(n):
        for x in range(n):
            d = (c+x)%9
            print(a[d], end=' ')
        c= c+n
        print()

n = int(input())
s(n)
# Please write your code here.