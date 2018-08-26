import math
sq_sum = 0
sum_sq = 0

for i in range(1, 101):
    sq_sum = sq_sum + math.pow(i, 2)
    sum_sq = sum_sq +i
print(str(math.pow(sum_sq, 2)-sq_sum))