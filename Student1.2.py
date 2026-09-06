
def Grade(Marks):
    Marks = Students['Marks']    
    if Marks >= 90:
        return "A"
    elif Marks >= 80:
        return "B"
    elif Marks >= 70:
        return "C"
    elif Marks >= 60:
        return "D"
    else:
        return "Fail"


Students = {
    "Name":input('Enter your name: '),
    "Age":int(input('Enter your age: ')),
    "Student_ID":int(input('Enter your student ID: ')),
    "Marks":int(input('Enter your marks: '))
    
}

def Grade(Marks):
    Marks = Students['Marks']    
    if Marks >= 90:
        return "A"
    elif Marks >= 80:
        return "B"
    elif Marks >= 70:
        return "C"
    elif Marks >= 60:
        return "D"
    else:
        return "Fail"


print(Grade('Marks'))




print(f"Student Name: {Students['Name']}")
print(f"Student Age: {Students['Age']}")
print(f"Student ID: {Students['Student_ID']}")
print(f"Student Marks: {Students['Marks']}")

final_marks = int(input('Enter students final marks:'))
Students['Marks'] = final_marks


print('Updating students marks...')
print(Students)
print(f"The students grade is {Grade(Students['Marks'])}")



