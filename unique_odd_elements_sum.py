n=int(input())
lst=list(map(int,input().split()))
s=set(lst)
os=0
for i in s:
    if i%2!=0:
        os=os+i
print(os)