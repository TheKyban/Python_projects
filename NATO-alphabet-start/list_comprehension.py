intgers = [1,2,3,4,5,6,7,8,9,10]
new_numbers = [num**2 for num in intgers if num % 2 == 0]
new_intgers = [num**2 for num in intgers if num % 2 != 0]
print(new_numbers)
print(new_intgers)

names = ["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
new_names = [name.upper() for name in names]
print(new_names)