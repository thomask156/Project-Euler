# Find the largest palindrome made from the product of two 3-digit numbers

# how to cehck if it's a palindrome: split number in half and check each side

def palindrome(pal):
    if len(pal) % 2 is not 0:
        return False
    mid = int(len(pal)/2)
    left = pal[:mid]
    right = pal[mid::]
    right = right[::-1]
    for i in range(mid):
        if left[i] is not right[i]:
            return False
    return True
largest_palindrome = -1

for i in reversed(range(1, 1000, 2)):
    for p in reversed(range(1000)):
        check = i * p
        if palindrome(str(check)):
            if check > largest_palindrome:
                largest_palindrome = check
print(largest_palindrome)