def bubblesort(L):
    for i in range(len(L)-1):
        for j in range(len(L)-i-1):
            if L[j] > L[j+1]:
                L[j],L[j+1] = L[j+1],L[j]
    return L

L = [1,85,6,5,95]

print(bubblesort(L))