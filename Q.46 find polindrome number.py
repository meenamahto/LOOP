n=int(input("Enetr your number:"))
i=n
rev=0
while n>0:
    rev=(rev*10)+n%10
    n=n//10
if i==rev:
    print("polindrome number")
else:
    print("not polindrome nummber")

