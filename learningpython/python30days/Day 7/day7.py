#day 7 of 30 days of python
print('\n********** day 7 ***********\n')

print('Sets!!!\n')

#Set is a collection of items
#unordered
#unindexed
#no duplicate values
#possible to find the union, intersection, difference, symmetric difference
#subset, super set and disjoint set among sets
#defined by curly braces or the set() function

#creating an epmty set
#st = set()

#or

st = {'item1', 'item2', 'item3'}
print(st)

#similarly to other collections, we can use len() to find the length of a set
print(len(st))

#accessing items in a set
#we use loops to access items, we will see this later in the loop section

#check if an item exists, we use 'in' keyword
#syntax
st = {'item1', 'item2', 'item3'}
print('item1' in st)

#adding items to a set
#once we cannot change any items, and we can also add additional items
#add using add() method

#syntax
st = {'item1', 'item2', 'item3'}
st.add('item4')
print(st)

#adding multiple items in sets
#use update() method to add multiple items to a sit
#takes a list, tuple, set or dictionary as an argument
#syntax
st = {'item1', 'item2', 'item3'}
st.update(['item4', 'item 5', 'item 6'])
print(st)

#you can also use a tuple or another set with update()
fruits = {'apple', 'banana', 'cherry'}
vegetables = ('carrot', 'lettuce', 'onion')
fruits.update(vegetables)
print(fruits)

#removing items from a set
#use remove()
#if the item is not found remove() will raise an error
#you can also use discard()method
#this method does not raise an error if the item is not found
#syntax
st = {'item1', 'item2', 'item3'}
st.remove('item1')
print(st)

#pop() method
#this removes a random item from a set, unlike other collections because there is no index
#syntax
st = {'item1', 'item2', 'item3'}
item = st.pop()
print(st)
print(item)
#it will print the set with one random item removed, and printing item
#will show the removed item

#clearing items in a set
#use the clear() method to empty the set
#syntax
st = {'item1', 'item2', 'item3'}
st.clear()
print(st) #prints empty set

#deleting a set
#to delete the set completely use the del keyword
#syntax
st = {'item1', 'item2', 'item3'}
del st
#print(st) #this will raise an error because the set no longer exists

fruits = {'apple', 'banana', 'cherry'}
del fruits

#converting a list to set, and a set to a list
#converting list to set removes duplicates and only unique items will be stored

#syntax
fruits_list = ['apple', 'banana', 'cherry', 'apple', 'banana']
print(fruits_list)
print(type(fruits_list))
fruits_set = set(fruits_list)
print(fruits_set)
print(type(fruits_set))
fruits_set = list(fruits_list)
print(fruits_set)
print(type(fruits_set))

#joining sets
#we can use union() method or update() method (or the '|' operator)
#union: This method returns a new set with all items from both sets
#update: This method inserts all the items from one set to another
#syntax
st1 = {'item1', 'item2', 'item3'}
st2 = {'item4', 'item5', 'item6'}
st3 = st1.union(st2)
print(st3)

#syntax
st1 = {'item1', 'item2', 'item3'}
st2 = {'item4', 'item5', 'item6'}
st1.update(st2)
print(st1)
#here the union made a whole new set, while update added the items of st2 to st1

#finding the intersection of two sets
#this returns a set of items which are in both sets
#we can use intersection() method or the '&' operator
#syntax
st1 = {'item1', 'item2', 'item3'}
st2 = {'item2', 'item3', 'item4'}
st3 = st1.intersection(st2)
print(st3)

#checking subset and super set
#a set can be a subset or super set of other sets
#a subset means that all items from a list, are contained in a second set
#a super set means that a set contains all items from another set
#if A is a subset of B, then B is a super set of A
#subset: issubset() method
#super set: issuperset() method
#syntax
st1 = {'item1', 'item2', 'item3'}
st2 = {'item1', 'item2'}
print(st2.issubset(st1)) #true
print(st1.issuperset(st2)) #true

#checking the difference between two sets
#reutrns the difference between two sets

#syntax
st1 = {'item1', 'item2', 'item3', 'item 4'}
st2 = {'item2', 'item3'}
print(st2.difference(st1)) #this deletes the items from st1 that are also in st2, which leaves none left (empty set)
print(st1.difference(st2)) #this deletes the items from st2 that are also in st1, which leaves item1 and item4

#finding symmetric difference between two sets
#it returns the symmetric difference of two sets as a new set
#it means that it returns a set that contains all items
#from both sets, except items that are present in both sets
#basically it creates a set with items that are NOT in both sets
#mathmatically it is represented as A Δ B
#we can use symmetric_difference() method or the '^' operator
#syntax
st1 = {'item1', 'item2', 'item3'}
st2 = {'item2', 'item3', 'item4'}
st3 = st1.symmetric_difference(st2)
print(st3) #prints item1 and item4, because they are not in both sets

#joining sets
#if two sets do not have a common item, or items, we call them disjoint sets
#we can check if two sets are disjoint using isdisjoint() method
#syntax
st1 = {'item1', 'item2', 'item3'}
st2 = {'item4', 'item5', 'item6'}
st2.isdisjoint(st1)
print(st2.isdisjoint(st1)) #prints true because there are no common items
#it prints true, because they are not joined sets, they do not have commen items

print('\n************* EXERCISES *************\n')

# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['Meta, Tesla, IBM']) #adding multiple companies
print(it_companies)
it_companies.remove('Twitter')
print(it_companies)
#difference between remove is that remove will tell
#you if the item you are trying to remove is not found
#discard will NOT tell you if the item is not found
#it_companies.discard('Twitter') #this will NOT raise an error even though Twitter

#EXERCISE 2

A.union(B) #joining A and B
print(A.union(B))

A.intersection(B)
print(A.intersection(B))

A.issubset(B)
print('is A a subset of B:', A.issubset(B))

A.isdisjoint(B)
print('Is a disjoint from B:', A.isdisjoint(B))

A.union(B)
B.union(A)
print(A.union(B) == B.union(A)) #true, because union is commutative

A.symmetric_difference(B)
print(A.symmetric_difference(B)) #prints the items that are NOT in both sets

del A
del B

#EXERCISE 3

set_ages = set(age)
print(len(set_ages)) #prints the ages without duplicates
print(len(age))

#the length of the list is 8, but the length of the set is 5
#length of list is bigger

#string is a collection of characters, it immuutable, has an index, and it is ordered
#a list is a collection of items, it is mutable, has an index, and it is ordered
#a tuple is a collection of items, it is immutable and is ordered
#a set is a collection of unique items, it is unordered, unindexed, and mutable

#I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
sentence = 'I am a teacher and I love to inspire and teach people.'
set_sentences = set(sentence.split())
print(set_sentences)
print('there are: ', len(set_sentences), 'unique words in the sentence')

print('\n********** END OF DAY 7!!! ***********\n')