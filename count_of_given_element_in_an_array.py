n=int(input())
lst=list(map(int,input().split()))
z=int(input())
cnt=0
for i in lst:
    if i==z:
        cnt+=1
print(cnt)