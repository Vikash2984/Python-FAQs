#definition

#push_function
def push(a,data):
    a.append(data)

#pop_function
def pop(a):
    x = a.pop()
    print("Popped item : ",x)

#peek_function
def peek(a):
    print("Peek element : ",a[-1])

#display_function
def display(a):
    for i in range (len(a)-1,-1,-1):
        print(a[i])

#__main__

a = []
while True :
    choice = int(input("\n1 -> Push \n2 -> Pop \n3 -> Peek \n4 -> Display \n5 -> Exit \n Enter Your Choice : "))

    if choice == 1:
        data = int(input("Enter value to push : "))
        push(a, data)

    elif choice == 2:
        if len(a)==0:
            print("Stack underflow....")
        else:
            pop(a)

    elif choice == 3:
        if len(a)==0:
            print("Stack underflow....")
        else:
            peek(a)

    elif choice == 4:
        if len(a)==0:
            print("Stack underflow....")
        else:
            display(a)

    elif choice == 5:
        break

    else:
        ("Invalid choice...!")
