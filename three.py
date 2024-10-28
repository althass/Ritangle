num = 120
numbers = [60,30,20,15,20,12,12,12,12,]
highest = 0
incorrectArray = []
arr = [1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60]

def makeSum(num, numbers, memo=None):
    if memo is None:
        memo = {}
    
    if num in memo:
        return memo[num]
    
    if num == 0:
        memo[num] = True
        return True
    
    if num < 0:
        incorrectArray.append(num)
        memo[num] = False
        return False
    
    for i in reversed(numbers):  
        copy_numbers = numbers.copy()  
        copy_numbers.remove(i)  
        remainder = num - i
        
        if makeSum(remainder, copy_numbers, memo):
            memo[num] = True
            return True
    
    incorrectArray.append(num)
    memo[num] = False
    return False

def checker():
    for i in range(len(arr) - 1, 0, -1):
        memo = {}
        
        if makeSum(num, numbers, memo) == False:
            numbers.append(arr[i])
            copy = numbers.copy()  
            if makeSum(num, copy) == False:
                continue
            else:
                numbers.remove(arr[i])
                break
    
    print("Final numbers:", numbers)
    print("Incorrect sums:", incorrectArray)

print(makeSum(num, numbers))

sum = 0
for i in range(len(numbers)):
    sum += numbers[i]

print(sum)
