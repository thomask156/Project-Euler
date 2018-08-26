

# Find the sum of all the multiples of 3 or 5 below 1000

num_sum = 0

for i in range(1, 1000):
    if i % 3 is 0 and i % 5 is not 0:
        num_sum = num_sum + i
    elif i % 5 is 0 and i % 3 is not 0:
        num_sum = num_sum + i
    elif i % 3 is i % 5 and i % 3 is 0:
        num_sum = num_sum + i

print(num_sum)