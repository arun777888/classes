#reverse  num

'''
num= int(input("enter a number ="))
num1=num
rev= 0
while(num!=0):
    rem=num%10
    rev=rev*10+rem
    num=num//10
print(rev)
if num1==rev:
    print('num is pallindrome')
'''

# factorial of num

'''
num= int(input("enter a number ="))
fact=1
while (num>0):
    fact=fact*num
    print(fact)
    num=num-1
'''

# fibonacci series

'''
x=0
y=1
count=1
num= int(input("enter a number "))
while (count<=num):
    sum=x+y
    print(sum,end=' ')
    x=y
    y=sum
    count= count+1
'''



# table
'''
i= 1 
table =1

num= int(input(' enter num = '))

while(i<=10):
    table= num*i
    print(table)
    i=i+1
'''

# leap year

'''
year = int(input('enter a year'))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,' is leap year')
        else:
            print(year,' is not a leap year')
    else:
        print(year,' is leap year')
else:
    print(year,' is not a leap year')

'''


# nested while
'''
table = int(input('enter a num ='))

while table<6:
    print('tables of',table)
    
    mul = 1
    while mul<=10:
        print(table,'*',mul,'=',table*mul)
        mul+=1
    print()
    table+=1
'''


# using for loop
'''
table =1
for i in range(4,8):
    for j in range(1,11):
        print(i,'*',j,'=',i*j)
'''

# beak, continue

'''
i=1
while i<10:
    if i ==5:
        break
    print(i)
    i=i+1
'''


i=10
while i>0:
   # i=i-1
    if i ==5:
        continue
    print(i)
    i=i-1

'''
i =1
while i<20:
    if i %2 ==0:
        pass
    else:
        print(i)
    i=i+1
'''


# sum of digits using for loop

'''
total = 0
num = input('enter a num = ')
for i in range( 0, len(num)):
    total=total + int(num[i])
print(total)
'''

# sum of digits using while loop

'''
num=  int(input('enter a number'))
total=0
while num!=0:
    total = total + num%10
    num = num//10
print(total)

'''


# sum of natural num using while loop
'''
total = 0
i=1
num = int(input('enter a number'))

while i<num:
    total = total+i
    i=i+1
    print(total)

'''   

# nested while

'''
num1 = int(input('enter a num ='))
num2 =  int(input('enter a num ='))

while num1<=num2:
    
    #print('tables of',num1)  
    mul = 1
    while mul<=10:
        print(num1,'*',mul,'=',num1*mul)
        mul+=1
    print()
    num1+=1
'''

































































