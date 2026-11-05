
print("Welcome to Student Grade Manager")

students = []

while True:
    print("\n--- Student Grade Manager ---")
    print("1. Add Student")
    print("2. Show Results")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        
        student_name = input("Enter student name: ").strip()

        if student_name == "":
            print("Student name cannot be blank.")
            continue
        
        if any(student["name"].lower() == student_name.lower() for student in students):
            print("This student name already exists.")
            continue

        try:
            student_mark = int(input("Enter student marks: "))

            if student_mark < 0 or student_mark > 100:
                print("Marks must be between 0 and 100.")
                continue

        except ValueError:
            print("Invalid marks. Please enter a whole number.")
            continue


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

        students.append({
            "name": student_name,
            "mark": student_mark,
            "grade": grade
        })

        print("Student saved successfully!")

    elif choice == "2":
        if len(students) == 0:
            print("No student records available.")
        else:
            print("\nName             Mark    Grade")
            print("--------------------------------")

            for student in students:
                print(f"{student['name']:<16} {student['mark']:<7} {student['grade']}")

            marks = [student["mark"] for student in students]

            average = sum(marks) / len(marks)
            highest = max(marks)
            lowest = min(marks)

            print("\nClass Statistics")
            print("Average:", round(average, 1))
            print("Highest:", highest)
            print("Lowest:", lowest)

    elif choice == "3":
        print("Thank you for using Student Grade Manager!")
        break

    else:
        print("Invalid choice. Please enter 1, 2 or 3.")
