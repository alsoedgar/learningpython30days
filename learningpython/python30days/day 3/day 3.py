#Day 3 of 30 days of python!

#showing comparison equalities as true/false values
print(3==3)

#showing 'is', 'is not', 'in', 'not in'
print('E in Edgar: ', 'E' in 'Edgar')

#python uses keywords for logical operators, such as
#and, or, not - instead of for example, && and ||

print (not True)
print (not not True)
print ('True or False', True or False)

#EXERCISES!!
#-------------------

age = 17
height = 71.5
var = 8 + 5j


b = input('base = ')
h = input('height = ')
area_triangle = (float(b) * float(h)) * 0.5

#f-string for formatting and good technique (allowing string without concatenation)
#:.2f for formatting of rounding the area to two digits
print(f'The area is {area_triangle:.2f} m')

#rectangle l and w
#l = 2
#w= 10
#rectangle_area = (float(l) * float(w))
#rectangle_perimeter= 2 * l + 2 *w

#l = rectangle_area / (float)l
#w = rectangle_area / (float)w

#l = (rectangle_perimeter - 2 * w) /2

#find slope. x-intercept, and y-int
#y=2x-2
#slope = m = 2, x-int = -2, y-int = 1

#(2,2), (6,10)
x1, y1 = 2, 2
x2, y2 = 6, 10

slope =  (y2 - y1) / (x2 -x1)
print(f'your slope is {slope:.2f}')

if slope > 2:
    print(f'exercise 9s slope is greater than 2')
elif slope < 2:
    print(f'exercise 9s slope is less than 2')
else:
    print(f'exercise 9s slope is equal to exercise 8')

#checking if 'python' and 'dragon' have the same length
print(len('python'), len('dragon'))
print(len('python') == len('dragon'))

##checking if 'on' is in both 'python' and 'dragon'
print('on' in 'python' and 'on' in 'dragon')

print('jargon' in 'I hope this course is not full of jargon')

#Find the length of the text python and convert the value to float and convert it to string
print (str(float(len('python'))))

#checking even vs odd
n = 7
print('even' if len('pythons') % 2 == 0 else 'odd')

#Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
print(7//3 == 2.7)

#Check if type of '10' is equal to type of 10
print(type('10') == type(10))

#Check if int converted value of '9.8' is equal to 10
print(int(float('9.8')) == 10)

#pay calculator
hours_worked = input('Hours Worked:')
hourly_rate=input('Hourly Rate:')
pay = float(hours_worked) * float(hourly_rate)

print(f'Your pay is ${pay:.2f}')

print('Enter your age:')
age = int(input())
age_in_seconds = age * 60 * 60 * 24 * 365
print(f'You have lived for {age_in_seconds} seconds')

#write a script that displays this table
#1 1 1 1 1
#2 1 2 4 8
#3 1 3 9 27
#4 1 4 16 64
#5 1 5 25 125

#using a for loop with a range making n's range 1-5
for n in range (1, 6): print((n),(n**0),(n**1),(n**2),(n**3))