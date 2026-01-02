#Student Management System
"""
Project Idea: Design a student management system where you can add,
delete, and update student records. Each student’s information can be stored as an object.
Why It’s Great for Beginners: This project involves working with lists of objects and
performing various operations on them.
"""

class Student:

    def __init__(self, name, age, grade,id):
        self.name = name
        self.age = age
        self.grade = grade
        self.id = id

    def __str__(self):
        return f"{self.name} | {self.age} of age is in Grade {self.grade} with ID {self.id}"

class Records:

    def __init__(self):
        self.students = []
        self.next_id = 1

    def add_student(self, student):

        student.id = self.next_id
        self.next_id += 1
        self.students.append(student)
        print(f"Student {student.name} added successfully.")

    def delete_student(self, id):

        for i, student in enumerate(self.students):
            if student.id == id:
                del self.students[i]
                print(f"Student with id {id} deleted.")
                return

        print(f"No student found with id {id}.")


    def update_student(self, id, name, age, grade):
        for student in self.students:
            if student.id == id:
                student.name = name
                student.age = age
                student.grade = grade

                print(f"Student {id} has been updated successfully \n{student}")
                return

        print(f"No student found with id {id}.")

    def view_student(self):

        if not self.students:
            print("No students available.")
            return
        for student in self.students:
            print(student)



def main():

    records = Records()

    while True:

        print("\n--- STUDENT MANAGEMENT SYSTEM ---")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. View Student")
        print("5. Exit")
        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == 1:
            name = input("Enter student name: ")
            try:
                age = int(input("Enter student age: "))
            except ValueError:
                print("Invalid age. Please try again.")
                continue
            grade = (input("Enter student grade: 1st,2nd etc."))

            student = Student(name, age, grade, 0)
            records.add_student(student)


        elif choice == 2:
            id = int(input("Enter student id: "))

            if id :
                records.delete_student(id)
            else:
                print("Student with id does not exist.")

        elif choice == 3:
            id = int(input("Enter student id: "))
            name = input("Enter update student name: ")
            age = int(input("Enter update student age: "))
            grade = (input("Enter update student grade: 1st,2nd etc."))

            records.update_student(id, name, age, grade)


        elif choice == 4:
            records.view_student()

        elif choice == 5:
            print("Thank you for your time. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

main()










