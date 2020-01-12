# WAP to return a list containing square of every element . 

'''
list=[1,2,3,4,5,6]
for i in list:
    list1= i**2
    print(list1,end=" ")
'''

# or
'''
list=[1,2,3,4,5]
list1=[]
for i in range(len(list)):
    list1.append(i**2)
print(list1)
'''


    

# WAP to return a reverse list

'''
list = [1,2,3,4,5,6,7]
list1=[]
list.reverse()
list1.append(list)
print(list1)
'''

#or
'''
list=[1,2,3,4,5]
list.reverse()
print(list)
'''

# using pop and append method
'''
list=[1,2,3,4,5]
list1=[]
for i in range(len(list)):
    a=list.pop()
    list1.append(a)
print(list1)
'''

# alternate  method
'''
list=[1,2,3,4,5]
list1=list[::-1]
print(list1)
'''



# WAP to reverse string.
# list=[ 'abc', 'def', 'ghi']
'''
list=['abc', 'def', 'ghi']
list1=[]
for i in list:
    list1.append(i[::-1])
print(list1)
'''


# WAP to obtain two list containing even no and odd no.

'''
list=[1,2,3,4,5,6,7,8,9,10]
l1=[]
l2=[]
for i in range(len(list)):
    if i%2==0:
        l1.append(i)
        print(l1)
    else:
        l2.append(i)
print(l2)
'''

# WAP to return common elements
'''
list1=[1,2,3,4,5,6,7,8,9]
list2=[2,3,5,6,9]
list=[]
for i in list1:
    if i in list2:
        list.append(i)
print(list)
'''    

##  string
'''
user = 'my name is Arun dabrAl'
char = 'a'

user1=user.lower()
char1=char.lower()

print(user1.count(char1))

# or

print(user.lower().count(char.lower()))

'''
'''
list=['abc', 'def', 'ghi']
list1=[]
for i in list:
    list1.append(i[::-1])
print(list1)
'''

# remove duplicate in strings
'''
txt='aabbcbbcccaaa'

x=0

s1=''

for i in txt:
    if txt.index(i)==x:
        s1=s1+i
    x=x+1
print(s1)
'''




















































