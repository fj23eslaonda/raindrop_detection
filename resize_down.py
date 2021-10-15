import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

# CHANGE IMAGES PATH
os.chdir('/home/francisco/Desktop/raindrop_problem/model2/testing_real/original_img')

# OBTAIN IMAGES NAME
os.system('ls >> ~/Desktop/raindrop_problem/model2/name_img.txt')

# CHANGE PATH AND SAVE IMAGES NAME
os.chdir('/home/francisco/Desktop/raindrop_problem/model2/')

# LOAD NAMES
list_img = open('./name_img.txt','r') 
list_img = list(list_img.read().split('\n'))


# INPUTS SIZE
width  = 1280
height = 720
number = 1

print('Loading images!\n')

# LOOP TO CHANGE SIZE OF IMAGE
for img in list_img[:-1]:
	image_o = cv2.imread('./testing_real/original_img/'+img)
	image_f = cv2.resize(image_o, (width, height), interpolation = cv2.INTER_AREA)
	cv2.imwrite('./testing_real/input_img/test_'+str(number).zfill(4)+'.png',image_f)
	number+=1

print('Images are ready!')
	

