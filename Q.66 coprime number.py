a=int(input("Enetr your first number:"))
b=int(input("Enter your second number:"))
while a%b!=0:
    rem=a%b
    a=b
    b=rem
if b==1:
    print("coprime number",b)
else:
    print("not coprime number",b)


