a = [1,1,5,2,3,6,9,5,4,1,2,3,6]
b = []
c = []
for i in a:
    if i not in b:
        b.append(i)
    else:
        c.append(i)
d = set(a)
print(d)
print(a)
print (b)
print(c)