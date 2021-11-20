n=int(input("Enyer your number:"))
i=1
while i<=n:
    k=1
    while k<=i:
        print(i,end="")
        k=k+1
    print()
    i=i+1




k=1
i=1
while i<=5:
    s=1
    while s<=5-i:
        print(' ',end='')
        s=s+1
    a=1
    while a<=k:
        print(a,end='')
        print('*',end=' ')
        a=a+1
    k=k+1
    print()
    i=i+1

n=int(input("Enter your number:"))
for i in range (n):
    print("*"*i)

