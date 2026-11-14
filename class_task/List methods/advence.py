
students = []

def add_student():
    name = input("Enter Student Name: ")
    marks = int(input("Enter Student Marks: "))

    students.append({
        "name": name,
        "marks": marks
    })

def display_students():
    print("\n--- Student Listing ---")

    for student in students:
        print("Name:", student["name"])
        print("Marks:", student["marks"])

def search_student():
    name = input("Enter Name to Search: ")

    for student in students:
        if student["name"].lower() == name.lower():
            print("Student Found:", student)
            return

    print("Student Not Found!")

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        break
    else:
        print("Invalid Choice!")
