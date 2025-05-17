from PIL import Image
from helper_functions import Octree, gaussian_kernel, clamp

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
    img = Image.open(imgPath)
    w, h = img.size
    ot = Octree()
    for row in range(h):
        for col in range(w):
            r, g, b = img.getpixel((col, row))
            ot.insert(r, g, b)
    ot.reduce(256)

    for row in range(h):
        for col in range(w):
            r, g, b = img.getpixel((col, row))
            nr, ng, nb = ot.find(r, g, b)
            img.putpixel((col, row), (nr, ng, nb))

    img.show()
    output_path = "output/"+imgName+"_quantized.bmp"
    img.save(output_path)
    return img
    
# Reference: https://medium.com/@rohit-krishna/coding-gaussian-blur-operation-from-scratch-in-python-f5a9af0a0c0f
def blur(imgPath, size, sigma, dog=False):
    img = Image.open(imgPath).convert("RGB")
    width, height = img.size
    pixels = img.load()
 
    if size % 2 == 0:
        raise ValueError("Kernel size must be odd")
    kernel = gaussian_kernel(size, sigma)
    offset = size // 2		

    # Create new image for output
    new_img = Image.new('RGB', (width, height))
    new_pixels = new_img.load()

    # Apply convolution to each pixel
    for y in range(offset, height - offset):
        for x in range(offset, width - offset):
            r_sum = g_sum = b_sum = 0

            for ky in range(size):
                for kx in range(size):
                    nx = x + kx - offset
                    ny = y + ky - offset
                    r, g, b = pixels[nx, ny]
                    weight = kernel[ky][kx]
                    r_sum += r * weight
                    g_sum += g * weight
                    b_sum += b * weight

            new_pixels[x, y] = (
                clamp(r_sum),
                clamp(g_sum),
                clamp(b_sum)
            )

    # Copy border pixels
    for y in range(height):
        for x in range(width):
            if x < offset or x >= width - offset or y < offset or y >= height - offset:
                new_pixels[x, y] = pixels[x, y]
            
    new_img.show()
    output_path = "output/"+imgName+"_blurred.bmp"
    new_img.save(output_path)
    return new_img

# Also known as Difference of Gaussians 
# Subtracting pixel by pixel of an image applied with larger gauss kernel with smaller
def edge_detection(imgPath):
    # Apply two types of Gauss on the same image with different kernel sizes
    # Subtract the results to detect edges (Difference of Gaussians)
    img = Image.open(imgPath).convert("RGB")
    
    # Apply Gaussian blur with smaller kernel
    small_blur = blur(imgPath, 3, 1.0)
    small_pixels = small_blur.load()
    
    # Apply Gaussian blur with larger kernel
    large_blur = blur(imgPath, 5, 2.0) 
    large_pixels = large_blur.load()
    
    # Create output image
    w, h = img.size
    output = Image.new('RGB', (w,h))
    output_pixels = output.load()
    
    # Calculate difference between blurs
    for x in range(w):
        for y in range(h):
            r1,g1,b1 = small_pixels[x,y]
            r2,g2,b2 = large_pixels[x,y]
            
            # Take absolute difference for each channel
            diff_r = abs(r1 - r2)
            diff_g = abs(g1 - g2)
            diff_b = abs(b1 - b2)
            
            # Amplify the differences to make edges more visible
            output_pixels[x,y] = (
                clamp(diff_r * 2),
                clamp(diff_g * 2), 
                clamp(diff_b * 2)
            )
    
    output.show()
    output_path = "output/"+imgName+"_edges.bmp"
    output.save(output_path)
    return output      
    

if __name__ == "__main__":
    # Create a normal user interface for terminal, so they can select image/filter
    while True:
        print("===== Image Filtertron 3000 =====")
        imgName = input("Enter the name of the image you want to filter (w/o extension): ")
        if imgName == "q":
            break
        
        current_path = "input/"+imgName+".bmp"
        keep_filtering = True
        while keep_filtering:
            print("1. Quantizer")
            print("2. Blur") 
            print("3. Edge Detection")
            filter = input("Enter the number of the filter you want to apply: ")
            
            if filter == "1":
                quantizer(current_path)
            elif filter == "2":
                blurStrength = int(input("Select odd kernel size (3,5,7...): "))
                blur(current_path, blurStrength, blurStrength/3)
            elif filter == "3":
                edge_detection(current_path)
            else:
                print("Invalid filter")
                
            cont = input("Would you like to apply another filter to this image? (y/n): ")
            if cont.lower() != 'y':
                keep_filtering = False    
