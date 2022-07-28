n=input()
cnt=0
vow='aeiouAEIOU'
for i in n:
    if i in vow:
        cnt+=1
print(cnt)