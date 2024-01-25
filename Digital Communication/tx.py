from Crypto.Cipher import AES




def add_preamble():
    preamble = bytes([0b10101010]) * 3000
    detect_sequence = b'0011001100110011'  # Sequence to detect preamble
    
    with open('encrypted.tmp', 'wb') as output_file:
        output_file.write(preamble + detect_sequence + ciphertext + detect_sequence + preamble)

#Encryption
def pad(data):
    # Padding the data to be a multiple of 16 bytes
    return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

def encrypt_file(file_path, key):
    global ciphertext
    with open(file_path, 'rb') as file:
        plaintext = file.read()

    plaintext = pad(plaintext)
    cipher = AES.new(key, AES.MODE_ECB)  
    ciphertext = cipher.encrypt(plaintext)

  



# Encryption details
file_path = 'gr-logo.png'
predefined_key = b'Hello_IamMihiran'

# Encrypt the file
encrypt_file(file_path, predefined_key)

#Adds the preamble
add_preamble()
