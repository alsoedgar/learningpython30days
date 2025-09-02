#Day 9 of 30 day python challenge

print('\n********** day 9 ***********\n')
print('Conditionals!!!\n')

#by default python scripts are executed sequentially
#from top to bottom, if processing logic requite
#the sequential flow can be altered by
#Conditional execution or Repetitive Execution

#if condition
#in python and other programming languages the keyword
#if is used to check if a condition is true

'''if condition;
    this part of the code runs for truthy conditions
'''

#example

a = 3
if a > 0:
    print('A is a positive number')

#If else
#if condition is true the first block will be executed
#if not the "else" block will be executed

#syntax
'''
if condition:
    this part of the code runs for truthy conditions
else:
    this part of the code runs for falsy conditions
'''

a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')

#If elif else
#We use elif when we have multiple confitions
#syntax
'''
if condition1:
    code
elif condition2:
    code
else:
code
'''

a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')

#Short Hand

#syntax
#code if condition else code

a = 3
print ('A is positive') if a > 0 else print ('A is negative or zero')

#Nested conditions
#syntax
'''
if condition:
    code
    if condition:
    code
'''

a = 0

if a > 0 :
    if a % 2 == 0:
        print ('A is a positive even number')
    else:
        print ('A is a positive number')
elif a == 0 :
    print ('A is zero')
else:
    print ('A is a negative number')

#We can avoid writing a nested condition by
#using logical operators
#and, or, not

#syntax
'''
if condition and condition:
    code
'''
a = int(input('give an integer:'))


if a > 0 and a % 2 == 0:
    print ('A is a positive even number')
elif a >0 and a % 2 != 0:
    print ('A is a positive number')
elif a == 0 :
    print ('A is zero')
else:
    print ('A is a negative number')

#if and or logical operators
'''
syntax
if condition or condition:
    code
'''

user = 'James'
access_level = 3
if user == 'Admin' or access_level >= 4:
    print ('You have full access')
else:
    print('Access denied :(')

#EXERCISES

age = int(input('Enter your age: '))
if age >= 18:
    print('You are old enough to drive')
else:
    print(f'You need {18 - age} more years to drive')

age = int(input('Enter your age: '))

if age == 18:
    print('You are the same age as me')
elif age < 18:
    diff = 18 - age
    if diff == 1:
        print(f'You are 1 year younger than me')
    else:
        print(f'You are {diff} years older than me')
else:
    diff = age - 18
    if diff == 1:
        print(f'Youu are 1 year older than me')
    else:
        print(f'You are {diff} years older than me')

numOne = int(input('Enter a number: '))
numTwo = int(input('Enter a number: '))
if numOne > numTwo:
    print(f'{numOne} is greater than {numTwo}')
elif numOne < numTwo:
    print(f'{numOne} is smaller than {numTwo}')
else:
    print(f'{numOne} is the same as {numTwo}')

grades = int(input('Enter your score: '))
if grades >= 80 and grades <= 100:
    print('A')
elif grades >= 70 and grades < 80:
    print('B')
elif grades >= 60 and grades < 70:
    print('C')
elif grades >= 50 and grades < 60:
    print('D')
elif grades >= 0 and grades < 50:
    print('F')

seasonChoice= input('Enter month: ').lower()
winter = ['December', 'January', 'February']
spring = ['March', 'April', 'May']
summer = ['June', 'July', 'August']
autumn = ['September', 'October', 'November']

if seasonChoice in [seasonChoice.lower() for seasonChoice in winter]: #checking for lowercase so all cases for inputs work
    print('Winter')
elif seasonChoice in [m.lower() for m in spring]:
    print('Spring')
elif seasonChoice in [m.lower() for m in summer]:
    print('Summer')
elif seasonChoice in [m.lower() for m in autumn]:
    print('Autumn')
else:
    print('Not a month')

fruits = ['banana', 'orange', 'mango', 'lemon']
userInput = input('Enter a fruit: ').lower()
if userInput in [f.lower() for f in fruits]:
    print('That fruit already exists in the list')
else:
    fruits.append(userInput)
    print(fruits)

person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
middleSkill = len(person['skills']) // 2

if 'skills' in person:
    print(person['skills'][middleSkill])
else:
    print('The skill list is empty')

if 'Python' in person['skills']:
    print('They know Python')
else:
    print('They dont know Python')

if all (skill in person['skills'] for skill in ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']):
    print('They are a fullstack developer')
elif 'Node' in person['skills'] and 'Python'in person['skills'] and 'MongoDB' in person['skills']:
    print('They are a backend developer')
elif 'JavaScript' in person['skills'] and 'React' in person['skills']:
    print('They are a front end developer')
else:
    print('Unknown title')

print('\n****************** DAY 9 COMPLETE!!!!!! ***************\n')
