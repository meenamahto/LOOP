n=input("enter your name:")
z=0
while z<5:
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

