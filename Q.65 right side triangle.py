n=int(input("Enter your number of raws:"))
# n=5
i=1
while i<=n:
    j=1
    while j<=n-i:
        print(" ",end="")
        j=j+1
    s=1
    while s<=i:
        print(j,end="")
        s=s+1
    print()
    i=i+1