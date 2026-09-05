
def Grade(Marks):
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
    "Age":input('Enter your age: '),
    "Student_ID":input('Enter your student ID: '),
    "Marks":int(input('Enter your marks: '))
    
}




print("The students name is " + Students['Name'])
print("The students age is " + Students['Age'])
print("The students ID is " + Students['Student_ID'])
print("The students marks are " + str(Students['Marks']))
print("The students grade is " + Grade(Students['Marks']))



final_marks = int(input('Enter students final marks:'))
Students['Marks'] = final_marks


print('Updating students marks...')
print(Students)
print("The students grade is " + Grade(Students['Marks']))


