# Find the sum of all the primes below two million.
# Have to use sieve of Eratosthenes
import math

def sieve(num):
    arr = [True] * num
    for i in range(2, int(math.sqrt(num))+1):
        if arr[i]:
            for j in range(int(math.pow(i, 2)), num+1, i):
                if j < num:
                    arr[j] = False
    return arr

size = 2000000
primes = sieve(size)
sum = 0
for i in range(2, size):
    if primes[i]:
        sum = sum + i


print(sum)
