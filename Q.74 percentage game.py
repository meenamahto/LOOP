print("Enter your name / marks /")
while True:
    name=input("Enter your name :")
    m=int(input("Enter your mathsmatic marks:"))
    m1=int(input("Enter your science marks:"))
    m2=int(input("Enter your history marks:"))
    m3=int(input("Enter your political marks:"))
    total_marks=m+m1+m2+m3
    percentage=(total_marks/400)*100
    print(name,"your total marks is",total_marks,"and your percentage is",percentage)
    a=input("want you enter more yes/no:")
    if a!="yes":
        print("ok")
        break


