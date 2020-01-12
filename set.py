# set

'''
a={1,2,3,4}
print(a[1]) # can not be indexed as it is unordered
'''

# it contain only unique elements

'''
a={1,2,3,3,4,4,4,5,6,7,7}
print(a)
'''

'''
a={1,2,3,4}

if 2 in a:
     print('present')
'''

# func

# union
'''
set1 = {1,2,3,4,5}
set2 = {5,6,'i'}

print(set1.union(set2))
'''
# or

'''
set1 = {1,2,3,4,5}
set2 = {5,6}

print(set1|set2)
'''

# intersectn

'''
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}

print(set1.intersection(set2))

#or

print(set1&set2)
'''


# subset

'''
set1 = {1,2,3,4,5}
set2 = {4,5}

print(set2.issubset(set1))

# or

set1 = {1,2,3,4,5}
set2 = {4,5,6}

print(set2.issubset(set1))
'''


# superset

set1 = {1,2,3,4,5}
set2 = {4,5,8}

print(set1.issuperset(set2))


# method

'''
s={1,2,3,4}

s.add(5)
print(s)
'''

#
'''
s={1,2,3,4,5}

s.remove(4)
print(s)
'''

#
'''
s = {1,2,3,4,5}
s.discard(4)
print(s)
'''





































