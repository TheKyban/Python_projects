a = int(input("Enter Num: "))
for i in  range(1,a+1):
    for j in range(1,2*i-1):
        print(end=" ")
    for j in range(1,a-i+2):
        print("* ",end="")
    print("\r")