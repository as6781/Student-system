
System = True
Students = []



def add_student():
    student = {}
    student['Name'] = input('Enter your name: ')
    student['Age'] = int(input('Enter your age: '))
    student['StudentID'] = int(input('Enter your student ID: '))
    student['Marks'] = int(input('Enter your marks: '))
    Students.append(student)
    print('Student added:', student)



def view_students():
    print('Students List:')
    for student in Students:
        print(student)


def search_student():
    searchID = int(input('Enter the student ID to search:'))
    found = False
    for student in Students:
        if student['StudentID'] == searchID:
            print('Student Found:', student)
            found = True
    if not found:
        print('Student not found.')

def determine_grade():
    searchName = input('Enter students name:')
    for student in Students:
        if student['Name'] == searchName:
            marks = int(student['Marks'])
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
            print('Student:', student['Name'], 'Grade:', grade)
        if grade in ['A','B','C']:
            print('Pass')
        else:
            print('Fail')
        break


def delete_student():
     delteId = int(input('Enter the student ID to delte:'))
     for student in Students:
        if student['StudentID'] == delteId:
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
     System = Exit()

       
    




