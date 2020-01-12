'''
user =  {
        'name':'arun',
        'age':23,
        'marks': 100,
        'hobby':'chess'
        
        }


user1={
     'state':'u.k',
     'city':'rishikesh'
     }

user.update(user1)
print(user)
'''

# Returns a dictionary with the specified keys and values
# takes 2 arguments

'''
x = ('key1', 'key2', 'key3')
y = 0

user = dict.fromkeys(x)

print(user)
'''

# or


'''
d={}

d=dict.fromkeys ('abc',' 24')

print(d)
'''



'''
cube={}
for i in range(1,10):
    cube[i]= i**3
print(cube)

'''

'''
user={}

user['name'] =  input('what is your name =')
user['age']  =  int(input('enter your age ='))
user['place']=  input(' enter your place =')



print(user)
'''

# concate dictionaries
'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}
for i in (dic1, dic2, dic3):
     dic4.update(i)
print(dic4)
'''
# if want this

'''
m={
   'k':dic1,
   'l':dic2,
   'p':dic3
   }
print(m)
'''

#wap to sum all the item in dict
'''
my_dict = {'data1':100,'data2':-54,'data3':247}
print(sum(my_dict.values())) 
'''
# or
'''
user = {'data1':10,'data2':4,'data3':2}
result=0
for i in user:    
    result=result + user[i]

print(result)
'''

# Write a Python program to multiply all the items in a dictionary.
'''
user = {'data1':10,'data2':4,'data3':2}
result=1
for i in user:    
    result=result * user[i]

print(result)
'''

#Write a Python program to map two lists into a dictionary.

'''
keys = ['red', 'green', 'blue']
values = [6,8,12]

user = dict(zip(keys, values))
print(user)
'''

#Write a Python program to sort a dictionary by key.
'''
user    = {'red':  1,
          'green': 2,
          'black': 3,
          'white': 4
           }
for i in sorted(user):
     print(i,user[i])
'''	


# counting of words in string

'''
s='goodboy' 
s1={}

for i in s:
     s1[i] = s.count(i)
print(s1)
'''

##counting of char in list

'''
s=[1,1,4,4,5,6,'age', 'fire','kite','age']
s1={}

for i in s:
     s1[i] = s.count(i)
print(s1)
'''



##
'''
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('the quick brown fox jumps over the lazy dog.'))
'''


c=dict({'name':input('enter the name='),
       'age' :input('enter the age=')})
print(c)






































































