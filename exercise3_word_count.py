file_path = 'P1_data.txt'

def word_count(file_path):
  with open(file_path, 'r') as f:
    data = f.readlines()
  
  word_dict = {}
  for line in data:
    words = line.lower().strip().split()
    for word in words:
      if word in word_dict:
        word_dict[word] += 1
      else:
        word_dict[word] = 1
  print(word_dict)

word_count(file_path)