#day 4 of 30 day python challenge

#multiline string '''blah blah blah '''

print('\n********** day 4 ***********\n')

#string concatenation
first_name = 'Edgar'
last_name = 'Maldonado'
space = ' '
full_name= first_name+ space + last_name
print(f'hello {full_name}!')

# \ backslashes are used for escape sequence
# # \n is used to create a new line
# # \t is used to create a tab space
# # \\ is used to print a backslash
# # \' is used to print single quote
# # \" is used to print double quote
# -for example-

print('\tHi this is Edgar\nI am 17 years old'
      '\\ this is a backslash\n'
      'how\'s it going?\n'
      'The doctor said \"you\'re way too awesome\"')

#old formatted variables, python uses % to format
# %s for strings, %d for integers, %f for float, and %.(number of digits)f for float with specific
#decimal places

name = 'edgar'
age = 17
height=71.5
print('My name is %s. I am %d years old. My height is %.2f inches' % (name, age, height))

#NEW formatting style introduced in python version 3
#format
name = 'edgar'
age = 17
height=71.5
formated_string = 'My name is {}, I am {} years old. My height is {} inches'.format(name, age, height)
print(formated_string)

number=4.2345
print('The number formatted in the new way, rounding to two decimal places is {:.2f}'.format(number))

#string interpolation (f-strings)
#put ' f' before the string and use {} to insert variables

f_string = 'inserting this into the print statement'
print (f'look how easy it is {f_string}')

#accessing characters in a string
#strings are indexed, starting at 0, so the first character is at index 0
#and the last character is at index -1
language = 'python'
print(language[0], '\n') #this prints first character 'p'

for char in language:
    print(char) #this prints each character in the string on a new line


#slicing strings
print(language[:3],'\n',language[-3:])

#reversing a string is super easy
reverse_sentence = 'Hello, World! Look how trippy this is!'
print(reverse_sentence[::-1])

#skipping characters in a string
#use the first number to start at, the second number to stop at, and the third number to skip
print(language[0:6]) #this prints the first 6 characters in the string
print(language[0:6:2]) #this prints every second character in the string
print(language[0:6:3]) #this prints every third character in the string

#string METHODS!

basic_sentence = 'i am enjoying 30 days of python'
print(basic_sentence.capitalize()) #this capalizes the first letter of the string

sentence = 'thirty days of python!'
print(sentence.count('y')) #this counts the numbers of tiemes 'y' appears in the string

print(sentence.endswith('on!')) #checks if the string ends with 'on!'
print(sentence.endswith('butt')) #checks if the string ends with 'on'

sentence_with_tabs = 'thirty\tdays\tof\tpython!'
print(sentence_with_tabs.expandtabs()) #this expands the tabs in the string to spaces
print(sentence_with_tabs.expandtabs(10)) #this expands the tabs in the string to x amount of spaces

print(sentence.find('days')) #this finds the index of the first occurrence of 'days' in the string
print(sentence.find('y')) #this finds the index of the first occurrence of 'y' in the string
print(sentence.find('butt')) #this returns -1 if 'butt' is not

print(sentence.rfind('y')) #this finds the LAST occurrence of 'y' in the string

#format() format strings into a nicer input

#.index() finds the index of the lowest index of a substring in a string
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7

#.rindex() finds the index of the highest index of a substring in a string
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.rindex(sub_string))  # 7
print(challenge.rindex('on', 8)) # 19

#.isalnum() checks if all characters in the string are alphanumeric (letters and numbers)
print(challenge.isalnum()) #false because of spaces
print('thirtydays'.isalnum()) #true because all characters are letters and numbers
print('thirtydays123'.isalnum()) #true because all characters are letters and numbers

#using .isalnumeric to make a password
"""print('Make a password for your account!\nRequirements:\n'
      '-Must be at least 8 characters long\n'
      '-Must be alphanumeric (letters and numbers only)\n'
      '-No special characters allowed!')

password = input('Enter a password: ')
while len(password) < 8 or not password.isalnum():
    print('Invalid password! Please try again.')
    password = input('Enter a VALID password: ')
else: print('Nice password! You are all set up!')"""""

#.isalpha() checks if all characters in the string are letters
print(challenge.isalpha()) #false because of spaces
print('thirtydays'.isalpha()) #true because all characters are letters

#.isdecimal() checks if all characters in the string are decimal numbers
#.isdigit() checks if all characters in the string are digits
#.isnumeric() checks if all characters in the string are numeric characters

#.isidentifier() checks if the string is a valid python identifier (correct variable name, cant
# start with a number and no special characters except _)

#.islower() checks if ALL characters in the string are lowercase
challenge = 'thiry days of python'
print(challenge.islower()) #true because all characters are lowercase
challenge = 'thiry days of Python'
print(challenge.islower()) #changes bc of the P in Python

#.isupper() checks if ALL characters in the string are uppercase
challenge = 'thiry days of python'
print(challenge.isupper()) #false because all characters are lowercase
challenge = 'THIRTY DAYS OF PYTHON'
print(challenge.isupper()) #true because all characters are uppercase

skills = ["C++", "Python", "Excel"]
result = ' '.join(skills)
print(result)
#this joins the list of skills into a string with spaces in between

#.strip() removes all given characters from the beginning and end of the string
print('   hello world   '.strip()) #removes spaces from beginning and end of string
print('---hello world---'.strip('-')) #removes dashes from beginning and end

# .replace() replaces all occurrences of a substring with another substring
phrase = '30 days of python!'
print(phrase.replace('python', 'CODING!')) #replaces 'python' with 'CODING!'

#.split() splits the string into a list of substrings based on a given delimiter
challenge = 'thirty days of python'
print(challenge.split()) # ['thirty', 'days', 'of', 'python']
challenge = 'thirty, days, of, python'
print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']

# .title() capitalizes the first letter of each word in the string (making it a title)
challenge = 'thirty days of python'
print(challenge.title())

#.swapcase swaps the case of all characters in the string, capital to lower and vise-versa
challenge = 'Thirty Days Of Python'
print(challenge.swapcase()) #THIRTY DAYS OF PYTHON

#.startswith() checks if the string starts with a given substring
print(challenge.startswith('Thirty')) #true because the string starts with 'Thirty'
print(challenge.startswith('thirty')) #false because the string starts with 'Thirty'

print('----------exercises-----------\n')





