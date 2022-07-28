def count_voe(word):
    voe='aeiou'
    cnt=0
    for i in word:
        if i in voe:
            cnt=cnt+1
    return cnt
s=input()
word=s.split()
view=[count_voe(i)for i in word]
mn=max(view)
print(view.count(mn))