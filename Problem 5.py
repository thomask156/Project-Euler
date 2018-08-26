import math

# get list of primes within the range 1-20
# if two primes add up to a number under 20, we use that number and get rid of the primes, check the other ones
nums = []  # a list of the factors of each number
mult = []

def prime(num):
    for i in range(2, int(num/2)+1):
        if num % i is 0:
            return False
    return True

def factor(list, num):
    if prime(num):
        list.append(num)
        return list
    for i in range(2, int(num/2)+1):
        if num % i is 0:
            if prime(i):
                list.append(i)
                return factor(list, int(num/i))

for i in range(2, 21):
    nums.append(factor([], i))

nums = sorted(nums, key=len, reverse=True)

for k in nums:
    if k[0] not in mult:
        for l in k:
            mult.append(l)

num_sum = 1
for num in mult:
    num_sum = num_sum * num

print(num_sum)
# only need to grab the primes aka if a number is made of a prime we take it and ignore it later on
# 2520 = 5*7*8*9

