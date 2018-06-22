import os
from _io import open

class Bitmap:
    def read_file(self, filename):
        file = open(filename, "rb")
        try:
            filesize = os.path.getsize(filename)
            print("Reading from", filename)
            print("File size", filesize)
            self.byte_array = bytearray(file.read(filesize)) #main reading in bmp
            self.width = self.convertToInteger(reversed(self.byte_array[18:22]))
            print("width" , self.width)
            self.height = self.convertToInteger(reversed(self.byte_array[22:26]))
            print("height" , self.height)
            self.data_offset = self.convertToInteger(reversed(self.byte_array[10:14]))
            print("data offset address" , self.data_offset)
        finally:
            file.close()
    
    def convertToInteger(self, array):
        sum = 0
        for value in array:
            sum = sum * 256
            sum = sum + value
        return sum

    def get_pixel(self, row, col):
        offset = self.data_offset + (row * self.width + col) * 3
        red = self.byte_array[offset + 2]
        green = self.byte_array[offset + 1]  
        blue = self.byte_array[offset + 0]
        return(red, green, blue)

    def write_file(self, filename):
        file = open(filename, "wb") 
        try:
            file.write(self.byte_array)
        finally:
            file.close()

#   def flip_horizontal(self):
#         half_width = int(self.width / 2)
#         for r in range(0, self.height):
#             for c in range(0, half_width, 3):
#                 r1, c1 = r, c
#                 offset1 = self.get_offset(r1,c1)
#                 
    
    def increase_brightness(self, factor):
        brightness_factor = 1 + factor
        for r in range(0, self.height):
            for c in range(0, self.width):
                red, green, blue = self.get_pixel(r, c)
                red, green, blue = red * brightness_factor, green + brightness_factor, blue + brightness_factor
                if red > 255:
                    red = 255
                if green > 255:
                    green = 255
                if blue > 255:
                    blue = 255
                self.set_pixel(r, c, int(red), int(green), int(blue))
    
    #grayscalevalues in brightness (r+g+b) / 3 the value to r,g,b
bitmap = Bitmap()
bitmap.read_file("test.bmp")
print("Pixel 0,0", bitmap.get_pixel(299, 199))
bitmap.write_file("new.bmp")


# try:
#     filesize = os.path.getsize(filename)
#     print("File size", filesize)
#     byte_array = bytearray(file.read(filesize))
#     print(byte_array[0], byte_array[1])
#    computed_file_size = convertToInteger(reversed(byte_array[2:6]))
   
#   print("computed file size", computed_file_size)
#    width = convertToInteger(reversed(byte_array[18:22]))
#    print("width" , width)
#   height = convertToInteger(reversed(byte_array[22:26]))
#    print("height" , height)
#    data_offset = convertToInteger(reversed(byte_array[10:14]))
#    print("data offset address" , data_offset)   
#    print(get_color(byte_array, data_offset, width, height, 0, 199))
#print(byte_array)
# finally:
#         file.close()
    