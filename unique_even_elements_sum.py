n=int(input())
lst=list(map(int,input().split()))
s=set(lst)
es=0
for i in s:
    if i%2==0:
        es=es+i
print(es)