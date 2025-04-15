"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order."""
num = [1, 4, 8, 9]
target = 9
num1 = 0
num2 = 1

while True:
    for i in range(len(num)):
        if num[num1] + num[num2] == target:
            print(num[num1], num[num2])
            break
        else:
            num2 += 1
            if num2 == len(num):
                break
    num1 += 1
    if num1 == len(num):
        break
    elif num2 == len(num):
        break
