# # # What is the value of the first triangle number to have over five hundred divisors?
# #
# # # n(n+1)/2 = sum
# # import math
# # sum = 1
# #
# # nums = {}  # a list of the number of factors for each number
# #
# # def prime(num):
# #     for i in range(2, int(num/2)+1):
# #         if num % i is 0:
# #             nums[str(i)] = 2
# #             return False
# #     return True
# #
# # # def factor(num):
# # #     if num in nums:
# # #         return nums[str(num)]
# # #     if prime(num):
# # #         return 2 # the prime number, then 1 and the number itself
# # #     for i in range(2, int(math.sqrt(num))+1):
# # #         if num % i is 0:
# # #             if prime(i):
# # #                 nums[str(i)] = 2 * factor(int(num/i))
# # #                 return nums[str(i)]
# # def factor(num):
# #     count = 2
# #     for i in range(2, int(math.sqrt(num)+1)):
# #         if num % i is 0:
# #             count = count + 2
# #     return count
# #
# # tri_num = 1
# # print(factor(8386560))
# # for i in range(2, 10000000):
# #     lnum = factor(i)
# #     rnum = factor(i+1)
# #     if lnum * rnum is 500:
# #         print(i*i+1)
# #         exit()