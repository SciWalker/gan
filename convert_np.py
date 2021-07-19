from PIL import Image
import os
import numpy as np

images_path = "../../dataset/gt_db/"    
np_array = []

GENERATE_RES = 3  # Generation resolution factor
GENERATE_SQUARE = 32 * GENERATE_RES  # rows/cols (should be square)
IMAGE_CHANNELS = 3
def conv_npy_two_tiers(images_path):
    np_array = []
    for root,direc,files in os.walk(images_path):
        for directory in direc:
            for index, file in enumerate(os.listdir(root+'/'+directory)):
                    image = Image.open(root+'/'+directory+'/'+file).resize((GENERATE_SQUARE, GENERATE_SQUARE), Image.ANTIALIAS)
                    np_array.append(np.asarray(image))
    np_array = np.reshape(np_array, (-1, GENERATE_SQUARE, GENERATE_SQUARE, IMAGE_CHANNELS))
    np_array = np_array.astype(np.float32)
    np_array = np_array / 127.5 - 1.

    np.save('images.npy', np_array)
     
def conv_npz(images_path):
    np_array = []
    #save images as npz
    for root,direc,files in os.walk(images_path):
        for directory in direc:
            for index, file in enumerate(os.listdir(root+'/'+directory)):
                single_im = Image.open(root+'/'+directory+'/'+file)
                single_array = np.array(single_im)
                np_array.append(single_array)            



conv_npy_two_tiers(images_path)
#np.savez("saved_images.npz",np_array)