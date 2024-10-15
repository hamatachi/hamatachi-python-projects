students = []

# Function to shift characters by 2
def encrypt_string(word):
    encrypted_string = ""
    
    for char in word:
        if char.isalpha():
            new_char = chr(ord(char) + 2)
            
            if char.islower() and new_char > 'z':
                new_char = chr(ord(new_char) - 26)
            elif char.isupper() and new_char > 'Z':
                new_char = chr(ord(new_char) - 26)
                
            encrypted_string += new_char
        else:
            encrypted_string += char
    
    return encrypted_string

def add_to_database():
    add_students = True
    while add_students:
        print("Welcome to the GradeMaster!")
        print("Please enter a student name:")
        student_name = input()

        encrypted_name = encrypt_string(student_name)

        print("Please enter a student ID:")
        student_id = input()

        while True:
            print("Please enter a grade from 1 to 9:")
            grade = input()
            if grade.isdigit() and 1 <= int(grade) <= 9:
                break
            else:
                print("Invalid grade. Please enter a whole number between 1 and 9.")

        student = {"name": encrypted_name,
                   "id": student_id,
                   "grade": grade}

        students.append(student)

        print("Would you like to add another student? Y/N")
        answer = input().upper()
        if answer == "N":
            add_students = False

def edit_student():
    print("Please enter the name of the student you'd like to edit:")
    student_name = input()

    encrypted_name = encrypt_string(student_name)
    
    student_found = False

    for student in students:
        if student["name"] == encrypted_name:
            student_found = True
            print("Student found! What would you like to edit?")
            print("1. Name")
            print("2. ID")
            print("3. Grade")
            choice = input()
            
            if choice == "1":
                print("Enter new name:")
                new_name = input()
                student["name"] = encrypt_string(new_name)  # Encrypt new name
            elif choice == "2":
                print("Enter new ID:")
                student["id"] = input()
            elif choice == "3":
                while True:
                    print("Enter new grade (1 to 9):")
                    new_grade = input()
                    if new_grade.isdigit() and 1 <= int(new_grade) <= 9:
                        student["grade"] = new_grade
                        break
                    else:
                        print("Invalid grade. Please enter a whole number between 1 and 9.")
            else:
                print("Invalid choice!")
            return
    
    if not student_found:
        print("Error: Student not found.")

def delete_student():
    print("Please enter the name of the student you'd like to delete:")
    student_name = input()

    # Corrected to use encrypt_string
    encrypted_name = encrypt_string(student_name)
    
    for student in students:
        if student["name"] == encrypted_name:
            students.remove(student)
            print(f"Student {student_name} has been deleted.")
            return
    
    print("Error: Student not found.")

def view_students():
    if not students:
        print("No students created in database.")
    else:
        print("\n--- Student Records ---")
        for student in students:
            print(f"Name: {student['name']}, ID: {student['id']}, Grade: {student['grade']}")
        print("-----------------------")

def menu():
    while True:
        print("\nStudent Database Menu")
        print("1. Add a new student")
        print("2. Edit an existing student")
        print("3. Delete a student")
        print("4. View all students")
        print("5. Exit")
        choice = input("Please choose an option (1-5): ")
        
        if choice == "1":
            add_to_database()
        elif choice == "2":
            edit_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            view_students()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please choose again.")

menu()
