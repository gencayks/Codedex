file = open("diaries.txt", "w")
file.write("Dear Diary, ")




file = open(file_path , mode )


lines = ['This is a line.\n', 'This is the next line.\n']
file.writelines(lines)





file = open('filename.txt', 'r')
content = file.read()
print('Using read():')
print(content)

line1 = file.readline()  # Read the first line
print(line1, end='')     # Printing the first line
line2 = file.readline()  # Read the second line
print(line2, end='')     # Printing the second line

with open('filename', 'r') as f:
  # handle file here