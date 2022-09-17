student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    
    pass
    # print(key)
    # print(value)

import pandas
student_data = pandas.read_csv("nato_phonetic_alphabet.csv")
student_data_frame = pandas.DataFrame(student_data)
# print(student_data_frame)

#
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# print(student_data.to_dict())
data = {row.letter:row.code for (index,row) in student_data.iterrows()}
# print(data)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def fullname():
    user = input("enter your name ").upper()
    try:
        output_list = [data[letter] for letter in user]
    except KeyError :
        print("enter valid Letters")
    else:
        print(output_list)

while(True):
    fullname()