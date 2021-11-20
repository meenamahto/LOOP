i=1
sum=0
while i<=10:
    if i%2==0:
        print(i,"+",i-2,"=",i+i-2)
        sum=sum+i+i-2
    i=i+1
print("sum=",sum)
        