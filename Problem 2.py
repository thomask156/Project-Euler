# By considering the terms in the Fibonacci sequence whose
# values do not exceed four million, find the sum of the even-valued terms.

prev = 1
curr = 1
temp = 0
fib_sum = 0

while curr < 4000000:
    temp = curr + prev
    prev = curr
    curr = temp
    if curr % 2 is 0:
        fib_sum = fib_sum + curr

print(fib_sum)