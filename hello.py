# print Hello World
print ("Hello, World!")

# set variable myNumber to integer and print variable
myNumber = 10
print(myNumber)

# set variable myFloater to float integer and print variable
myFloater = 9.99
print(myFloater)

# set variable iWantToSayHello to string and print variable
iWantToSayHello = 'Hello!'
print(iWantToSayHello)

#basic addition between two variables that are set to integer values
one = 1
two = 2
three = one + two
print(three)
four = two + two
print(four)

#mix operators -- will throw error
#print(one + two + iWantToSayHello)

#create new list

numberList = []
numberList.append(one)
numberList.append(two)
numberList.append(three)
numberList.append(four)
print(numberList)
print('first index of List is:', numberList[0])
print('first index of List is:', numberList[1])
print('first index of List is:', numberList[2])
print('first index of List is:', numberList[3])

#for loop and print list
for x in numberList:
    print ('For Loop of numberList:', x)

#arithmatic
#addition/subtraction
seven = 1+2+10-6
print(seven)

#division
seven = 35/5
print(seven)

#multiplication
seven = 3.5 * 2
print(seven)

#square
sixteen = 4 ** 2
print(sixteen)

#cubed
twentySeven = 3 **3
print(twentySeven)

#operators with strings

Lili = 'Li' + 'li'
print(Lili)

Lili = ('Li' + 'li' + ' ') * 10
print(Lili)


#opeators with lists

red = ['apples', 'watermelon', 'stop signs']
green = ['grass', 'trees', 'leaves']
combinedList = red + green
print(combinedList)

#String Formatting

firstName = 'Lili'
lastName ='Bourgeois'
print ('Hello, %s %s!' % (firstName, lastName))
print('Hello your first name is {0} and your last name is {1}'.format(firstName, lastName))

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

accountBalance = 100.50
print ('Hello %s %s. Your account balance is: %f' %(firstName, lastName, accountBalance))

#string operations

dogName = 'Winnie'
#number of characters in string
print('Winnie is how many characters long:', len(dogName))

#position of specific character
print('The first occurence of the letter i is at position:', dogName.index('i'))
print('The first occurence of the letter e is at position:', dogName.index('e'))

#slice string
print ("Slice 'inni' from Winnie:", dogName[1:5])

#start at end of string
print ('The second letter from the end of Winnie is:', dogName[-2])
print ('The first letter from the end of Winnie is:', dogName[-1])

#to reverse a string

print ('Reversing Winnie is:', dogName[::-1])

#uppercase
print('Uppercase Winnie is:', dogName.upper())

#lowercase
print('Lowercase Winnie is:', dogName.lower())

#starts with/ends with
print ('Winnie starts with Winn:', dogName.startswith('Winn')) #should return true
print ('Winnie ends with Winn:', dogName.endswith('Winn')) #should return false
print ('Winnie ends with ie', dogName.endswith('ie')) #should return true

#conditions
print (one)
print (one == 1) #should return true
print (one == 2) #should return false
print (one == '1') #should return false
print (one < 10) #should return true
print (one != 2) #should return true

#if statements

if one == 1 and dogName == 'Winnie':
    print('Statements are true')

if 'apples' in red :
    print ('Apples is in list red')

if 'grass' in red :
    print ('Grass is in list red') #will return nothing as this is false


if 'grass' in red:
    print ('Grass is in list red')
elif 'grass' in green:
    print ('Grass is in list green')

if one == 2:
    print('One is equal to 2')
else:
    print('One is not equal to 2')

# the is operator

print (one == 1) #should return true
print (one is 1) #should return false
oneAgain = 1

print (one == oneAgain)#should return true
print( one is oneAgain)# should return true

redAgain = ['apples', 'watermelon', 'stop signs']
print(redAgain == red)
print(redAgain is red)

#for loops
for items in red:
    print (items)

#while loop
count = 0
while count <=10:
    print(count)
    count += 1

count = 10
while count >=0:
    print(count)
    count -=1

#function

def addition_function(a, b):
    return a + b

print('Adding 2 and 4 is:', addition_function(2, 4))
print('Adding 10 and 4 is:', addition_function(10, 4))
