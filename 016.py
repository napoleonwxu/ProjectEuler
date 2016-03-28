def digitSum(num):
    sum = 0
    while num > 0:
        sum += num%10
        num /= 10
    return sum

print digitSum(2**1000)