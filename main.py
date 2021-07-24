# Set items are enclosed in curly brackets
# Set is unordered
# Set is mutable, can contain only immutable items
# Set elements are unique
# Elements can contain only immutable items


"""
Sets can be used for mathematical set operations such as union, intersection, difference 
and symmetric difference.

https://en.wikipedia.org/wiki/Set_(mathematics)
"""

'''
Python Set Attributes
'''

# print(dir(set))
# #  this shows the methods

'''
Creating Python sets
'''

# set = {}
# print(type(set))
#  this is not a set, but it becomes a dictionary
# set = set()
# print(type(set))

# set = set()
# set = {1,2,3}
# print(set)


'''
Modifying a set in Python
'''

set_example = {'hello', 'world!'}
# set_example[0]
# you cannot index in a set
# set_example.add('yay!')
# print(set_example)
#  we can only add immutable items
# set_example.add(['hey!'])
# print(set_example)
# set_example.add(('hey!'))

# set_example.update([1,2,3])
# # print(help(set.update))
# print(set_example)

#  https://www.programiz.com/python-programming/set



'''
Removing elements from a set
'''

# set_example = {1,2,3,4}

# set_example.discard(1)
# print(set_example)

# set_example.discard(1)
# print(set_example)
# # if we try to discard something that doesnt exist, Python does not return a mistake, just ignores the code

# set_example.remove(1)
# print(set_example)

# set_example.remove(1)
# print(set_example)
# #  in that case if we try to remove something that doesnt exist, then it will give us an error

# set_example = {1,2,3,4,5,6,7,8}
# set_example.pop()
# print(help(set.pop))
# print(set_example)
# print({'hello', 'world', 'hello', 'hello'})

'''
Set Union Operations
'''

# a = {1,2,3,6,7}
# b = {4,5,6,7,8,9}

# print(a | b)
# print(a.union(b))


'''
Set Intersections Operations
'''

# a = {1,2,3,6,7}
# b = {4,5,6,7,8,9}

# print(a & b)
# print(a.intersection(b))

# = shows what is common between the two sets



'''
Set Difference Operations
'''

# a = {1,2,3,4,6,7,9}
# b = {2,5,6,7,8,9}

# print(a - b)
# print(a.difference(b))

# print(b - a)
# print(b.difference(a))


'''
Set Symmetric Difference
'''

# a = {1,2,3,4,6,7,9}
# b = {2,5,6,7,8,9}

# print(a ^ b)
# print(a.symmetric_difference(b))


'''
Set Methods
'''

# print(dir(set))