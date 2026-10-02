students = []
def add_students():
    roll_no = input("Enter Roll Number: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")
    marks = float(input("Enter student marks: "))
    student = {
        "roll_no": roll_no,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }
    students.append(student)
    print(f"Student {name} added successfully.")

def view_students():
    if not students:
        print("No students found.")
        return
    for student in students:
        print("\n------------")
        print("Roll Number:", student["roll_no"])
        print("Name:", student["name"])
        print("Age:", student["age"])
        print("Course:", student["course"])
        print("Marks:", student["marks"])

def search_student():
    roll_no = input("Enter Roll Number to search: ")
    for student in students:
        if student["roll_no"] == roll_no:
            print("\nStudent found:")
            print("Roll Number:", student["roll_no"])
            print("Name:", student["name"])
            print("Age:", student["age"])
            print("Course:", student["course"])
            print("Marks:", student["marks"])
            return
    print("Student not found.")


def delete_student():
    roll_no = input("Enter Roll Number to delete: ")
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            print(f"Student with Roll Number {roll_no} deleted successfully.")
            return
    print("Student not found.")


def update_student():
    roll_no = input("Enter Roll Number to update: ")
    for student in students:
        if student["roll_no"] == roll_no:
            print("Enter new details (leave blank to keep current value):")
            name = input(f"Name ({student['name']}): ") or student['name']
            age = input(f"Age ({student['age']}): ") or student['age']
            course = input(f"Course ({student['course']}): ") or student['course']
            marks_input = input(f"Marks ({student['marks']}): ")
            marks = float(marks_input) if marks_input else student['marks']
            student.update({
                "name": name,
                "age": age,
                "course": course,
                "marks": marks
            })
            print(f"Student with Roll Number {roll_no} updated successfully.")
            return
    print("Student not found.")

while True:    
    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    choice = input("Enter your choice: ")
    if choice == '1':
     add_students()
    elif choice == '2':
     view_students()
    elif choice == '3':
     search_student()
    elif choice == '4':
     delete_student()
    elif choice == '5':
     update_student()
     pass
    elif choice == '6':
     print("Exiting the program.")
     break
    else:
     print("Invalid choice. Please try again.")