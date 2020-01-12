l1 = [1,2,3,4]
l2= ['arun','varun']

#l=[l1,l2]
#print(l)
'''
l1.insert(1,9)
print(l1)

l1.append([12,13])
print(l1)

l1.extend([12,13])
print(l1)
'''
#l1.clear()
#print(l1)

#l1.pop()
#print(l1)

#l1.remove(1)
#print(l1)


#del l1[3:15:2]
#print(l1)


#print(l1.index(5))

#print(l1[4])

# list of lists

#l5 =[[1,2],['hi','arun']]
#print(l5)


#l_mix =['arun',4,4.5,['hi',3,4]]
#print(l_mix)


#empty_list= list()
#print(empty_list)

#print(l1[1:7:2])

# convert str to list

'''
str = 'hi, there,i am, arun'
print(str.split(','))

str1 = 'hello arun'
print(list(str1))
'''

'''
int1 = 123456
int2=str(int1)
print(list(int2))

list = [int(i) for i in str(int1)]
print(list)
'''
# creating list from dict keys or values
'''
my_dict = {'a':1,'b':2,'c':3}
key_list = list(my_dict.keys())
print(key_list)

key_list1 = list(my_dict.values())
print(key_list1)
'''


###

lst1 = ['penguin','parrot','sparrow','goose','sparrow']
print(lst1)

lst1.insert(lst1.index('sparrow')+1,'duck')
print(lst1)


'''
lst = [1,2,5,9,3,12,19,15,18,20]

lst.sort(reverse=True)
print(lst)


lst.reverse()
print(lst)
'''
#print(len(lst))
#print(max(lst))


###
'''
lst = ['a','b','c','d','e','a','A']
char = 'a'
print(lst.count(char))
'''

'''
lst = ['dog','cat','horse']

if 'dog' in lst:
     print('lst has dog')
'''
'''
lst=[1,2,3,4,5,6,7,8]
print(lst[5:0:-1])
print(lst[5::-1])
print(lst[::-1])



print(lst[::2])
print(lst[5:])
'''

# copy in list

'''
a=[1,2,3]
b=a
a[0]=20
print(a)
print(b)
'''
'''
a=[1,2,3]
b=list(a)
a[0]=20
print(a)
print(b)
'''

'''
a = [[1,2,3],[4,5]]

b=list(a)
a[0][0]=15
print(a)
print(b)
'''

import copy
'''
a = [[1,2,3],[4,5]]
b=copy.deepcopy(a)
a[0][0]=14
print(a)
print(b)
'''

## looping on list

lst = ['dog','cat','horse']
'''
for i in lst:
     print(i)
'''
'''
for i in range(0,len(lst)):
     print('index=',i,'value=',lst[i])
'''

# join a strng
'''
lst=['dog','cat','horse']

print('  '.join(lst))
'''

# list of list

import itertools
'''
lst= [[1,2,3],[4,5,6],[7,8,9]]

lst1= list(itertools.chain(*lst))
print(lst1)
'''

'''
a=[1,2,2,3,4,5,5,6,7,7]

b=[i for i in a if a.count(i)>1]
print(b)
'''

# extract unique items

'''
a=[1,2,2,3,4,5,5,6,7,7]

b=list(set(a))
print(b)

'''
##
'''
a=[1,2,3,4,5,6,7]


from collections import deque

lst = deque(a)
lst.rotate(-3)
print(lst)
'''
'''
l1=[1,9,3,10,3,4,8,13,7,12,]
#l1.reverse()
#print(l1)


l1.sort(reverse=False)
print(l1)
l1.sort(reverse=True)
print(l1)
'''

a = [[1,2,3],[4,5]]

b=list(a)
a[0]=15
print(a)
print(b)
















































































































































      
