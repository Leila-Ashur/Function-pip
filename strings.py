#  Given the variables name and age, how can you format a
#  string to print "My name is John and I am 30 years old."?
name = "john"
age = 30
print(f"My name is {name} and iam {age} years old")


    # Given the variables num1, num2, and result, how can you format a string to print 
    # "The result of adding 5 and 10 is 15."?
num1=5
num2=10
result = num1+num2
print(f"The result of adding {num1} and {num2} is {result}.")


    # Given the variable pi, how can you format a string to print "The value of pi is 3.14159."
PI=3.14159
print(f"The value of PI is {PI} ")

# Given the variables item and price, how can you format a string to print "The price of a banana is $0.99."?
cash=0.99
item="Banana"
print(f"The price of a {item} is ${cash} ")

# Given the variables first_name, last_name, and city, how can you format a string to print
# "My name is John Smith and I live in New York City."?
first_name="John"
last_name="Smith"
city="New York "
print(f"My name is {first_name} {last_name} i live in {city} city ")

# Given the variable num, how can you format a string to print "The number is 5." with
# a minimum field width of 10 characters?
digit =5
print((f"The number is {digit:>10}"))

# Given the variable num, how can you format a string to print "The number is 5.00." with 
# a precision of 2 decimal places?
double=5.00
print(f"The number is {double:.2f} ")

# Given the variables num1, num2, and result, how can you format a string to print "The result of dividing 10 by 3 is 3.33." 
# with a precision of 2 decimal places?
num1=10
num2=3
result=num1/num2

print(f"The result of dividing {num1} by {num2} is {result:.2f} ")



# Given the variable sentence, how can you format a string to print "The quick brown fox jumped over the lazy dog." 
# with the first letter of each word capitalized?

sentence="The quick brown fox jumped over the lazy dog"
detail =sentence.title()
print(detail)


# Create a variable age and assign it the value 30. Convert the value to a string and concatenate 
# it with  the string " years old". Print out the resulting string.
age=30
string =str(age)+"years old"
print(string)


