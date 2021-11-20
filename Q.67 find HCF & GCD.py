n=int(input("Enter your first number:"))
n1=int(input("Enter your second number:"))
while n%n1!=0:
    rem=n%n1
    n=n1
    n1=rem
print("hcf=",n1)



n=input("enter your name:")
z=0
while z<5:
    # n=input("Enter your string:")
    # for i in n:
    if n=="a":
        if z==0:
            print("  *  ",end=" ")
        elif z==1:
            print("*   *",end=" ")
        elif z==2:
            print("* * *",end=" ")
        elif z==3:
            print("*   *",end=" ")
        elif z==4:
            print("*   *",end=" ")
    elif n=="m":
        if z==0:
            print("*     *",end=" ")
        elif z==1:
            print("* * * *",end=" ")
        elif z==2:
            print("*  *  *",end=" ")
        elif z==3:
            print("*     *",end =" ")
        elif z==4:
            print("*     *",end=" ")
    if n=="e":
        if z==0:
            print("***",end=" ")
        elif z==1:
            print("*  ",end=" ")
        elif z==2:
            print("***",end=" ")
        elif z==3:
            print("*  ",end=" ")
        elif z==4:
            print("***",end=" ")
    if n=="n":
        if z==0:
            print("*  *",end=" ")
        elif z==1:
            print("** *",end=" ")
        elif z==2:
            print("** *",end=" ")
        elif z==3:
            print("* **",end=" ")
        elif z==4:
            print("*  *",end=" ")
    
    print()
    z=z+1










