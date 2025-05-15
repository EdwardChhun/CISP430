from PIL import Image
from helper_functions import build_and_display

def my_filter(imgPath):
	img = Image.open(imgPath) #open image
	width, height = img.size #get width and height
	pixels = img.load() # load the 2D array of pixels
	for py in range(height): #for each row
		for px in range(width): #for each column
			#get the red, green, and blue values for this pixel
			r, g, b = pixels[px, py] 

			#make the image 10% brighter
			newR = r*1.1
			newG = g*1.1
			newB = b*1.1
			#end adding your filters

			#make sure the new color values aren't too large
			if newR > 255:
					newR = 255

			if newG > 255:
					newG = 255

			if newB > 255:
					newB = 255
			#update the pixel
			pixels[px, py] = (int(newR),int(newG),int(newB))

	return img
	
def quantizer(imgPath):
	build_and_display(imgPath)
	
def blur(imgPath):
	pass

def edge_detection(imgPath):
	pass

if __name__ == "__main__":
	# Create a normal user interface for terminal, so they can select image/filter
	while True:
		print("===== Image Filtertron 3000 =====")
		imgName = input("Enter the name of the image you want to filter (w/o extension): ")
		if imgName == "q":
			break
		else:
			print("1. Quantizer")
			print("2. Blur")
			print("3. Edge Detection")
			filter = input("Enter the number of the filter you want to apply: ")
			if filter == "1":
				quantizer("input/"+imgName+".bmp")
			elif filter == "2":
				blur("input/"+imgName+".bmp")
			elif filter == "3":
				edge_detection("input/"+imgName+".bmp")
			else:
				print("Invalid filter")
