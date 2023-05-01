# Write a Python function that takes two arguments (a and b)
# and returns their sum.
import numbers


def sum_numbers(a,b):
    
    return a+b
a=2
b=4
print (sum_numbers(a,b))

# Write a Python function that takes a string as input and 
# returns the string reversed.:
def reversed_string(School):
    return School[::-1]
school="AkiraChix"
print(reversed_string(school))

# Write a Python function that takes a list of integers as
# input and returns the sum of all the integers in the list.
def sum_of_int(list):
    sum =0
    for num in list:
        sum+=num
    return sum 
    
nums=[7,6,]    
print(sum_of_int(nums))

# Write a Python function that takes a list of integers as
# input and returns a new list with all the even numbers
# removed.
def remove_even_numbers(numbers):
    newArr=[]
    for num in numbers:
        if num % 2 !=0:
            newArr.append(num)
    return newArr

list=[2,3,1,4,5,6,7,8]
print(remove_even_numbers(list))
# Write a Python function that takes a list of integers as
# input and returns the highest value in the list.
def get_highest_value(numbers):
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest
nums = [1, 5, 2, 7, 3, 9]
print(get_highest_value(nums))

# Write a Python function that takes a list of strings as 
# input and returns a new list with all the strings
# capitalized.
def capitalize_strings(name):
    
    return [s.capitalize() for s in names]
    
  
names= ["leila","val","victoria"]
print(capitalize_strings(names))   
   
   
    