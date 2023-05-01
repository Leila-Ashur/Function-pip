# # Write a Python program that takes in alist of tuples, where each tuple 
# # represents a book and its price.The program should find the book with the 
# # highest price and print out its title.
# def highestbook(tuple):
#     books =[("book1",300),("book2",545),("book3",400)]
#     # initialize max price and max title
#     max_price = books[0][1]
#     max_title = books[0][0]

# # Iterate through the rest of the list of books and update max_price and max_title if a higher price is found
# books = [("Book A", 15.99), ("Book B", 10.99), ("Book C", 19.99), ("Book D", 8.99)]

# # Initialize max_price and max_title to the first book in the list
# max_price = books[0][1]
# max_title = books[0][0]

# # Iterate through the rest of the list of books and update max_price and max_title if a higher price is found
# for book in books[1:]:
#     if book[1] > max_price:
#         max_price = book[1]
#         max_title = book[0]
    
        
#         print(f"The book with the highest price is '{max_title}' at ${max_price:.2f}")
# # Write a Python program that takes in a list of tuples, where each tuple 
# # represents a person's name, age, and salary. The program should
# #calculate and print out the average salary for people in each age group (
#     people = [("Alice", 25, 40000), ("Bob", 30, 50000), ("Charlie", 25, 45000), ("David", 35, 60000), ("Eve", 30, 55000)]

# #  store the total salary and count for each age group
# age_groups = {}

# # Iterate through the list of people, updating the total salary and count for each age group
# for person in people:
  
#     age = person[1]
#     salary = person[2]
# if age in tuple:
#         tuple[age]["total_salary"] += salary
#         tuple [age]["count"] += 1
# else:
#         tuple [age] = {"total_salary": salary, "count": 1}
#         # Calculate and print out the average salary for each age group
# for age, data in tuple.items():
#     avg_salary = data["total_salary"] / data["count"]
#     print(f"Average salary for age {age}: ${avg_salary:.2f}")
    
    
#     # Write a Python program that takes in a list of tuples, where each tuple
#     # represents a student and their scores on two exams. The program should 
#     # calculate and print out the average score for each student, and determine
#     # which student had the highest overall score.
    
#     student=[("Alice", 85, 90), ("Bob", 75, 80), ("Charlie", 90, 95), 
#              ("David", 80, 85), ()]
# average_scores = {}

# # Initialize max_score and max_student to the first student in the list
# max_score = sum(students[0][1:]) / 2
# max_student = students[0][0]

# # Iterate through the list of students, calculating the average score for each student and updating max_score and max_student if a higher score is found
# for student in students:
#     name = student[0]
#     score1 = student[1]
#     score2 = student[2]
#     avg_score = (score1 + score2) / 2
#     average_scores[name] = avg_score
#     if avg_score > max_score:
#         max_score = avg_score
#         max_student = name

# # Print out the average score for each student and the student with the highest overall score
# for name, score in average_scores.items():
#     print(f"{name}'s average score is {score:.2f}")
# print(f"\n{max_student} had the highest overall score of {max_score:.2f}")

# Create a tuple with elements 1, 2, 3, 4, 5, and slice it to get a new tuple with 
# elements 2, 3, 4.
mytuple=(1,2,3,4,5,6)
mytuple1=mytuple [1:4]
print(mytuple1)
#  Create two tuples with elements (1, 2, 3) and (4, 5, 6), and concatenate
# them to get a new tuple with elements (1, 2, 3, 4, 5, 6)
tuple1=(1,2,3)
tuple2=(4,5,6)
mytuple=tuple1+tuple2
print(mytuple)
#  Create a tuple with elements "apple", "banana", "cherry", and use the 
# index method to find the index of "cherry" in the tuple.
tuple=("apple","banana","cherry")
mytuple=tuple.index("cherry")
print(mytuple)
#  Write a function that takes in a list of tuples, where each tuple contains
# three integers, and returns a new list of tuples sorted by the sum of the
# integers in descending order.
def integer(tuples-list):
    tuple1=(1,2,3)
    tuple2=(4,5,6)
    tuple3=(7,8,9)
    tuples=tuple1+tuple2+tuple3
    mytuple=tuples.__reversed__
    


  
      
      
    