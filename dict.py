# dictionary
'''
my_dict = {'sam':21,'bob':25,'john':27}
print(my_dict)

my_dict = {'sam':21,'bob':25,'john':27,'bob':30}
print(my_dict)

my_dict = {'a':1, 3:4,'k':[1,2,3]}
print(my_dict)

d=dict()
print(d)
'''

#method 1

'''
user=dict(name='arun',age=24)
print(user)
'''


# dict from list
'''
my_dict= dict([['a',1],['b',2],['c',3]])
print(my_dict)
'''
# nested dict

'''
my_dict = {1:{'a':1,'b':2},2:{'c':3,'d':4}}
print(my_dict)
'''

# adding element

'''
my_dict = {}

my_dict[0] = 'a'
print(my_dict)

my_dict['animals']='cat,dog'

print(my_dict)
'''

# delete elements

'''
my_dict = {'sam':21,'bob':25,'john':27}

del my_dict['sam']

print(my_dict)
'''
'''
my_dict = {'sam':21,'bob':25,'john':27}

my_dict.pop('sam')
print(my_dict)
'''

# looping

#user1=user.values()
#print(user1)

'''
my_dict = {'sam':21,'bob':25,'john':27}

for i in my_dict:
     print(my_dict[i])
'''
'''
user = {'sam':21,'bob':25,'john':27}

for i in user.values():
     print(i)


for i in user.keys():
     print(i)
'''

# for both keys and values together

'''
user = {'sam':21,'bob':25,'john':27}


for key, value in user.items():
     print(key,value)
'''

###

'''
user = {'sam':21,'bob':25,'john':27}

if 'sam' in user:
     print('user has sam')
'''


# shallow coping

'''
user = {'sam':[20,21],'bob':[22,23]}

user1=user.copy()

print(user1)


user['bob'][0] = 19

print(user)

print(user1)
'''

# deep copy

'''
import copy

user = {'sam':[20,21],'bob':[22,23]}

user1= copy.deepcopy(user)

user['bob'][0] = 30

print(user)
print(user1)
'''



# func

'''
user = {'sam':21,'bob':25,'john':27}

user1 = {'name': 'arun','age':25}

user.update(user1)

print(user)
'''

'''
user = {'sam':21,'bob':25,'john':27}

user.update({'sam':27,'name':'arun'})

print(user)
'''
'''
user = {'sam':21,'bob':25,'john':27}
print(len(user))
'''


# get method

'''
user = {'sam':21,'bob':25,'john':27}

print(user.get('name'))
'''

'''
if user.get ('name'):
     print('present')
else:
     print('not present')
'''

# more

'''
user = {'sam':21,'bob':25,'john':27}

print(user.get('bob','not found'))
'''



# user input dict

'''
user = {}

name = input('enter your name')
age  = int(input('enter your age'))
fav_movies = input('enter your fav movies').split(',')


user['name']= name
user['age'] = age
user['fav_movies'] = fav_movies

print(user)
'''

##
'''
user = {
  "name": "amit",
  "subject": "geography",
  "marks": 86
}
print(user)
'''

#for i in user:
#     print(i,user[i])


#user['fav_place']=['shimla', 'manali']
#print(user)

#if 'name' in user:
#     print('yes')

# find lenth of dict
#print(len(user))

# pop- it takes 1 argument , it removes item with the specified key 
#print(user.pop('name'))

# popitem- it takes no argument , it remove last item
#print(user.popitem())

#del user    # gives error as dict is no longer exists
#print(user)

#user.clear()
#print(user)

#
'''
myfamily = { "child1" :{
                      "name" : "Emil",
                     "year" : 2004
                       },
             
            "child2" : {
                      "name" : "Tobias",
                      "year" : 2007
                       },
            "child3" : {
                      "name" : "Linus",
                      "year" : 2011
                        }
          }
print(myfamily)
'''
# or
'''
child1 = {
            "name" : "Emil",
            "year" : 2004
          }
child2 = {
            "name" : "Tobias",
            "year" : 2007
          }
child3 = {
            "name" : "Linus",
            "year" : 2011
          }

myfamily={
     'child1':child1,
     'child2':child2,
     'child3':child3
     }

print(myfamily)
'''


# set default - it return alue if present,otherwise it takes the given value


car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(car.setdefault("model", "Bronco"))

#print(x)

#
























































































































































































































































