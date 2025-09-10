# numbers = [1, 2, 3, 4, 5, 6]
# mixed = ['Donald', 1, 2, 3.56]

# print (numbers)
# print (mixed)

# p = list('DONALD')
# print(p)

# ### tuples

# integers = (1, 2, 3, 4, 5, 6)
# lists = [1, 2, 3, 4, 5, 6]

# print(integers)
# print(tuple(lists))

# ### dictionary

# d = dict(
#     a = 2,
#     b = 3,
#     c = 3
# )
# print(d)
# print(d.get('c'))

# ### sets
# set1 = {1, 2, 3, 4}
# print(set1)

# set2 = set(["Geek", "for", "Guitar"])
# print(set2)


# ### list comprehension
# a = [1, 2, 3, 4, 5 ]
# result = [val ** 2 for val in a]
# print(result)



nums = [8, 2, 9, 6, 7]
target = 11
total = 0

for i in range(1, len(nums)):
    print(i)

x=121
   
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if str(x) == str(x)[::-1]:
#             return True
#         else:
#             return False
#     isPalindrome()

nums = [1, 2, 3, 4]
squares = list(map(lambda x: x**2, nums))
print(squares)
