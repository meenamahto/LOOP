n=int(input("Enter your number of raws:"))
i=1
while i<n:
    s=1
    while s<=n-i:
        print(" ",end="")
        s=s+1
    j=1
    while j<=i:
        print("*",end="")
        j=j+1
    print()
    i=i+1
i=1
while n>0:
    b=1
    while b<i:
        print(" ",end="")
        b=b+1
    k=1
    while k<=n:
        print("*",end="")
        k=k+1
    print()
    n=n-1
    i=i+1
