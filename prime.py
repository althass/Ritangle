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

#for i in range(999):
#    if isprime(i):
#        if ispalindrome(i):
#            arr.append(i)

def reverseprime():
    for i in range(100):
        if isprime(i):
            arr.append(str(i)[::-1])

reverseprime()
array = ['11', '31', '71', '91', '32', '92', '13', '73', '14', '34', '74', '35', '95', '16', '76', '17', '37', '97', '38', '98', '79']

print(sorted(array))



        



