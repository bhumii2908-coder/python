# organizing student grades
# create a list to store and calculate average grades for students
grades=[88,94,78,79,95,83]

# adding a new grade
grades.append(75)

# calculating the average grade
average_grade = sum(grades)/len(grades)
print(F"Average grade:{average_grade:.2f}")

# finding the highest and lowest grades
highest_grade= max(grades)
lowest_grade = min(grades)
print(f"highest grade:{highest_grade}")
print(f"lowest grade:{lowest_grade}")