import math

def isprime(num):
    for i in range(2,math.ceil(num/2) + 1):
        if num % i == 0:
            return False

    return True

arr = []
def ispalindrome(num):
    num_str = str(num)
    mid = math.ceil(len(num_str) / 2)
    
    for i in range(mid):
        if num_str[i] != num_str[-(i + 1)]:
            return False
            
    return True
for i in range(999):
    if isprime(i):
        if ispalindrome(i):
            arr.append(i)

print(arr)
    


        



