import math

def findMax(numsList):
    maxNum = -math.inf
    for i in range(len(numsList) - 1):
        num = numsList[i] * numsList[i + 1]
        if num > maxNum:
            maxNum = num
    return maxNum

numsList = [1, 2, 3, -1, -2, -5]

print(findMax(numsList))