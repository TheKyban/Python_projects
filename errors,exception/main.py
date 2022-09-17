try:
    with open("text.txt") as f:
        text = f.read()
        print(text)
        a_dic = {"key":"value"}
        print(a_dic["key"])

except FileNotFoundError:
    with open("text.txt","w") as f:
        f.write("hello Aditya")

except KeyError as s :
    print(f"The {s} is not found")

else:
    print("done")

finally:
    raise TypeError("this is a type error")