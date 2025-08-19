#day 2 of 30 day python challenge

#just exploring types

first_name = 'Edgar'
last_name = 'Maldonado'
full_name = 'Edgar Maldonado'
country = 'USA'
city = 'Chicago'
age= 17
year= 2025
is_married= False
is_true= 1
is_light_on= True
favorite_foods=['pizza','tacos','steak']

#saying what type of var

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(favorite_foods))

#comparing length of user inputted first & last name
print(len(first_name))
print(len(last_name))
if len(first_name) > len(last_name):
        print('your first name has more letters than your last')
else:
    print('your last name has more letters than your first\n')

#different mth equations with operands

num_one=5
num_two=4

num_total= num_one+num_two
print(num_total)

num_different=num_one-num_two
print(num_different)

num_multiple=num_one*num_two
print(num_multiple)

num_division=num_two/num_one
print(num_division)

num_mod=num_one%num_two
print(num_mod)

num_floordiv=num_one//num_two
print(num_floordiv)

#radius of a circle = 30m
r = float(input('Enter a radius!: '))

area_of_circle=(3.14 * r) ** 2
print('area=',area_of_circle, 'm')
circum_of_circle= (2 * 3.14) * r
print('circum=', circum_of_circle, 'm')

#Use the built-in input function to get first name, last name
#country and age from a user and store the value to their corresponding variable names

first_name= input('Enter your first name: ')
last_name= input('Enter your last name: ')
country= input('Enter your country: ')
age= input('Enter your age: ')

print(first_name + ' ' + last_name)
