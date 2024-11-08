ritangle = "ritangle"

triangle = "triangle"
array = [""] * 100000
arr = [""] * 100000
num = 0

for i in range(1, 1000):
    num += i
    if num + i + 1 >= 100000:
        break
    array[num] = triangle[(i - 1) % len(triangle)]

for i in range(90,len(array),90):
    if i % 90 == 0:
        if array[i] == ritangle[(i // 90 - 1) % len(ritangle)]:
            print(i, array[i])
            break