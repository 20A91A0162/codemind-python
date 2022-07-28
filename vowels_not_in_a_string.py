s=input()
vow='aeiou'
v=[i for i in vow if i not in s]
if len(v)==0:
    print(0)
else:
    print(*v)