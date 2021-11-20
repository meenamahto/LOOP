n=int(input("Enter your number:"))
i=n
sum=0
while n>0:
    d=n%10
    sum=sum+d
    n=n//10
if i%sum==0:
    print("harshad number")
else:
    print("not harshad number")
