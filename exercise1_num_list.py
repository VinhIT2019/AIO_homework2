# 1
num_list = [3, 4, 5, 1, -44 , 5 ,10, 12 ,33, 1]
k=3
output=[]
if k>=1:
  for i in range(0, len(num_list)-k+1):
    output.append(max(num_list[i:i+k]))
  print(output)
else:
  print("Error: k<1")