#DAY 6 OF 30 DAY PYTHON CHALLENGE

print('\n********** day 6 ***********\n')


#tuples!
#a tuple is a collection of different data types, which is ordered and
#immutable (cannot be changed)
#tuples are defined by parentheses
#example of a tuple

empty_tuple = tuple()
print(empty_tuple)

thistuple = ('apple', 'banana', 'cherry')
print(thistuple)
print(type(thistuple))

#use len() to find the length of a tuple
print(len(thistuple))

#access tuple items by index
print(thistuple[1]) #banana gets second item
print(thistuple[-1]) #cherry gets last item

#slicing a tuple
#syntax
tpl = ('item1', 'item2', 'item3', 'item4', 'item5')
all_items = tpl[0:4] #gets items from index 0 to 3
all_items = tpl [0:] #gets items from index 0 to 3
middle_two_items = tpl[1:3] #gets items from index 1 to 2

#changing tuples to lists and vice versa
#tuples are immutable, so to change them we can convert them to a list
#syntax
fruits = ('apple', 'banana', 'cherry')
fruits = list(fruits) #convert to list
fruits[0] = 'kiwi' #change first item
print(fruits)
print(type(fruits))
fruits = tuple(fruits) #convert back to tuple
print(fruits)
print(type(fruits))

#check if item exists in tuple
#we can check using 'in' it returns a boolean
#syntax
tpl = ('item1', 'item2', 'item3')
print('item2' in tpl) #returns True

fruits = ('apple', 'banana', 'cherry')
print('apple' in fruits) #true
print('kiwi' in fruits) #false
#fruits[0] = kiwi #TypeError: 'tuple' object does not support item assignment

#joining a tuple to another tuple
#use the '+' operator

#syntax
tpl1 = ('item1', 'item2')
tpl2 = ('item3', 'item4')
tpl3 = tpl1 + tpl2
print(tpl3)

#Deleting Tuples
#It is not possible to remove a single item in a tuple, but it
#is possible to delete the tuple itsel fusing del keyword
#syntax
tpl1 = ('item1', 'item2', 'item3')
del tpl1
#print(tpl1)
#this will raise an error because the tuple no longer exists

print('\n******************EXERCISES******************\n')

empty_tuple = tuple()
sisters = ('Natalie', 'Naomi')
brothers = ('Omar', 'randombrother')
siblings = sisters + brothers
print(siblings)
print(len(siblings))
family_members = siblings + ('Luz', 'Edgar Sr.')
print(family_members)

#Unpack siblings and parents from family_members
#unpacking would be similar to slicing, but we would be assigning
#the values to different variables
#syntax

siblings_unpack, parents_unpack= family_members[0:4], family_members[4:]
print('Siblings: ', siblings_unpack,'Parents: ',parents_unpack)

fruits = ('apple', 'banana', 'cherry')
vegetables = ('carrot', 'lettuce', 'pepper')
animal_products = ('milk', 'meat', 'cheese')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
middle_item = len(food_stuff_tp)/2
print(food_stuff_tp[int(middle_item)])
print('first three: ', food_stuff_tp[0:3], 'last three: ', food_stuff_tp[-3:])
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)

print('\n********** end of day 6!!!!!!!! ***********\n')