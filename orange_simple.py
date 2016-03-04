"""
Orange.py
A program that should output an 8x8 bitmap of an orange
Written in a mostly linear fashion to figure out how to write a bitmap by hand
By Alan Jacon (AlfalfaScout)
27 Feb 2016
"""
orange = "" #The hex string that will be written to the file

#Generate the header
orange += "424D" #0, BM prefix
orange += "66000000" #2, file size placeholder
orange += "00000000" #6, reserved
orange += "46000000" #10, pixel array location in hex
orange += "28000000" #14, header size
orange += "08000000" #18, image width
orange += "08000000" #22, image height
orange += "0100" #26, number of color planes
orange += "0400" #28, number of bits per pixel
orange += "00000000" #30, compression (none)
orange += "40000000" #34, size of image in bytes
orange += "130B0000" #38, print resolution ??
orange += "130B0000" #42, print resolution ??
orange += "04000000" #46, hopefully this means 4 palette colors
orange += "04000000" #50, hopefully this means 4 important colors

#Color palette
orange += "FFFFFF00" #54, (0) white
orange += "0096FF00" #58, (1) orange
orange += "00D8FF00" #62, (2) yellow
orange += "00985800" #66, (3) green

#Image data, vertically flipped
orange += "00111100"
orange += "01111110"
orange += "11111111"
orange += "12111111"
orange += "11121111"
orange += "12111111"
orange += "01212110"
orange += "00131100"

#Write the hex values to the file as bytes
with open('orange.bmp', 'wb') as orange_file:
    orange_file.write(bytearray.fromhex(orange))
