def findIdx(a:list, x:float) -> int:
    for i, val in enumerate(a):
        if val == x:
            print('///', i)
            return i
    return 0


print('set size of array')
size:int = int(input('size: '))
arr = [0] * size

print("///filling of array///")

for i in range(size):
    print("array index-", i, " element: ", sep='', end='')
    arr[i] = float(input())

summa:float = 0

for i in range(0, size, 2):
    summa += arr[i]
print("sum of odd elements of array: ", summa)

first = findIdx(arr, 0.0)
last = size - findIdx(arr[::-1], 0.0) - 1

mult:float = 0

if first != last:
    mult = 1
    for i in range(first + 1, last):
        mult *= arr[i]
print("multiply of array: ", mult)