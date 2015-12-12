'''If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.'''

numList = []
num = 3
while num < 1000:
    numList.append(num)
    num += 3
num = 5
while num < 1000:
    if num not in numList:
        numList.append(num)
    num += 5
finalNum = 0
for number in numList:
    finalNum += number

print finalNum