n, m = map(int, input().split())
def a(n,m):
    l=[]
    for i in range(1,101):
        if n%i==0 and m%i==0:
            l.append(i)
    p=max(l)
    print(int((n*m)/p))
a(n,m)
# Please write your code here.