emp=[{'name':'vishwanath','dept':10,'sal':100000},{'name':'john','dept':20,'sal':200000}]
while True:
    print('===================================')
    print('1.Get Employee Details\n2.Calculate the Total Salary\n3.Dept statistics\n4.Exit')
    print('===================================')
    first_val=int(input("Enter your choice: "))
    if first_val == 1:
        for i in emp:
            print(f'{i['name']}|{i['dept']}|{i['sal']}')
    elif first_val == 2:
        total_salary = 0
        for i in emp:
            total_salary += i['sal']
        print(f'Total salary: {total_salary}')
    elif first_val == 3:
        while True:
            print('-----------------------------------')
            print('1.Get deptwise avg sal\n2.Dept max sal\n3.dept count\n4.Exit')
            print('-----------------------------------')
            dept_val=int(input("Enter your choice: "))
            if dept_val == 1:
                dept_avg_sal={}
                for i in emp:
                    if i['dept'] not in dept_avg_sal:
                        dept_avg_sal[i['dept']] = []
                    dept_avg_sal[i['dept']].append(i['sal'])
                for dept, salaries in dept_avg_sal.items():
                    print(f'Dept {dept} avg sal: {sum(salaries)/len(salaries)}')
            elif dept_val == 2:
                dept_max_sal={}
                for i in emp:
                    if i['dept'] not in dept_max_sal:
                        dept_max_sal[i['dept']] = i['sal']
                    elif i['sal'] > dept_max_sal[i['dept']]:
                        dept_max_sal[i['dept']] = i['sal']
                for dept, max_sal in dept_max_sal.items():
                    print(f'Dept {dept} max sal: {max_sal}')
            elif dept_val == 3:
                dept_count={}
                for i in emp:
                    if i['dept'] not in dept_count:
                        dept_count[i['dept']] = 1
                    else:
                        dept_count[i['dept']] += 1
                for dept, count in dept_count.items():
                    print(f'Dept {dept} count: {count}')
            elif dept_val == 4:
                break
            else:
                print("Invalid choice")
    elif first_val == 4:
        break
    else:
        print("Invalid choice")
    