i=1
while i<=5:
    j=1
    while j<=i:
        print('*',end='')
        j=j+1
    print()
    i=i+1

n=int(input("Enter your number:"))
for i in range(1,n+1):
    print("*"*i)

