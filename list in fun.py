
def f(x,l=[]):
    for i in range(x):
        l.append(i*i)
    print(l)

f(2)
f(3,[3,2,1])
f(3)#l列表会继承f(2)里的列表　输出为［0,1,0,1,4]