"""
      *
    * *
  * * *
* * * *
"""
a = int(input("Enter number: "))

for i in range(a,0,-1):
  for j in range(2*(i-1),0,-1):
    print(end=" ")
  for k in range(1,a-i+2):
    print("* ",end="")
  print("\r")

