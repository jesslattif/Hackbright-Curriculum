my_file = open("newfile.txt")
file_text = my_file.read()
my_file.close()

file_text = file_text.lower()
print file_text

counts = [0] * 26

for character in file_text:
	index = ord(character) - 97
	if index>=0 and index < 26:
		counts[index] = counts[index] + 1


print counts