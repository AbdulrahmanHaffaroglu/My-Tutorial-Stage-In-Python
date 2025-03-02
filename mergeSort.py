def merge(l,m,r,arr):
    n1 = m - l + 1
    n2 = r - m

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = arr[i + l]
    for j in range(n2):
        R[j] = arr[m + j + 1]

    i = 0
    j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def sort(l,r,arr):
    if l < r:
        m = l + (r - l) // 2

        sort(l,m,arr)
        sort(m+1,r,arr)

        merge(l,m,r,arr)

arr = [12,81,293,14,92,3]

sort(0,len(arr) - 1,arr)

print(arr)