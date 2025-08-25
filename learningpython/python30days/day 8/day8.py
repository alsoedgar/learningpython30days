#day 8 of 30 day python challenge
print('\n********** day 8 ***********\n')

print('Dictionaries!!!\n')

#A dictioonary is a collection of unordered, mutable paired (key: value)
#data types

#creating a dictionary
#to create a dictionary we use curly braces {}, or the dict() function

#syntax
empty_dict = {}
print(empty_dict)

dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
print(dct)

person = {
    'firstname' : 'Edgar',
    'lastname' : 'Maldonado',
    'age' : 18,
    'address' : {
        'street' : '123 Main St',
        'city' : 'Chicago',
        'state' : 'IL',
        'zip' : '60601'
    }
}

print(person['address']['city']) #prints a dictionary giving values about a person
#dictionary shows that a valu ecould be any data type: string, boolean, list, tuple, set or a dictionary
#I even show a nested dictionary

#finding the length of a dictionary
#we can use len() to find the length of a dictionary

print(len(person)) #shows there's 4 values in the person dictionary
print(len(person['address'])) #shows there's 4 values in the address dictionary (len of a nested dictionary)

#accessing items in a dictionary
#we can access items in a dictionary by referring to its key name
#syntax
print(person['firstname']) #prints Edgar
print(person['address']['state']) #prints IL

#accessing an item by key name raises an error if the key does NOT exist
#so to avoid this error, we can use the get() method
#it returns none if the key does not exist
#syntax
#print(person.get('address').get('zip')) #prints 60601
#print(person('address').get('country')) #prints None since country key does not exist

#adding items to a dictionary
#we can add items to a dictionary by using a new index key and assigning a value to it
#syntax
DCT = {'key1' : 'value1', 'key2' : 'value2'}
DCT['key3added'] = 'value3added' #adds new key and value
print(DCT)

#modifying items in a dictionary
#we can modify items in a dictionary by referring to its key name
#syntax
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
print(dct)
dct['key1'] = 'value-one' #changes value of key1
print(dct)

#Checking Keys in a dictionary
#we use the in operator to chekc if a key exisrts in a dictionary
#syntax
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
print('key1' in dct) #shows that key 1 exists
print('key4' in dct) #shows that key 4 does NOT exist

#removing key and value pairs from a dictionary
#we can use three methods
#pop(key) - removes the item with the specified key name
#popitem() - removes the last item
#del keyword - removes an item with specified key name

#syntax
print('\nremoving items from a dictionary\n')
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
print(dct)
dct.pop('key1') #removes key1 and its value
print(dct)
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
dct.popitem() #removes last item
print(dct)
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
del dct['key2'] #removes key2 and its value
print(dct)

#changing dictionary to a list of items
#The items() method changes the dictionary to a list of tuples
#syntax
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
print(dct.items()) #prints a list of tuples

#clearing a dictionary
#if we dont want the items in a dictionary, we can clear them using clear() method

#syntax
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
print(dct)
dct.clear
print(dct) #prints empty dictionary/none

#deleting a dictionary
#if we do not use the dictionary anymore, we can delete it using the del keyword
#syntax
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
print(dct)
del dct['key2']
print(dct)

#Copy a dictionary
#We can copy a dictionary using the copy() method or the dict() function
#This helps avoid mutation
#syntax
print('\ncopying a dictionary\n')
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
dct2 = dct.copy() #this creates a copy of the first dictionary
print(dct2)

#getting dictionary keys as a list
#we can get all the keys in a dictionary using the keys() method
#syntax
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
print(dct.keys()) #prints a list of all the keys, skips the values

#getting dictionary values as a list
#we can get all the values in a dictionary using the values() method
#syntax
dct = {'key1' : 'value1', 'key2' : 'value2', 'key3' : 'value3'}
print(dct.values()) #prints a list of all the values, skips the keys

print('\n******************EXERCISES******************\n')

dog = {}
dog['name'] = 'Buddy'
dog['color'] = 'Black & White'
dog['breed'] = 'Shih tzu'
dog['legs'] = 4
dog['age'] = 5
print(dog)

student = {'Name' : 'Edgar', 'Lastname' : 'Maldonado', 'marital_status' : 'Single af'
              , 'country' : 'USA', 'age' : 18, 'skills' : ['Python', 'C++', 'Excel']}
print(len(student))
print(student.values())
print(type(student['skills']))
student['skills'].append('Java') #you can also use extend() or append() method to add one or more skills
print (student['skills'])
print(list(student.keys())) #converts the keys to a list
print(student.keys()) #gets the keys of the dictionary
print(student.values()) #gets the values of the dictionary

student_tuples = list(student.items())
print(student_tuples)
print(type(student_tuples)) #shows that the items were converted to a list of tuples

print(student)
del [student['age']] #deleting the age of 'student'
print(student)

#delete one of the dictionaries
del student
#prints an error because the dictionary no longer exists
#print(student)

print('\n********** END OF DAY 8 ***********\n')