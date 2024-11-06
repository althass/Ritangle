sqr = [1,4,9,16,25,36,49,64,81,100]
arr = []
for number in range(10,100):
    strnum = str(number)
    if int(strnum[0]) + int(strnum[1]) in sqr:
        arr.append(strnum)
print(arr)

array = []
i = 0
while len(str(i**3)) < 3:
    array.append(i**3)
    i +=1
print(array)

