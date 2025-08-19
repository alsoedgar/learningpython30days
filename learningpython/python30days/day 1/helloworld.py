#day 1 of 30 day python challenge
import math

print("hello world!.... anyways you see that phrase through every beginning software engineering journey"
      "\njoin me as I learn Python, and watch as I grow and gain experience :)"
      "\nAlso, hello future self! I already know you're looking back at this seeing how far you've come"
"\nThink of this of this as a time capsule, I know you're successful and doing the next big thing :)")

print ('\n********** day 1 ***********\n')
print(3 + 4) #addition
print(3 - 4) #subtractoin
print(3 / 4) #division
print (3 // 4) #floor division (rounds division down to integer)
print (3 * 4) #multiplication
print (3 ** 4) #exponential
print (3 % 4) #modulus (finds remainder)


print("Edgar Maldonado")
print ("Maldonado's")
print ("USA")
print ("I am enjoying 30 days of python")

#checking data types

print (type(10))
print (type(9.8))
print (type(3.14))
print (type(4 - 4j))
print (type(['Asabeneh', 'Python', 'Finland']))
print (type("Edgar Maldonado"))
print (type("Maldonado's"))
print (type("USA"))

#example of different data types: numbers, string, boolean, list, tuple, set, and Dictionary
int = 3
float = 3.14
complex= 6 + 7j

string = 'Edgar Maldonado'
boolean = True
list = ['Edgar', 'Python', 'USA'] #an ordered collection of stored data types
tuple = ('Ducks', 'Horchata', 'Mexico') #ordered collection of stored data types
                                        #BUT immutable, can NOT be changed

#dictionary = unordered collection of data in a key value pair format
{
'first_name': 'Edgar',
'country': 'Mexico',
'age':18,
'skills': ['c++', 'python', 'excel'],
'is_student': True
}

#set = collection of data types, similar to list and tuple, however it is
#NOT ordered and stores only unique items (order is unimportant in a set)
{5.5, 2, 25}


#finding the euclidian distance of (2,3) and (10, 8)
#coordinates
x1, y1 = 2,3
x2, y2= 10,8
#formula
euclidian_distance= math.sqrt((x2-x1)**2 + (y2-y1)**2)
#printing results
print(euclidian_distance)