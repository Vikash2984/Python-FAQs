def execmain():
    x=int(input("\nEnter a number : "))
    if(abs(x)==x):
        print("You entered a postive no")
    else:
        x*=-1
        print("Number made positive",x)
execmain()