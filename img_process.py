# Import packages
import base64
import numpy as np
import os
from PIL import Image
from time import strftime as sft

SAVE_PATH = './Images'

# Preprocessing function
# Input: JPEG URI image
# Output: Image array (np.ndarray, shape=(28, 28)) 
def preprocess(jpgtxt):
    # Decode URI image
    data = jpgtxt['imgURI'].split(',')[-1]
    data = base64.b64decode(data)

    # Save acquired image to "./Images/" dirtectry
    name = sft("%Y%m%d%H%M%S") # Get string of the local time (Exp: 201811010932)
    directry = SAVE_PATH
    # If "./Images" directory is not exist, making it. 
    if os.path.lexists(directry) is False:
        os.makedirs(directry)
    f = open("{}/image_{}.jpg".format(SAVE_PATH, name),'wb')       # Open file object
    f.write(data)              # Write image data to file
    f.close()                  # Close file object

    # Convert to a form suitable for input
    img = Image.open("{}/image_{}.jpg".format(SAVE_PATH, name))
    img = img.convert('L')     # Convert to glay scale
    img = img.resize((28,28))  # Resize
    img_array = np.array(img)  # Now we have image data in numpy

    threshold, upper, lower = 150., 0., 1.0                   # Binarization setting
    img_array = np.where(img_array > threshold, upper, lower) # Binarization
    img_array = np.array([[img_array]], dtype=np.float32)     # input data must be np.float32 in chainer
    return img_array
