n = int(input())
arr = list(map(int, input().split()))
darr = arr
Acount = 0
Dcount = 0
for i in range(n - 1, 0, -1):
    for j in range(i):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            Acount += 1
for i in range(n - 1, 0, -1):
    for j in range(i):
        if darr[j] < darr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            Dcount += 1
print(min(Acount, Dcount))
