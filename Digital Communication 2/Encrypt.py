#python code for encryption

# take path of the file as an input
##path = r'input.txt'
path = r'input.jpeg'
##path = r'input.wav'

# taking encryption key as input
key = 122
		
# open file for reading purpose
fin = open(path, 'rb')
	
# storing file's data in variable "file"
file = fin.read()
fin.close()
	
# converting file into byte array to perform encryption easily on numeric data
file = bytearray(file)

# performing XOR operation on each value of bytearray
for index, values in enumerate(file):
        file[index] = values ^ key

# opening file for writting purpose
fin = open(path, 'wb')
	
# writing encrypted data in image
fin.write(file)
fin.close()
