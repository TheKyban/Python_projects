import pandas
students_dic = {
    "students":["Angela","James","Lily"],
    "score":[56,76,98]
}


nato = pandas.read_csv("nato_phonetic_alphabet.csv")
data = pandas.DataFrame(nato)
# print(data)

data_dic = {row.letter:row.code for (index,row) in data.iterrows()}

user = input("Enter ").upper()
final_output = [data_dic[letter] for letter in user]
print(final_output)