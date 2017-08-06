from PIL import Image
import os

# Get directory containing images for conversion
image_dir = os.path.join(os.getcwd(), 'Images') 

# Open the image and get its width and height
img = Image.open(os.path.join(image_dir, 'ethan.jpeg'))
img_width, img_height = img.size

print(img_width, img_height)

# Now, convert the image to grayscale then get its new (r,g) array
img = img.convert('LA')
pix = img.load()

# A character map, where characters are sorted in such a way that associates 
# with increasing grayscale intensity i.e light to dark
CHARMAP = " .,:;ox%#@"


####################
# HELPER FUNCTIONS #
####################

def get_grayscale_intensities(pix, img_width, img_height):
	"""Takes a 2D pixel array storing (r,g) values for an image and a 2-tuple
	   containing image dimensions as input, and returns a 2D nested list 
	   storing the grayscale intensity for a pixel (or pixel area)."""

	# Initialise the grayscale intensity array
	gscale_int = [[0 for i in range(img_width)] for j in range(img_height)]

	# Calculate the grayscale intensity for each pixel
	for i in range(img_height):
		for j in range(img_width):
			gscale_int[i][j] = sum(pix[j,i])/2

	return gscale_int



def get_min_max_gi(gscale_int):
    """Takes a 2D array of grayscale intensities and returns a 2-tuple which
    respectively contains the lowest and highest grayscale intensities in
    the entire matrix."""
    max_gi = max([max(gi) for gi in gscale_int])
    min_gi = min([min(gi) for gi in gscale_int])

    return min_gi, max_gi
   


def convert_to_char_matrix(gscale_int, charmap):
	"""Converts a 2D grayscale intensity matrix into a character matrix."""

	# Get the min and max grayscale intensities
	min_gi, max_gi = get_min_max_gi(gscale_int)

	# Calculate the difference between them
	diff = max_gi - min_gi

	# Now, for each pixel, we will assign an index to it which refers to the
    # specific character that will represent it from the character map
	for row in gscale_int:
		for i in range(len(row)):
			row[i] = int((row[i] - min_gi)/diff*(len(charmap)-1))
    
	return gscale_int



def print_ascii_image(char_matrix, charmap):
    """Takes a 2D matrix of ASCII values as input and prints out an image
       of ASCII characters based on matrix values."""
    for row in char_matrix:
        for i in range(len(row)):
            if (i != len(row)-1):
                print(charmap[row[i]], end='')
            else:
                print(charmap[row[i]])
    return


# MAIN PROGRAM
if __name__ == '__main__':

    # Obtain the grayscale intensity for each pixel in the image
    gscale_int = get_grayscale_intensities(pix, img_width, img_height)

    # Convert the grayscale intensity values to integer 
    # values, denoting ASCII character values
    char_matrix = convert_to_char_matrix(gscale_int, CHARMAP)

    # Now, print out the image as ASCII art
    print_ascii_image(char_matrix, CHARMAP)

    # Job done!