for raw in range(7):
    for col in range(7):
        if  raw==0 or raw==6 or col==0 or col==6:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()