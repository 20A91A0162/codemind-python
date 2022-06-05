n=int(input())
lst=list(map(int,input().split()))
s=set(lst)
esc=0
for i in s:
    if i%2==0:
        esc=esc+1
print(esc)