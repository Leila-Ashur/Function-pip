# Write a program that asks the user to enter their name and age, and
# then prints out a message saying "Hello, [name]! You are [age] years old."
# input:name,age output a sentence

from math import factorial


name="Leila"
age=25
print(f"Hello {name}! You are {age} years old")

# Write a program that uses a loop to print out the numbers from 1 to 10.
count=1
count<=10
count=+1
for count in range(1,11):
    print(count)
    # Write a program that uses a loop to print out the even numbers from 1 to 20.
    
i=1
i<=20
i+1
for i in range(1,20):
    if i%2==0:
        print(i)
# Write a program that calculates the factorial of a number entered by the user.
# def factorial(num):
#     if num==0:
#         return 1
#     else:
#         return num*factorial(num-1)
# if num < 0:
# print("Factorial is not defined for negative numbers.")
# else:
# print(f"The factorial of {num} is {factorial(num)}.")
    

    

        
# Write a program that takes a list of numbers and returns the sum of all the even numbers in the list.
def aditionEven(list):
  
    sum=0
    for i in list:
         if i%2==0:
            sum+=i
    return sum
list=[2,3,1,4,5,6,7,8]
print(aditionEven(list))

# 
def add(list):
    sum =0
    for n in list:
        sum+=n
    return sum
list=[3,5,7,8,9]
print(add(list))

# Write a program that defines a function called "multiply" that takes 
# two numbers as arguments and returns their product.
def multiply(num1,num2):
    return a * b
a=5
b=4
print(multiply({a},{b}))



# Write a program that defines a function called "is_even" that takes a number as
# an argument and returns True if the number is even and False if it is odd.
def is_even(number):
   
    if number % 2 == 0:
        return True
    else:
        return False
numb=3
print(is_even(numb))

# Write a program that defines a function called "reverse_string" that 
# takes a string as an argument and returns the reverse of the string.
def reverse_string(string):
    return string [::-1]

print(reverse_string("leila"))


# Write a program that defines a function called "find_max" that takes a 
# list of numbers as an argument and returns the largest number in the list.
# def find_max(list):
#    list=[4,5,6,6,4,3,9]
# list.sort()
# print(list[-1])
def find_max(list):
    largenum =list[0]
    for num in list:
        if num > largenum:
            largenum=num
    return largenum

print(find_max([2,3,5,7,9]))      



# def smallest(list):
def smallest(list):
    smaller=list[0]
    for small in list:
        if small<smaller:
            smaller=small
    return smaller
print(smallest([2,7,6,4,9]))  
        
#     # Write a program that imports the "math" module and uses the "sqrt" function 
#     # to calculate the square root of a number entered by the user.
# import math


# # Ask user for input
# number = float(input("Enter number"))

# # Calculate square root using math.sqrt function
# sqrt_number = math.sqrt(number)
# number=9

# # Print result
# print(f"The square root of {number} is {sqrt_number}")



# Write a program that asks the user to enter their name and
# age, and then prints out a message saying "Hello, [name]!
# You are [age] years old."
name ="leila"
age=21
print(f"Hello,{name}! You are {age}years old")
# Write a program that uses a loop to print out the 
# numbers from 1 to 10
number=range(1,10)
for num in number:
    print(num)
# Write a program that uses a loop to print out the even numbers 
# from 1 to 20. 
number=range(1,20)
for num in number:
    if num%2==0:
        print (num)
#Write a program that calculates the factorial of a number entered by the user.
# number = int(input(7))
# for i in range(number):
#  print(i)
# Write a program that takes a list of numbers and returns the sum of 
# all the even numbers in the list.

def aditionEven(list):
  
    sum=0
    for i in list:
         if i%2==0:
            sum+=i
    return sum
list=[2,3,1,4,5,6,7,8]
print(aditionEven(list))
# Write a program that defines a function called "multiply" that takes 
# two numbers as arguments and returns their product.
def multiply(num1,num2):
    return a * b
a=5
b=4
print(multiply({a},{b}))

# Write a program that defines a function called "is_even" that takes
# a number as an argument and returns True if the number is even and False 
# if it is odd.
def is_even(number):
    
        if num%2==0:
            return True
        else :
             return False
number=7
print(is_even(number))  

#Write a program that defines a function called "reverse_string" that takes a
# string as an argument and returns the reverse of the string.   
def reverse_string(School): 
    return School[::-1]
text=reverse_string("union")
print(text)
# Write a program that defines a function called "find_max" 
# that takes a  list of numbers as an argument and returns the 
# largest number in the list.
def findmax(list):
    largenum =list[0]
    for num in list:
        if num > largenum:
            largenum=num
    return largenum

print(find_max([2,3,5,7,9]))      

# define a function that accepts a string as input and uses the for 
# for loop to iterrate through the string and count the vowels
def count_vowels(string):
    vowels="a,e,i,o,u"
    count= 0
    for char in string:
        
        if char in vowels :
            count +=1
    return count
            
string = "HelloA"
num_vowels = count_vowels(string)
print( num_vowels)










 
    
       
        
        
        
