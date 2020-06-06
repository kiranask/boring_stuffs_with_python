file1 = open('myfile.txt', 'r')
lines = file1.readlines()


# Strips the newline character
for line in lines:
	print(line.strip())