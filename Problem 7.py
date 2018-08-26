# brute force here, not sure of another way, used some dynamic programming to save the only values we have to check
count = 0
num_check = 1
prime_num = 1
primes = [2]
def prime(num):
    for i in primes:
        if num % i is 0:
            return False
    return True

while count < 10000:
    num_check = num_check + 2
    if prime(num_check):
        primes.append(num_check)
        count = count + 1
        prime_num = num_check

print(prime_num)

