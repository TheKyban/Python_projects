"""
* 
*  * 
*  *  *
*  *  *  *
*  *  *
*  * 
*
"""

a = int(input("enter num: "))
for i in range(a,0,-1):
    for j in range(1,a-i+2):
        print("*  ",end="")
    print("\r")
for i in range(1,a):
    for j in range(1,a-i+1):
        print("*  ",end="")
    print("\r")