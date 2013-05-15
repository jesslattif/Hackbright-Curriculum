from sys import argv
script, filename = argv

def count_words(filename):
	in_file = open(filename)
	read_file = in_file.read()
	in_file.close()

	read_file = read_file.lower()
	read_file = read_file.replace("."," ").replace(","," ").replace("?"," ")
	

	print read_file 

	words = read_file.split()
	my_dict = {}

	for word in words:
		if word in my_dict:
			my_dict[word] += 1
		else: my_dict[word] = 1
	
	print my_dict

print count_words(filename)