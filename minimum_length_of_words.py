n=input()
words=n.split()
lengths=[len(i)for i in words]
print(min(lengths))