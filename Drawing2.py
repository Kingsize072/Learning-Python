num = int(input("Please Enter your number: "))
for i in range(num):
    print(" " * (num-i-1) + "*" * (2*i+1))