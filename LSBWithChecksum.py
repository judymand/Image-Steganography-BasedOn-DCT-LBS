#import libraries
import sys
from functools import reduce

import numpy as np
from PIL import Image
from scipy import fft
np.set_printoptions(threshold=sys.maxsize)

def checksum(st):
    return reduce(lambda x,y:x+y, map(ord, st))

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
def Decode(src,chk_sum):

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
        if(chk_sum==checksum(message[:-5])):
            print("check sum currect:",chk_sum);

    else:
        print("No Hidden Message Found")

#main function
def Stego():

    func = 1;

    if func == 1:
        print("Enter Source Image Path")
        src = input()
        print("Enter Message to Hide")
        message = input()
        chk_sum = checksum(message)
        print("The message checksum:",chk_sum)
        print("Enter Destination Image Path")
        dest = input()
        print("Encoding...")
        Encode(src, message, dest)
        print("Enter Source Image Path")
        src = input()
        print("Decoding...")
        Decode(src, chk_sum)


Stego()