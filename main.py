students = {

}

def menu(): #Just to Start with asking the users choice
    print("---Student Management System---")
    print("1. Add Student")
    print("2. View Students")
    print("3. Save to file")
    print("4. Load Students from file")
    print("5. Exit")
def addstudent(students): #Adding Students
    roll = int(input("Enter the students roll.no: "))

    if roll in students:
        print("This students data already exists")
        return
    name = str(input("Enter the students name: "))
    age = int(input("Enter the students age: "))
    
    students[roll] = {
        "name" : name,
        "age" : age

    }
    print("Student Added Succesfully")
def viewstudents(students):#Access to Students info if in RAM
    if not students:
        print("No students in the data, Try to load it first")    
        return

    for roll, info in students.items():
        print(f"\nRoll: {roll}")
        print("Name:", info["name"])
        print("Age:", info["age"])
        
def savetofile(students):#Saving everything to a file as RAM clears all the data 
    with open("studentsdata.txt", "w") as f:
        for roll, info in students.items():
            line = f"{roll},{info['name']},{info['age']}\n"
            f.write(line)
    print("Data Saved to File")
def loadfromfile(students):#We have to load data to RAM to see the Students whenever we reopen the file
    try:
        with open("studentsdata.txt", "r") as f:
            for line in f:
                roll, name, age,  = line.strip().split(",")

                students[int(roll)] = {
                    "name": name,
                    "age": int(age),
                    
                }

        print("Data loaded successfully!")

    except FileNotFoundError:
        print("File not found!")

    return students 
while True: #Whole Loop
    menu()
    choice = input("Enter Choice: ")
    
    if choice == "1":
        addstudent(students)
    elif choice == "2":
        viewstudents(students)
    elif choice == "3":
        savetofile(students)  
    elif choice == "4":
        loadfromfile(students)
    elif choice == "5":
        print("Exiting File")
        break
    else:
        print("Invalid Choice, Try again choosing 1,2,3,4,5 !")#A good message so that if the user was entering something else


