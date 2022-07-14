import os
from os import listdir
from PIL import Image
from icecream import ic
clean_dir = os.path.join(os.path.dirname(__file__),'PetImages/Test')
'''
li = []
for filename in listdir(clean_dir):
    try:
      #ic(filename)
      img = Image.open(os.path.join(clean_dir,filename)) # open the image file
      ic(img)
      img.verify() # verify that it is, in fact an image
    except:
      li.append(filename)
li.sort()
ic(li)
'''
'''
#method 2 
import cv2
li = []
rmvd = []
IMG_SIZE = 25
for category in ["Cat","Dog"]:  # do dogs and cats
  path = os.path.join(clean_dir,category)  # create path to dogs and cats
  for img in os.listdir(path):  # iterate over each image per dogs and cats
    try:
      img_array = cv2.imread(os.path.join(path,img) ,cv2.IMREAD_GRAYSCALE)  # convert to array
      new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))  # resize to normalize data size

    except Exception as e:  # in the interest in keeping the output clean...
      ic(img)
      li.append(img)
      ic(e)
      if os.path.exists(os.path.join(path,img)):
          os.remove(os.path.join(path,img))
          rmvd.append(img)
      else:
          print(img,"does not exist")

ic(li,len(li))
ic(rmvd)
'''
'''
x = 0
import os
import tensorflow as tf
num_skipped = 0 
for folder_name in ("Cat", "Dog"):
    folder_path = os.path.join(clean_dir, folder_name)
    for fname in os.listdir(folder_path):
    #for fname in range(190):
        print(fname)      
        fpath = os.path.join(folder_path, f"{12400+fname}.jpg")
        try:
            fobj = open(fpath, "rb")
            is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
        finally:
            fobj.close()

        if not is_jfif:
            print(fname,'is not there')
            num_skipped += 1
            
            # Delete corrupted image
            os.remove(fpath)

print("Deleted %d images" % num_skipped)
'''
import os
import tensorflow as tf
num_skipped = 0
for folder_name in ("Cat", "Dog"):
    folder_path = os.path.join(clean_dir, folder_name)
    for fname in os.listdir(folder_path):
        fpath = os.path.join(folder_path, fname)
        try:
            fobj = open(fpath, "rb")
            is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
        finally:
            fobj.close()

        if not is_jfif:
            num_skipped += 1
            # Delete corrupted image
            os.remove(fpath)

print("Deleted %d images" % num_skipped)