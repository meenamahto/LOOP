for raw in range(7):
    for col in range(7):
        if   raw==6 or col==0 or col==raw:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
