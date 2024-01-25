from Crypto.Cipher import AES

# Function to remove both front and back preambles and sequence from file
def remove_preamble(file_path):
    global content
    detect_sequence = b'0011001100110011'
    preamble = bytes([0b10101010]) * 3000

    with open(file_path, 'rb') as file:
        content = file.read()

    start_index = content.find(detect_sequence)
    if start_index != -1:
        content = content[start_index + len(detect_sequence):]

    end_index = content.rfind(detect_sequence)
    if end_index != -1:
        content = content[:end_index]

    preamble_length = len(preamble)
    while True:
        start_index = content.find(preamble)
        if start_index == -1:
            break
        else:
            content = content[start_index + preamble_length:]

    while True:
        end_index = content.rfind(preamble)
        if end_index == -1:
            break
        else:
            content = content[:end_index]




def decrypt_file(key):
    
    ciphertext = content
    cipher = AES.new(key, AES.MODE_ECB)  
    decrypted = cipher.decrypt(ciphertext).rstrip(b'\0')  # Removing padding
    
    #Write the decrypted file
    with open('decrypted_file', 'wb') as file:
        file.write(decrypted)


#Key
predefined_key = b'Hello_IamMihiran'


# Remove both front and back preambles and sequence from the output.tmp file
remove_preamble('output.tmp')


decrypt_file(predefined_key)