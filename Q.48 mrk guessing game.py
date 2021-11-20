a=5
print("I have a number in my mind ,can you guess it .")
while True:
    n=int(input("Enter your guessing number :"))
    if n==a:
        print("wow! amazing, your number is correct.")
        break
    elif n>a:
        print("my number is smaller than the number you entered \ntry again\n")
    else:
        print("my number is greater than the number you entered. \ntry again\n")

