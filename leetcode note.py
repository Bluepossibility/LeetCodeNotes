import collections
import random
import math
import re



print('\n1###############################')
"""set(iter)"""
nums = [1, 2, 3, 4, 3, 2, 1]
print(set(nums))
print(list(set(nums)))

print('\n2###############################')
"""list.sort() & sorted(list)"""
l = [1, 2, 3, 4, 3, 2, 1]
print(sorted(l))
print(l)
l.sort()
print(l.sort())
print(l)

print('\n3###############################')
"""The usage of underscore"""
print(0x23 == 0x_2_3)

print('\n4###############################')
"""list[:] create an identical list but does not refer to the same"""
l = [1, 2, 3]
l = [4]
l[:] = [5]
print(l)
l[:] = [5]
l = [4]
print(l)
print(l[:] == l)
print(l[:] is l)

print('\n5###############################')
"""The usage of ^, which performs XOR operations"""
a = 3
print(a ^ 12)
# 0011
# 1100
# 1111

print('\n6###############################')
"""The usage of % and //"""
print(4321 % 10000 // 1000)

print('\n7###############################')
"""dictionary can't keep duplicate keys"""
dic = {'3': 0, '2': 1, '3': 2}
print(dic)

print('\n8###############################')
""" The usage of colon"""
nums = [1, 2, 3, 4, 4, 5]
i_idx = nums.index(4)
rest_list = nums[:i_idx] + nums[i_idx + 1:]
print(rest_list)

print('\n9###############################')
""" The usage of double colon"""
x = 12321
x_str = str(x)
print(type(x_str[::-1]))
print(x_str[::-1])
print(x_str == x_str[::-1])
print(x_str[::-2])

print('\n10###############################')
""" The usage of double enumerate"""
for idx, val in enumerate(x_str):
    print(idx, val)

print('\n11###############################')


def isPalindrome(s: str) -> bool:
    """
    Judge whether the input string is palindrome
    :param s: input string
    :return: True or False
    """

    """
    filter(function, iterable), Construct an iterator from those elements of iterable for which function returns true. 
    iterable may be either a sequence, a container which supports iteration, or an iterator. If function is None, the 
    identity function is assumed, that is, all elements of iterable that are false are removed.

    Note that filter(function, iterable) is equivalent to the generator expression (item for item in iterable if 
    function(item)) if function is not None and (item for item in iterable if item) if function is None.
    """

    """
    The isalnum() method returns True if all characters in the string are alphanumeric (either alphabets or numbers). 
    If not, it returns False.
    """

    """
    map() function returns a map object(which is an iterator) of the results after applying the given function to each 
    item of a given iterable (list, tuple etc.)
    """
    filtered_chars = filter(lambda ch: ch.isalnum(), s)
    lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

    filtered_chars_list = list(lowercase_filtered_chars)
    reversed_chars_list = filtered_chars_list[::-1]

    return filtered_chars_list == reversed_chars_list


print(' '.isalnum())
print(','.isalnum())
print('a'.isalnum())
print(isPalindrome('abcba'))

print('\n12###############################')
s = "-42"
l = len(s)
print(len(s))
print([s[i] for i in range(l)])
print(int(s))

print('\n13###############################')
"""
The join() method takes all items in an iterable and joins them into one string.
A string must be specified as the separator.
"""
myTuple = ("John", "Peter", "Vicky")
myList = ["apple", "banana", "orange"]
print("".join(myTuple))
print("".join(myList))
separator = "#"
x = separator.join(myTuple)
y = separator.join(myList)
z = separator.join(myTuple).join(myList)
print(x)
print(y)
print(z)

print('\n14###############################')
head = None
print(not head)
print(head is not None)

print('\n15###############################')
print(True and True)
print(math.inf)

print('\n16###############################')
nums1 = [1]
print(nums1[:1])

print('\n17###############################')
s = "babad"
print(s[0:5])

print('\n18###############################')
t = ('Han shan Li', 100)
print(t)
print(*t)

print('\n19###############################')
mylist = ["apple", "banana", "cherry"]
random.shuffle(mylist)
print(mylist)

print('\n20###############################')
mylist = collections.deque(mylist)
print(mylist.popleft())
print(list(mylist))

print('\n21###############################')
print("pi")
print("pi".upper())
print("{0}".format(math.pi))
print("{:.2f}".format(math.pi))

print('\n22###############################')
s = 'mississippi'
d = collections.defaultdict(int)
for k in s:
    d[k] += 1
print(d.items())
print(d.values())

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)
print(d.items())
print(d.values())
d.clear()
print(d.items())
print(d.values())

print('\n23###############################')
d = {2: 3, 1: 89, 4: 5, 3: 0}
od = collections.OrderedDict(sorted(d.items()))
print(od)

print('\n24###############################')
print(math.gcd(50,775))
print(math.gcd(5,35))
print(math.gcd(8,30))

print('\n25###############################')
data = 88
print(chr(88).upper())
print(ord(chr(88)))

binary_data = bin(data)
print(type(binary_data), binary_data)
print(int(binary_data, 2))

hex_data = hex(data)
print(type(hex_data), hex_data)
print(int(hex_data, 16))


print('\n26###############################')


def prime(n):
    return n > 1 and all(n % d for d in range(2, int(n**.5)+1))


for i in range(1, 10):
    print(prime(i))

print('\n27###############################')
"""Another way for a+b"""
a = 4396
b = 2200
while b != 0:
    temp = (a & b) << 1
    a = a ^ b
    b = temp
print(a)

print('\n28###############################')
"""Distinguish upper letter, lower letter, number, special_char"""
pswd = 'Lhs981206!'
Upper = '[A-Z]'
SSS = 'ZZZ'
Lowwer = '[a-z]'
num = '\d'
chars = '[^A-Za-z0-9_]'
patterns = [Upper, Lowwer, num, chars]
for pattern in patterns:
    print(re.search(pattern, pswd))

print('L'.isalpha() and 'L'.isupper() and 'L'.isalnum())
print('l'.isalpha() and 'l'.islower() and 'l'.isalnum())
print('9'.isdigit() and '9'.isalnum() and '9'.isdecimal())
print('!'.isalnum())

c = '\u00B1'
print(c.isdecimal())
print(c.isdigit())

print('\n29###############################')
array = [[0]*5 for _ in range(4)]
print(array)
print(math.lcm(4, 6), math.gcd(27, 15))

print('\n30###############################')
a = [1,2,3]
b = []
b.append(a[0])
b[0] = 4
print(a)
print(b)

print('\n31###############################')
print(bool(0), bool(1), bool(-1))

print('\n32###############################')
n = 16
print(type(n**.5))
print(n**.5 == int(n**.5))

n=8
print(math.isqrt(n)**2 == n)

s = ".*"
print(s[0:0+2])


print('\n32###############################')
print(77+11)
