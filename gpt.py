arr = []

def Cchecker(a, b, c):
    total = a * b * c + a * b + b * c + c * a + a + b + c

    while c < 2024 and total < 2024:
        total = a * b * c + a * b + b * c + c * a + a + b + c
        if total == 2024:
            arr.append((a, b, c))
            return True
        c += 1

    return False

a = 1

while a < 2024:
    b = a + 1
    while b < 2024:
        c = b + 1 
        if Cchecker(a, b, c):
            print(f"Solution found: a={a}, b={b}, c={c}")
        b += 1
    a += 1

print(arr)
totalsum = 0
memo = []
for i in range(len(arr)):
    if arr[i][2] in memo:
        continue
    memo.append(arr[i][2])
    totalsum += arr[i][2]

print(totalsum)