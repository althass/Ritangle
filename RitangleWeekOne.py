nums = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
copy = nums.copy()
startingnum = '01' 
memo = {}
numbers = []

def removeFromList(num):
    for i in range(len(num)):
        if num[i] in memo:
            return 'invalid'
        if num[i] in nums:
            memo[num[i]] = num[i]
            nums.remove(num[i]) 
        else:
            return 'invalid'
    return 'valid'

def inmemo(num):
    for i in range(len(num)):
        if num[i] in memo:
            return True
    return False

def Ritanlge(startingnum, interval):
    global nums
    if len(startingnum) >= 3:
        nums = copy
        memo.clear()
        return 'invalid'
    if inmemo(str(startingnum)):
        nums = copy
        memo.clear()
        return 'invalid'
    if len(nums) <= 2:
        nums = copy
        memo.clear()
        return 'valid'
    if removeFromList(str(startingnum)) == 'invalid':
        nums = copy
        memo.clear()
        return 'invalid' 
    startingnum = str(int(startingnum) + interval).zfill(2)
    return Ritanlge(startingnum, interval)


def increasenum(num):
    num = int(num) + 1
    return str(num).zfill(2)

arr = []
def algorithm(startingnum, interval):
    global nums
    nums = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']
    if interval >= 25:
        numbers.append(arr)
        if int(startingnum) <= 20:
            return algorithm(increasenum(startingnum), interval = 0)
        return arr
    
    if Ritanlge(startingnum,interval) == 'valid':
        arr.append((startingnum, interval)) 
    return algorithm(startingnum, interval+1)  


print(algorithm(startingnum, interval=0))
#print(Ritanlge(startingnum, interval=9))

