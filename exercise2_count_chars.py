#2
def count_chars(s):
    char_dict = {}
    for char in s:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    print(char_dict)

string = 'Happiness'
count_chars(string)

string = 'smiles'
count_chars(string)