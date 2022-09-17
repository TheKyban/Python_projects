from posixpath import split


math,science = input("enter :" ).split()
if math == "yes" and science == "yes" :
    print("you are awarded with 100rs")
elif math == "yes":
    print("you are awarded with 30rs in math")
elif science == "yes":
    print("you are awarded with 30rs in science")