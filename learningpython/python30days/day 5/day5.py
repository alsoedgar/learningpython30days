#day 5 of 30 day python challenge
#LISTSSSS mutable or modifiable ordered collection of items!
print('\n********** day 5 ***********\n')

#how to create a list, 2 ways

list = list()
list = []

fruits = ['banana', 'orange', 'mango', 'lemon']
print('Fruits:', fruits)
print('number of fruits:', len(fruits))
print('first fruit:', fruits[0])
print('last fruit:', fruits[-1])
print('second to third fruit:', fruits[1:3])

#lists can have items of different data types

#you can unpack a list
fruits = ['banana', 'orange', 'mango', 'lemon', 'grapes']
first_fruit, second_fruit, third_fruit, *rest = fruits
print(first_fruit)
print(second_fruit)
print(third_fruit)
print(rest)

#rest prints the rest of the list as a list

#slicing items from a list, you can specift a range
# of positive or negative indexes

fruits = ['banana', 'orange', 'mango', 'lemon', 'grapes']
all_fruits = fruits[0:] #from beginning to end
print(all_fruits)
orange_and_mango = fruits [1:3] #from index 1 to 3 (not including 3)
print(orange_and_mango)

#using negative indexing starts the order in reverse, annd can also be used in slicing
reversed_fruits = fruits[::-1]
print(reversed_fruits)

#modifying list items
#lists are mutable, meaning you can change them
fruits = ['banana', 'orange', 'mango', 'lemon', 'grapes']
fruits[0] = 'avocado' #changing the first item
print(fruits)
fruits[1] = 'kiwi' #changing the second item
print(fruits)
#change the last item
fruits[-1] = 'tomato'
print(fruits)

print('tomato does exist in the list:', 'tomato' in fruits)

#adding items to a list
#using append method

#syntax
''''
lst = list()
lst.append(item)
print(lst)
'''

fruits = ['banana', 'orange', 'mango', 'lemon', 'grapes']
fruits.append('apple')
print(fruits)
#added apple to the end

#inserting items into a list
#use insert() method to insert a single item
#at a specified index in a list, other items shift to the right

#syntax
'''
lst = ['item 1', 'item 2']
lst.insert(index, item)
'''

fruits = ['banana', 'orange', 'mango', 'lemon', 'grapes']
fruits.insert(2,'apple') #insert apple between orange and mango
print(fruits)

#removing items from a list
#use remove() method to remove a specified item
fruits.remove('banana')
print(fruits) #removes banannananna

#use pop() method to remove an item by index

#syntax
'''
lst= ['item 1', 'item 2']
lst.pop(index) #if no index is specified, removes the last item
'''

fruits = ['banana', 'orange', 'mango', 'lemon', 'grapes']
fruits.pop()
print(fruits) #removes grapes

fruits.pop(1)
print(fruits) #removes second item on list aka BANANNAANANNA

#removing items using Del
#syntax

'''
lst = ['item 1', 'item 2']
del lst[index] #if no index is specified, removes the entire list
'''

print('\n')
fruits = ['banana', 'orange', 'mango', 'lemon', 'grapes']
print(fruits)
del fruits[0] #deletes the first item
print(fruits)
del fruits[2:3] #deletes the third to fourth item
print(fruits)
del fruits #deletes the entire list
#print(fruits) #this will raise an error since the list no longer exists

#clearing the list
#use clear() method to empty the list
fruits = ['banana', 'orange', 'mango', 'lemon', 'grapes']
print('\n')
print(fruits)
fruits.clear()
print(fruits) #prints an empty list

#copying a list
#you can reassign it to a new variable, such as list1=list2
#but this will make both variables point to the same list, so if you change one,
#the other will also be changed
#use copy() method to copy a list to another list
#syntax
'''
lst = ['item 1', 'item 2']
lst_copy = lst.copy()
print(lst_copy)
'''

fruits = ['banana', 'orange', 'mango', 'lemon', 'grapes']
fruits_copy = fruits.copy()
print('\n')
print(fruits_copy)

#joining lists
#you can use + operator to join two or more lists
#to join or concatenate two lists
#syntax
'''
lst1 = ['item 1', 'item 2']
lst2 = ['item 3', 'item 4']
joined_lst = lst1 + lst2
print(joined_lst)
'''

positive_numbers = [1, 2, 3]
zero = [0]
negative_numbers = [-3, -2, -1]
integers = positive_numbers + zero + negative_numbers
print('\n')
print(integers)

#you can also use extend() method to join two lists
#syntax
'''
lst1 = ['item 1', 'item 2']
lst2 = ['item 3', 'item 4']
lst1.extend(lst2)
print(lst1)
'''
num1=[1, 2, 3]
num2=[4, 5, 6]
num1.extend(num2)
print(num1) #appends the second list to the first list, extends it if you will >:)
print('\n')

#counting items in a list
#use count() method to count the number of occurrences of an item in a list
#syntax
''' 
lst = ['item 1', 'item 2', 'item 1']
count = lst.count('item 1')
print(count)
'''

fruits = ['banana', 'orange', 'mango', 'lemon', 'grapes']
print('number of banana\'s:', fruits.count('banana')) #counts how many times banana appears in the list
print('\n')

#finding index of an item in a list
#use index() method to find the index of an item in a list
#finds first occurrence
#syntax
'''
lst = ['item 1', 'item 2', 'item 3']
index = lst.index('item 2')
print(index)
'''

fruits = ['banana', 'orange', 'mango', 'lemon', 'grapes']
print(fruits.index('orange'))

#reversing a list
#use reverse() method to reverse the order of a list
#syntax
'''
lst = ['item 1', 'item 2', 'item 3']
lst.reverse()
print(lst)
'''

fruits = ['banana', 'orange', 'mango', 'lemon', 'grapes']
print('\n', fruits)
fruits.reverse()
print(fruits)

#sorting a list
#use sort() method to sort the items of a list in ascending or descending order
#if you sort names, it will sort them in alphabetical order
#syntax
'''
lst = ['item 3', 'item 1', 'item 2']
lst.sort() #for ascending order
print(lst)
lst.sort(reverse=True) #for descending order
print(lst)
'''

fruits = ['banana', 'orange', 'mango', 'lemon', 'grapes']
print('\n', fruits)
fruits.sort()
print(fruits)

print('Now in descending order:')
fruits.sort(reverse=True)
print(fruits)

ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.sort(reverse=True)
print(ages)

print('\n')
print('********** EXERCISES ***********')
print('\n')

lst = []
print(list)

lst = ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6']
print(lst)

print(len(lst))

lst = ['item 1', 'item 2', 'item 3', 'item 4', 'item 5', 'item 6']
print(lst[0], lst[2], lst[-1])

mixed_data_types = ['Edgar', 17, '5\'4 tall', 'SINGLE :(', 'Chicago']
print(mixed_data_types)

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[3], it_companies[-1])
it_companies.append('Palantir')
print(it_companies)
it_companies.insert(3, 'Twitter')
print(it_companies)

#Change one of the it_companies names to uppercase (IBM excluded!
it_companies.remove('Palantir')
it_companies[1] = it_companies[1].upper()
print(it_companies)

print('#; '.join(it_companies))

print('GOOGLE' in it_companies) #checking if google is in the list

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
it_companies.sort()
print(it_companies)

it_companies.sort(reverse=True)
print(it_companies)

#slicing the first 3 companies
print(it_companies[0:3])
#slicing the last 3 companies
print(it_companies[-3:])

#slicing the middle company
middle_index = len(it_companies) // 2
print(it_companies[middle_index])

it_companies.pop(middle_index)
print(it_companies)

it_companies.pop(0)
print(it_companies)
it_companies.pop(-1)
print(it_companies)

it_companies.clear()
print(it_companies)

#del it_companies
#print(it_companies) #this will raise an error since the list no longer exists

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

full_stack_copy = full_stack.copy()
full_stack_copy.insert(5, 'Python')
full_stack_copy.insert(6, 'SQL')
print(full_stack_copy)

#list of 10 students ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print('min:', ages[0], 'max:', ages[-1]) #min and max age
print(ages[0] + ages[-1]) #sum of min and max age
average_ages = sum(ages) / len(ages)
print(average_ages)
range_of_ages = ages[-1] - ages[0]
print(range_of_ages)
#Compare the value of (min - average) and (max - average), use abs() method
first_value = abs(ages[0] - average_ages)
second_value = abs(ages[-1] - average_ages)
if(first_value == second_value):
    print('the absolute values are equal')
elif(first_value > second_value):
    print('the absolute value of min - average is greater than max - average')
else:
    print('the absolute value of max - average is greater than min - average')

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
];

print('\nCountries problems:')
print(len(countries))
middle_countries = len(countries) // 2
print('the middle country is:',countries[middle_countries])

if(len(countries) % 2 == 0):
    list_countries1 = countries[:middle_countries]
    list_countries2 = countries[middle_countries:]
    print('list 1:', list_countries1)
    print('list 2:', list_countries2)
else:
    list_countries1 = countries[:middle_countries+1]
    list_countries2 = countries[middle_countries+1:]
    print('list 1:', list_countries1)
    print('list 2:', list_countries2)

#['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries
#and the rest as scandic countries.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
first_country, second,country, third_country, *rest = countries
print('\nfirst three countries:', first_country, second,country, third_country)
print('scandic countries:', rest)
print('\n************* END OF DAY 5 ***********\n')