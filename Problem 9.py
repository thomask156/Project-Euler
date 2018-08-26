# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

# the hypotenuse is always the greatest side, aka c > a  and c > b
import math

for a in range(1, 500):
    for b in range(1, a):
        check = math.pow(a, 2) + math.pow(b, 2)
        check = math.sqrt(check)
        if check - math.floor(check) == 0.0:
            if a + b + int(check) == 1000:
                print(str(a)+ " "+str(b)+ " "+ str(int(check)))
                print(int(a*b*check))