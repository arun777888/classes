'''
print ('e' in 'Umbrella')

a = "This is orange juice"
print ('orange' in a)
'''

#. Write a Python program to add 'ing' at the end of a given string
# (length should be at least 3). If the given string already ends
# with 'ing' then add 'ly' instead. If the string length of the
# given string is less than 3, leave it unchanged.

str1  = input('enter the string = ')
length = len(str1)
if length > 2:
     if str1[-3:] == 'ing':
          print(str1 + 'ly')
     else:
          print(str1 + 'ing')
else:
     print(str1)



#Write a Python program to get a string made of the first 2 and the
#last 2 chars from a given a string.
#If the string length is less than 2, return instead of the empty string.
'''
txt= input('enter the string =')
if len(txt) < 2:
     print('') 
else:
     print(txt[0:2] + txt[-2:])
'''


#Write a Python program to change a given string to a new string
#where the first and last chars have been exchanged.
'''
txt= input('enter the string =')
print(txt[-1:] + txt[1:-1] + txt[:1])
'''	  

#Write a Python program to remove the characters
#which have odd index values of a given string
'''
txt= input('enter the string =')
result = "" 
for i in range(len(txt)):
     if i % 2 == 0:
          result = result + txt[i]
print(result)
'''

#Write a Python program to count the number
#of characters (character frequency) in a string
'''
str1=input('enter strng =')
dict = {}
for n in str1:
     keys = dict.keys()
     if n in keys:
          dict[n] += 1
     else:
          dict[n] = 1
print(dict)
'''


#Write a Python program to count
#the occurrences of each word in a given sentence.
'''
txt=input('enter a string')

counts = dict()
words = txt.split()

for word in words:
     if word in counts:
          counts[word] += 1
     else:
          counts[word] = 1
print(counts)
'''




































