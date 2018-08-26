# find largest product 13 length string
temp_prod = 1
max = 1

with open('num_block', 'r') as numblock:
    data = numblock.read().replace('\n', '')

def get_sum(num):
    ret = 1
    for i in range(13):
        ret = ret * int(data[num+i])
    return ret

max = get_sum(0)
temp_prod = get_sum(0)

# now we have to check for zero division <- DONT DO THAT
i = 0
while i + 14 < 1000:
    i = i + 1
    temp_prod = get_sum(i)
    if temp_prod > max:
        print(temp_prod)
        max = temp_prod
print(max)

