#import libraries
import sys
import numpy as np
from PIL import Image
from cryptography.fernet import Fernet






np.set_printoptions(threshold=sys.maxsize)

#encoding function
def Encode(src, message, dest):




    img = Image.open(src, 'r')
    width, height = img.size
    array = np.array(list(img.getdata()))
    #array=fft.dct(arr)

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size//n

    message += "$t3g0"
    b_message = ''.join([format(ord(i), "08b") for i in message])
    req_pixels = len(b_message)

    if req_pixels > total_pixels:
        print("ERROR: Need larger file size")

    else:
        index=0
        for p in range(total_pixels):
            for q in range(0, 3):
                if index < req_pixels:
                    array[p][q] = int(bin(array[p][q])[2:9] + b_message[index], 2)
                    index += 1

        array=array.reshape(height, width, n)
        enc_img = Image.fromarray(array.astype('uint8'), img.mode)
        enc_img.save(dest)
        print("Image Encoded Successfully")


#decoding function
def Decode(src):

    img = Image.open(src, 'r')
    array = np.array(list(img.getdata()))

    if img.mode == 'RGB':
        n = 3
    elif img.mode == 'RGBA':
        n = 4

    total_pixels = array.size//n

    hidden_bits = ""
    for p in range(total_pixels):
        for q in range(0, 3):
            hidden_bits += (bin(array[p][q])[2:][-1])

    hidden_bits = [hidden_bits[i:i+8] for i in range(0, len(hidden_bits), 8)]

    message = ""
    for i in range(len(hidden_bits)):
        if message[-5:] == "$t3g0":
            break
        else:
            message += chr(int(hidden_bits[i], 2))
    if "$t3g0" in message:
        print("Hidden Message:", message[:-5])
    else:
        print("No Hidden Message Found")


    print("Message after encode",message)

#main function
def Stego():


    func = 1

    if func == '1':
        # we will be encryting the below string.
        print("Enter Message to Hide")
        message = input()

        # generate a key for encryptio and decryption
        # You can use fernet to generate
        # the key or use random key generator
        # here I'm using fernet to generate key

        key = Fernet.generate_key()

        # Instance the Fernet class with the key

        fernet = Fernet(key)

        # then use the Fernet class instance
        # to encrypt the string string must must
        # be encoded to byte string before encryption
        encMessage = fernet.encrypt(message.encode())

        print("Enter Source Image Path")
        src = input()

        message = encMessage #*****
        print("Enter Destination Image Path")
        dest = input()
        print("Encoding...")
        Encode(src, message.decode(), dest)
        print("Message before decoding",message,type(message))



        #Decode
        print("Decoding...")
        img = Image.open('newDataLSB.png', 'r')
        array = np.array(list(img.getdata()))

        if img.mode == 'RGB':
            n = 3
        elif img.mode == 'RGBA':
            n = 4

        total_pixels = array.size // n

        hidden_bits = ""
        for p in range(total_pixels):
            for q in range(0, 3):
                hidden_bits += (bin(array[p][q])[2:][-1])

        hidden_bits = [hidden_bits[i:i + 8] for i in range(0, len(hidden_bits), 8)]

        message = ""
        for i in range(len(hidden_bits)):
            if message[-5:] == "$t3g0":
                break
            else:
                message += chr(int(hidden_bits[i], 2))
        if "$t3g0" in message:
            print("Hidden Message:", message[:-5])
            decMessage = fernet.decrypt(encMessage).decode()
            print("Message after decryption:",decMessage)
        else:
            print("No Hidden Message Found")


Stego()
