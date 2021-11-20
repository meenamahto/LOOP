n=int(input("enter your number wherever you want sum:"))
i=1
k=0
sum=0
while i<=n:
    k=k+i*i*i
    print(k,' + ',end='')
    sum=sum+k
    i=i+1
print()
print(sum)





