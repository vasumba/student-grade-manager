print("Welcome to Student Grade Manager")
student_name = "Priya"
student_mark = 92
grade = "A"
if student_mark >= 90:
    grade = "A"
elif student_mark >= 80:
    grade = "B"
elif student_mark >= 70:
    grade = "C"
elif student_mark >= 60:
    grade = "D"
else:
    grade = "E"
print("Name:", student_name)
print("Mark:", student_mark)
print("Grade:", grade)
print("Test program completed successfully")