employees = {101:{'name':'muttu','dept':'10','salary':123456789}}
def create_employee():
    empid = int(input("Enter the employee ID: "))
    if empid in employees:
        print("Employee already exists")
        return
    name = input("Enter the employee name: ")
    dept = (input("Enter the employee department: "))
    salary = float(input("Enter the employee salary: "))
    employees[empid] = {
        "name":name,
        "dept":dept,
        "salary":salary,
    }
    print("Employee added successfully")


def total_salary():
    total = sum(emp["salary"] for emp in employees.values())
    print("Total salary: ", total)

def departmental_statistics():
    while True:
        print("1. Department Average Salary")
        print("2. Department Max Salary")
        print("3. Department wise Count")
        print("4. Exit Statistics Menu")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            dep_avg_sal()
        elif choice == 2:
            dep_max_sal()
        elif choice == 3:
            dep_emp_count()
        elif choice == 4:
            break
        else:
            print("Invalid choice")

def dep_avg_sal():
    dept_data = {}
    for emp in employees.values():
        dept = emp["dept"]
        dept_data.setdefault(dept,[]).append(emp["salary"])

    for dept, sal in dept_data.items():
        avg = sum(sal)/len(sal)
        print(f"{dept} \t\t Average Salary: {avg}")
    print()
    
def dep_emp_count():
    dept_data = {}
    for emp in employees.values():
        dept = emp["dept"]
        dept_data[dept]=dept_data.setdefault(dept,0)+1

    for dept, count in dept_data.items():
        print(f"{dept} \t\t count: {count}")
    print()

def dep_max_sal():
    dept_data = {}
    for emp in employees.values():
        dept = emp["dept"]
        if dept in dept_data:
            if dept_data[dept]<emp["salary"]:
                dept_data[dept]=emp["salary"]
        else:
            dept_data[dept]=emp["salary"]
    for dept, sal in dept_data.items():

        print(f"{dept} \t\t max Salary: {sal}")
    print()
while True:
    print('1.create employee\n2.total salary\n3.departmental statistics\n4.exit')
    choice = int(input("Enter your choice: "))
    if choice == 1:
        create_employee()
    elif choice == 2:
        total_salary()
    elif choice == 3:
        departmental_statistics()
    elif choice == 4:
        break
    else:
        print("Invalid choice")