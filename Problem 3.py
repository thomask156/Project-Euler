import math
# What is the largest prime factor of the number 600851475143 ?

for i in range(1, int(math.sqrt(600851475143))):
    if 600851475143 % i is 0:
        print(i)
        # here I just looked at the numbers and determined that 6857 is prime
