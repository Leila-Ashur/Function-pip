
# Write a Python program to sum all the items in a list.



def addition(list):
    sum =0
    for x in list:
        sum+=x
    return sum
list=[3,6,55,7,44,33,65]
print(addition(list))


#  Write a Python program to find the largest number in a list.
my_list = [3, 9, 2, 5,  1]
largest_number = my_list[0]

for item in my_list:
    if item > largest_number:
        largest_number = item
        print(largest_number)
        # 
def largest(list):
    largest_number=list[0]
    for item in list:
      if item>largest:
          largest=item
          print(largest)
          list
        
        

#    Write a Python program to find the smallest number in a list.  

list=[34,76,89,90,43,8]
smallest=list[0]
for item in list:
    if item<smallest:
        smallest = item
print (smallest)

        # for loop
def  find_smallest_num(lst):
   
    smallest = lst[0]

    for num in lst:
        if num < smallest:
            smallest = num  

    return smallest


my_list = [5, 3, 8, 1, 9, 2]
smallest_num = find_smallest_num(my_list) 
print(smallest_num)  

#  Write a Python program to remove duplicates from a list.
new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)

# Print the new list
print(new_list)
my_list=[23,54,21,34,21,67,23,34]


#  Write a Python program to check if a list is empty.
my_list = []

if not my_list:
    print("The list is empty.")
else:
    print("The list is not empty.")
    
    # Write a Python program to reverse a list.
    
my_list=[1,43,76,98,21]
my_list.reverse()
print(my_list)

#  Write a Python program to count the number of occurrences
# of an item in a list.

my_list=[3,3,3,3,65,5,6]
count=my_list.count(3)
print(count)

   
   
       
    
  

    




