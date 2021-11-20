n=int(input("Enter your number:"))
orig=n
sum=0
while n>0:
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if sum==orig:
    print("amstrong number")
else:
    print("not amstrong")