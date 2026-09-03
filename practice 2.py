
System = True
Students = []



def add_student():
     addStudent = True
     while addStudent == True:
         Students.append({
              "Name": input('Enter the students name:'),
              "Age": input('Enter the students age:'),
              "StudentID": input('Enter the students ID:'),
              "Marks": input('Enter the students marks:')
         })
         addStudent = False
         if addStudent == False:
            break


def view_students():
    print('Students List:')
    for student in Students:
        print(student)


def search_student():
    searchID = input('Enter the student ID to search:')
    found = False
    for student in Students:
        if student[2][1] == searchID:
            print('Student Found:', student)
            found = True
        break
    if not found:
        print('Student not found.')

def determine_grade():
    searchName = input('Enter students name:')
    for student in Students:
        if student[0] == searchName:
            marks = int(student[3][1])
            if marks >= 90:
                grade = 'A'
            elif marks >= 80:
                        grade = 'B'
            elif marks >= 70:
                        grade = 'C'
            elif marks >= 60:
                        grade = 'D'
            else:
                        grade = 'F'
            print('Student:', student[0], 'Grade:', grade)
        if grade in ['A','B','C']:
            print('Pass')
        else:
            print('Fail')
        break


def delete_student():
     delteId = input('Enter the student ID to delte:')
     for student in Students:
        if student[2][1] == delteId:
            Students.remove(student)
            print('Student removed:', student)
        break

def Exit():
    print('Exiting the system.')
    System = False
    




while System == True:
    menu = input('1.Add Student,2.View Students, 3.Search Student, 4.Determine Grade, 5.Delete Student, 6.Exit')

    if menu == '1':
        add_student()
      
    elif menu == '2':
        view_students()

    elif menu == '3':
        search_student()
      
    elif menu == '4':
        determine_grade()
      

    elif menu == '5': 
        delete_student()
      

    elif menu == '6':
        Exit()

       
    




