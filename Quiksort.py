def quiksort(a):
    n = len(a)
    if n <= 1 :
        return a
    pivot = a[0]
    smaller, larger = [],[]
    for i in range (1,n):
        if a[i] < pivot:
            smaller.append(a[i])
        else:
            larger.append(a[i])
    smaller = quiksort(smaller)
    larger = quiksort(larger)
    return smaller + [pivot] +larger

a = [7, 2, 4, 8, 1, 5, 3, 6]
print(a)
print(quiksort(a))
