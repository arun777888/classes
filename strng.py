
#escape character
'''
a='my names is arun'
a='i\'m arun'
a = "i\'m arun"
print(a)

txt = 'We are the so-called \'Vikings\' from the north.'
print(txt)

txt = 'Your time is limited, \\\\''so don\'t waste it '
print(txt)

txt='arun \nowhere dabral'

print(r"arun\'s nowhere dabral")
'''






'''
a= "my name is arun"

total=0

for i in range(len(a)):
    total=total+i
    #print(i)
    print(a[i],end='')

for i in a:
    print(i,end='')
'''

'''
a= 'arun'
print(a[::2])
print(a[1:])
print(a[3:])
print(a[3:0:-1])
print(a[::-1])
print(a[1:8:2])
'''





# methods 
'''
a='my naME is arun'


print(len(a))
print(a.title())
print(a.capitalize())
print(a.upper())
print(a.lower())
print(a.count('a'))
print(a.count('a',6))
print(a.count('a',5,7))
'''

'''
a='***aarun***'
print(a.lstrip('*'))

print(a.rstrip('*'))

print(a.strip('*'))  # not from between

print(a.replace('a','+'))
'''

'''
a = 'hard work is a key of success'
print(a.endswith('success'))

print(a.startswith('he'))


print(a.find('e',17))
print(a.index('e',17))


print(a[8])

a='arun'
print(a.isalpha())

txt = "The rain in Spain stays mainly in the plain"
x = "ainy" in txt
print(x)

txt = "The rain in Spain stays mainly in the plain"
x = "ainy" not in txt
print(x) 
'''



'''
txt = 'banana'
x = txt.center(20, "O")

print(x)
'''

####

'''
txt = "H\te\tl\tl\to"

print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))


txt = "Hello, welcome to my world."

print(txt.find("e",3,18))   # return -1 if value is not found
print(txt.index("e",2,17))  # raise error if value is not found

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

'''

####

'''
txt = "Company12%"
x = txt.isalnum() # only(a-z and 0-9)
print(x)


txt = "50800"
x = txt.isdigit() # return true if all the char are digits
print(x)

# identifier (returns True if the string is a valid identifier,
# otherwise False.
# A string is considered a valid identifier if it only contains
# alphanumeric letters (a-z) and(0-9),or underscores (_).A valid
# identifier cannot start with a number, or contain any spaces.

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())


txt = "Hello world!"
x = txt.islower()
print(x)
'''
'''
txt = "   s   "
x = txt.isspace()
print(x)
'''
'''
# chk only alphabet characters

a = "Hello World!"
b = "hello 123"
c = "MY NAME IS PETER"

print(a.isupper())
print(b.isupper())
print(c.isupper())


#The is title()method returns True if all words in a text
#start with a upper case letter,
#AND the rest of the word are lower case letters,otherwise False.
# symbols and nums are ignored

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"

print(a.istitle())
print(b.istitle())
print(c.istitle())
print(d.istitle())
'''

# lstrip - remove any leading characters(by deafault space)
'''
txt = ",,,,,ssaaww.....banana"
x = txt.lstrip(",sw.")
print(x)

# endswith

txt = "Hello, welcome to my world."
x = txt.endswith("my world.", 5, 11)
print(x)


#The join() method takes all items in an iterable
#and joins them into one string.
#A string must be specified as the separator.
myTuple = ("John", "Peter", "Vicky")
x = ",".join(myTuple)
print(x)


#The split() method splits a string into a list.
#You can specify the separator,
#default separator is any whitespace.

txt = "welcome to the jungle"
x = txt.split()
print(x)


txt = "hello# my name is Peter# I am 26 years old"
x = txt.split("#",1)
print(x)



#Search for the word "bananas", and return a tuple with three
#elements:

#  1 - everything before the "match"
#  2 - the "match"
#  3 - everything after the "match"


txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)


# replace

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print(x)



#swapcase

txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

'''

'''
s=input('enter a strng = ')
char=input('enter a character = ')

print(s.upper().count(char.upper()))
'''



'''

txt = "I could eat bananas all day"
x = txt.partition("bananas")
print(x)
'''

# if string contain space only
'''
txt=' '
print(txt.isspace())
'''











































