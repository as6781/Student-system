Employee = []
Admins = [{'username': 'admin', 'password': 'admin123'}]
Employee_leave = []
Accepted_leave = []
Rejected_leave = []

print('welcome to the management system')



def emp_menu(employee):
    while True:
        emp_option = input('Please select an option: 1. View Profile, 2. Apply for Leave, 3. Logout: ')
        if emp_option == '1':
            print('Viewing profile...')
           
            print(f"Username: {employee['username']}")
        elif emp_option == '2':
            leave_request = input(f'Please enter your leave request and date of leave for employee {employee["username"]}: ')
            Employee_leave.append(f"Leave request for {employee['username']}: {leave_request}")
            print('Leave request submitted.')
        elif emp_option == '3':
            print('Logging out...')
            break
        else:
            print('Invalid option. Please try again.')


def leave_aprove():
    while True:
        print('\n--- Pending Leave Requests ---')

        for leave in Employee_leave:
            print(leave)

        leave_option = input(
            '1. Approve Leave, 2. Reject Leave, 3. Return: '
        )

        if leave_option == '1' or leave_option == '2':
            username = input('Enter the employee username: ')

            leave_request = None

            for leave in Employee_leave:
                if f'Leave request for {username}:' in leave:
                    leave_request = leave
                    break

            if leave_request is None:
                print('No pending request found for that username.')
                continue

            if leave_option == '1':
                Accepted_leave.append(leave_request)
                print(f'{username}\'s leave request has been approved.')

            else:
                Rejected_leave.append(leave_request)
                print(f'{username}\'s leave request has been rejected.')

            Employee_leave.remove(leave_request)

        elif leave_option == '3':
            print('Returning to main menu...')
            break

        else:
            print('Invalid option. Please try again.')
def register():
    username = input('Enter username: ')
    password = input('Enter password: ')
 
    employee = {'username': username, 'password': password}
    Employee.append(employee)

    print('Registration successful!')
    emp_menu(employee)

def admin_menu():
    while True:
        admin_option = input('Please select an option: 1. View All Employees, 2. View Leave Requests, 3. Logout: ')
        if admin_option == '1':
            print('Viewing all employees...')
            for employee in Employee:
                print(f"Username: {employee['username']}")
        elif admin_option == '2':
            leave_aprove()
        elif admin_option == '3':
            print('Logging out...')
            break
        else:
            print('Invalid option. Please try again.')

def login():
        username = input('Enter username: ')
        password = input('Enter password: ')
        for employee in Employee:
            if employee['username'] == username and employee['password'] == password:
                print('Login successful!')
                emp_menu()

        for admin in Admins:
            if admin['username'] == username and admin['password'] == password:
                print('Login successful!')
                admin_menu()
                return
        return 

        print('Invalid username or password.')


while True:
    MainMenu = input('Please select an option: 1. Register, 2. Login, 3. Exit: ')
    if MainMenu == '1':
        register()
    elif MainMenu == '2':
        login()
    elif MainMenu == '3':
        print('Exiting the system. Goodbye!')
exit()