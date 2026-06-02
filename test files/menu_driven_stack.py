class Stack:
    listA=[]
    def push(a):
        listA.append(a)
        print(f'viited {a}')
    
    def do_pop():
        if listA:
            b=listA.pop()
            print(f'Went back from {b}')
        else:
            print('list is empty')
    
    def peek():
        print(f'last visited is {listA[-1]}')

    def is_empty():
        print(len(listA)>0)
    
    def history():
        for i in listA:
            print(i)

s=Stack()
while True:
    print('1.visit a new website\n2.Go back\n3.Display recent page\n4.Display browser history\n5.is history present\n6.exit\n')
    print('========================================')
    choice=int(input('Enter the choice'))
    if choice==1:
        a=input('Enter the URL')
        s.push(a)
    elif choice==2:
        s.do_pop()
    elif choice==3:
        s.peek()
    elif choice==4:
        s.history()
    elif choice==5:
        s.is_empty()
    else:
        print("invalid input")
    


