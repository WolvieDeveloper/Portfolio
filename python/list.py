
# fruits['apple','orange','grapes','mango']


# for fruit in fruits:
#     print(fruit)


students = []

# def showall():
#     x = 0
#     for name in students:
#         print(x+)

def addstudent(name):
    students.append(name)
    print("Name: ", name , " Added")

while(True):
    print("     Menu")
    print("1. Add Student")
    print("2. Show All Student")
    print("3. Search Student")
    print("4. Remove Student")
    print("5. Exit")
    opt = input("Select Option:>>")

    if opt == '1':
        print("Add a Student")
        name = input("Name: ")
        addstudent(name)
        

    elif opt == '2':
        print("All Student")
    elif opt == '3':
        print("Search Student")
    elif opt == '4':
        print("Remove")
    elif opt == '5':
        print("Exit")
        break
print("End")