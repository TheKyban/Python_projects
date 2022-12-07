"""
      1
    2  3
  4  5  6
7  8  9  10
"""
a = int(input("Enter num: "))
num = 1
for i in range(a,0,-1):
    for j in range(1,2*i-1):
        print(end=" ")
    for j in range(1,a-i+2):
        print(f"{num}  ",end="")
        num+=1
    print("\r")