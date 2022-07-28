def count_voe(words):
    voe='aeiou'
    cnt=0
    for i in words:
        if i in voe:
            cnt=cnt+1
    return cnt
s=input()
word=s.split()
view=[count_voe(i)for i in word]
mn=min(view)
print(view.count(mn))