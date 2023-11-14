#Write a python program that takes courses marks as input and then calculates average of all the 
#courses. After calculating the average, calculate the percentage of a student using total marks. Assume 
#the total of all the courses marks is 500 or take the total marks from the user as input.

Courses= int(input("Enter the number of courses: "))
total_marks = float(input("Enter the total marks: "))
sum_of_marks = 0

for i in range(Courses):
    course_marks = float(input(f"Enter marks for course {i + 1}: "))
    sum_of_marks = course_marks

# Calculate average
average_marks = sum_of_marks / Courses

# Calculate percentage
percentage = (sum_of_marks / total_marks) * 100

#  results
print("\nAverage marks:", average_marks)
print("Percentage:", percentage, "%")
