
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
