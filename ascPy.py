from PIL import Image, ImageFilter
import numpy

try:
	myImg = Image.open("samples/coke.jpg")
	print("Image loaded successfully!")
	width, height = myImg.size
	print("Image size: " + str(width) + " x " + str(height))
except IOError:
	print("Image failed to load")

newSize = width * .1, height * .1
myImg.thumbnail(newSize, Image.ANTIALIAS)


imgMatrix = numpy.asarray(myImg)

'''
print("Iterating through pixel contents...")
for x in range(len(imgArr)):
	for y in range(len(imgArr[x])):
		print(imgArr[x][y])
'''

brightnessMatrix = []
for row in imgMatrix:
	brightnessRow = []
	for pixel in row:
		brightness = numpy.mean(pixel[0] + pixel[1] + pixel[2])
		brightnessRow.append(brightness)
	brightnessMatrix.append(brightnessRow)

# ASCII characters: `^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$
# Brightness values should be betwee 0 and 255. There are 67 characters.
# So, 256 brightness values / 67 characters = 3.8 values per character
# Brightness (B) 0 would match Character (C) `
# B255 = $
# B128 = u
# So it's the B value divided by the value per character number (3.8), rounded up

characters = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
length = len(characters)
print("length: " + str(length))

asciiMatrix = []
for row in brightnessMatrix:
	asciiRow = []
	for pixel in row:
		# print("pixel: " + str(pixel)) 
		# print("ceiling: " + str(math.ceil(pixel / (255/length))))
		ascii = characters[int(pixel / 255 * length) - 1]
		# print("ascii: " + ascii)
		asciiRow.append(ascii)
	asciiMatrix.append(asciiRow)

for row in asciiMatrix:
	line = [p + p + p for p in row]
	print("".join(line))

#myImg.show()

