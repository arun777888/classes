# list comp

# use to create list in one line

# square of num
'''
s=[]
for i in range(1,11):
     s.append(i**2)

print(s)


# by using list comp

square = [i**2 for i in range(1,11)]
print(square)
'''

# neg num

'''
neg=[]

for i in range(1,11):
     neg.append(-i)
print(neg)


# by using list comp

neg = [-i for i in range(1,11)]
print(neg)
'''

# first letter of name

'''
names = ['arun','varun','tarun']
names1=[]
for i in names:
     names1.append(i[0])
print(names1)

# using list comp

names2 = [i[0] for i in names]
print(names2)
'''

# rev ['abc','tuv','xyx']

'''
l=['abc','tuv','xyz']
l1=[]
for i in l:
     l1.append(i[::-1])
print(l1)


# by using list comp

l1=[i[::-1] for i in l]
print(l1)
'''


# list comp with if statement

'''
l= [1,2,3,4,5,6,7,8]
num=[]

for i in l:
     if i%2==0:
          num.append(i)
print(num)


# using list comp

num = [ i for i in l if i%2==0]
print(num)
'''

# list comp with if else statement


'''
l = [1,2,3,4,5,6,7,8,9,10]

l2=[i*2 if i%2==0 else -i for i in l]
print(l2)

'''

# nested list
'''
l= [ [i for i in range(1,3)] for j in range(3)]
print(l)
'''

'''
lst = [[1,2,3],[4,5,6]]
for i in lst:
     for j in i:
          print(j,end=' ')
'''

s='things'
p=list(s)

print(type(p))































































































