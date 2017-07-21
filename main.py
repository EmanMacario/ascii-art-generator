from PIL import Image
import os

# Get directory containing images for conversion
image_dir = os.path.join(os.getcwd(), 'Images') 

# Open the image and get its width and height
img = Image.open(os.path.join(image_dir, 'ethan.jpeg'))
img_width, img_height = img.size

# Now, convert the image to grayscale then get its new (r,g) array
img = img.convert('LA')
pix = img.load()

# A character map, where characters are sorted in such a way that associates 
# with increasing grayscale intensity i.e light to dark
CHARMAP = " .,:;ox%#@"


####################
## Helper Functions
####################

def get_grayscale_intensities(pix, dim):
	"""Takes a 2D pixel array storing (r,g) values for an image and the image 
	   dimensions as input, and returns a 2D matrix storing the 
	   grayscale intensity for a pixel (or pixel area)."""

	# Initialise the grayscale intensity array
	gscale_int = [[0 for i in range(dim[0])] for j in range(dim[1])]

	print(dim[0], dim[1])

	# Calculate the grayscale intensity for each pixel
	for i in range(dim[0]):
		for j in range(dim[1]):
			gscale_int[i][j] = sum(pix[i,j])/2

	return gscale_int


def convert_charmap():
	pass




def print_ascii_image(matrix):
    """Takes a 2D matrix of ASCII values as input and prints out an image
       of ASCII characters based on matrix values."""
    for row in matrix:
        for i in range(len(row)):
            if (i != len(row)-1):
                print(chr(row[i]), end='')
            else:
                print(chr(row[i]))
    return



print(get_grayscale_intensities(pix, (img_width, img_height)))





img.show()