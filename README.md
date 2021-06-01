# Image-Steganography-BasedOn-DCT-LBS
# LSB and the Discrete Cosine Transform
Imlementation of lossy image compression using DCT method (JPEG standard) and Encryption using LSB technique.

--Run DCT operation first by enter the folowing commands in the console
```bash
python DCT.py <input_file> <level_of_compression>
python DCT.py Image/car1.jpg 50 
```

 ## Overview the process
 
1. The image broken into 8x8 blocks of pixels.
2. Working from left to right, top to bottom, the DCT is applied to each block.
3. Each block is compressed through quantization.
4. The array of compressed blocks that constitute the image is stored/ transmitted in a less amount of size.
4. When desired, the image is reconstructed through decompression, using Inverse Discrete Cosine Transform (IDCT).


--Run convert to (convert JPEG to PNG)
After the DCT operation we'll need to convert the JPEG picture to PNG.

--Run the LSB operation
Supported host formats:
**PNG

Dependencies:

**numpy
**cryptography
**Pillow (PIL fork)

Run the code and follow the Instructions from the console.




