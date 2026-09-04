
def Grade(Marks):
    if Students['Marks'] >= '90':
        return "A"
    elif Students['Marks'] >= '80':
        return "B"
    elif Students['Marks'] >= '70':
        return "C"
    elif Students['Marks'] >= '60':
        return "D"
    else:
        return "Fail"



Students = {
    "Name":input('Enter your name: '),
    "Age":input('Enter your age: '),
    "Student_ID":input('Enter your student ID: '),
    "Marks":input('Enter your marks: ')
}

print("The students name is " + Students['Name'])
print("The students age is " + Students['Age'])
print("The students ID is " + Students['Student_ID'])
print("The students marks are " + Students['Marks'])
print("The students grade is " + Grade(Students['Marks']))



final_marks = input('Enter students final marks:')
Students['Marks'] = final_marks


print('Updating students marks...')
print(Students)
print("The students grade is " + Grade(Students['Marks']))


