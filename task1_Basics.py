

● Create a Boolean variable named x

x = 15
print(bool(x))

if x < 20 :
    print(x)
    


● Create an integer variable named y

y = 15
print(type(y))

● Create a float variable named z


z = 3.5
print(type(z))


● Create a string variable names s


M = "Muhannad"
print(type(M))

● Convert the int variable to float


x = 15
print(float(x))


x = 10 / 4
print(x)



● Can we convert the str to int ?

x = "500"
print(type(int(x)))


● Create a list of numbers from 1 to 5


lista = [1,2,3,4,5]
print(lista)
print(type(lista))


● Create a tuple from 10 to 15


tupla=(10,11,12,13,14,15,)
print(tupla)
print(type(tupla))

● Convert the list to tuple

lista = [1,2,3,4,5]
tuplec = tuple(lista)

print(tuplec)
print(type(tuplec))




● Create a dict of 3 values


dicta = {"Muhannad" :"python" , "Mahmoud" : "django" , "khaled" : "java"}
print(dicta)
print(type(dicta))


● Can we use semi colon ; with python

NO 

● Python is interpreted or compiled ?

interpreted

● What is the differences between low level & high level

low level
---------------------------
the language of the computer 
it consists of 1,0
it easy to be executed
it is  hard to program
can run only of one kind of computer and have to be rewritten to another like C Assembley




High level
------------------
Easy to program
Takes less time to be coded
Easy to be corrected
portable ( only one program can run on any pc )
Like python , java , c# 

● What is the differences between = , ==

x = 5 
valeu for x 


x==5
Question for Python


● What do we mean by using !=

Any number is not equal.


● What is the operator precedence

Operators are used to perform operations on variables and values.

    Arithmetic operators
    Assignment operators
    Comparison operators
    Logical operators
    Identity operators
    Membership operators
    Bitwise operators


● Create a variable x with value of 10

x = 10

● Increase x value by 15 using assignment operators

x = 10
x += 15
print(X)


● Divide the x value by 5 using assignment operators

x /= 5
print(x)

● Multiply the x value by 10 using assignment operator

x *= 10
print(x)

● Get module of x on 3 using assignment operators

x %= 3
print(x)


● Using python print the module of 11 to 4

x = 11
y = 4
print(x % y)

I dont know if it is true or not

● Print the exponent of 2,3

print(2 ** 3)



● Divide 11 by 3 using python division● Can we divide 11 by 3 and get an integer number ?

print(11//3)


● Check if 10 is bigger than 15 or not

x = 10
if 10 > 15 :
    print( "10 > 15 ")


else :
    print("10 less than 15")



● If 10 is not bigger than15 print x is smaller than 15

x = 10

if 10 > 15 :
    print( "10 > 15 ")


else :
    print("x smaller than 15")


● In which cases we will use all

and

● What is the differences between all , and

all : The condition should not be verified

and :The conditions must be verified

● What is the differences between any , or

any

any will return True when at least one of the elements

( or ) :  At least one subexpressions must be true for the compound expression to be considered true



( all ) will return True only when all the elements are True


● If we need all the conditions to be true we will use ….


● What is the differences between if , elif

If the condition  for if is wrong  Here be dealing with elif



● What is the differences between elif else


If the condition of elif are wrong, else is performed


● Can we use more than one elif

yes

● Can we use more than one else

NO

● write s simple ternary operator

x = 100
print(" x < 50") if x < 50 else print(x)


● in elif , python will check all the conditions no matter what ?

If the condition  for if is wrong Here be dealing with elif


● in elif we use else for ... ?

If the condition of elif are wrong, else is performed



● if we have this list [2,4,6,8,10] :

○ check to see if 4 in this list or not


x = [2,4,6,8,10]

if 4 in x :
    print("yes 4 in list")

    
○ check to see if 4 and 6 in this list on not

x = [2,4,6,8,10]

if 4 in x :
    print("yes 4 in list")

if 6 in x :
    
    print("yes 6 in list")

else :
    print(" not found ")


○ check to see if 3 or 6 in this list

x = [2,4,6,8,10]

if 3 in x :
    print("yes 3 in list")

elif 6 in x :
    
    print("yes 6 in list")

else :
    print(" not found ")


○ check to see if 2 , 4 and 5 in this list


x = [2,4,6,8,10]

if 2 in x :
       print("yes 2 in list")


if 4 in x :
       print("yes 4 in list")


      
if 5 in x :
       print("yes 5 in list")
     
    

else :
      print(" 5 not found ")





