for raw in range(7):
    for col in range(7):
        if raw==0 or col==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

for raw in range(5):
    for col in range(4):
        if raw==0 or raw==2 or (col==0 or col==3  ):
            print("*",end="")
        else:
            print(" ",end="")
    print()


for raw in range(7):
    for col in range(5):
        if (raw==0 or raw==3 or raw==6) or (col==0 and col!=3 and col!=6):
            print("*",end="")
        else:
            print(" ",end=" ")
    print()
 


