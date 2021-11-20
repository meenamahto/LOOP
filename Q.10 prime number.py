n=int(input("Enter your number:"))
i=1
fact=0
while i<=n:
    if n%i==0:
        fact=fact+1
    i=i+1
if fact==2:
    print(n, "prime  number")
else:
    print(n,"composite number")

