n=int(input())
lst=list(map(int,input().split()))
s=set(lst)
osc=0
for i in s:
    if i%2!=0:
        osc=osc+1
print(osc)