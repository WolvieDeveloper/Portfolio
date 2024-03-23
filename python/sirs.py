print("#------------------------------------------------#")
print("THIS PROGRAM WILL DISPLAY THE POWER OF USING LIST")
print("#------------------------------------------------#")

def showAllRecords():
    cnt = len(students)
    for i in range(cnt):
        print(str(i+1) + "]" + students[i])


def searchStudent(studname):
    size = len(students)
    for i in range(size):
        print(students[i])
        if studname == students[i]:
            print("Found " + students[i] + " " + str(i+1))
            return

    print("File not found!")
            

def DelStudent(studname):
    size = len(students)
    for i in range(size):
        print(students[i])
        if studname == students[i]:
            print("Found " + students[i] + " " + str(i+1))
            del(students[i])
            print("record deleted")
            return

    print("File not found!")    
        
    1
  



students = []
while(True):
    print("Size: " + str(len(students)))
    print("--------------------------")
    print("     MENU    ")
    print("1.] ADD Student")
    print("2.] REMOVE STUDENT")
    print("3.] DISPLAY ALL RECORDS")
    print("4.] SEARCH STUDENT ")
    print("5.] EXIT")
    option = input("Enter your option: ")
    if option == "1":
        print("Add student ")
        varname = input("Enter name ")
        students.append(varname)
    elif option == "2":
        sn = input("Enter name to delete: " )
        DelStudent(sn)
    elif option == "3":
        showAllRecords()
    elif option == "4":
        sn = input("Enter name: " )
        searchStudent(sn)
        print("Search student")
    elif option == "5":
        print("Exit application")
        break
    else:
        print("Invalid option")

print("Done!")