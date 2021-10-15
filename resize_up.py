import cv2
import os

# OBTAIN IMAGES NAME
os.chdir('/home/francisco/Desktop/raindrop_problem/model2/testing_result/output_test')
os.system('ls >> /home/francisco/Desktop/raindrop_problem/model2/out_name_img.txt')

# CREATE FOLDER
os.mkdir('/home/francisco/Desktop/raindrop_problem/model2/testing_result/original_test/')

# INPUTS SIZE
width  = 3840
height = 2160
number = 0

# LOAD OUTPUT IMAGES NAME
os.chdir('/home/francisco/Desktop/raindrop_problem/model2')
list_img = open('./out_name_img.txt','r')
list_img = list(list_img.read().split('\n'))

# LOAD IMAGES NAME
name_img = open('./name_img.txt','r')
name_img = list(name_img.read().split('\n'))

print('Loading images!\n')

# RESIZE IMAGE
for img in list_img[:-1]: 
	image_o = cv2.imread('/home/francisco/Desktop/raindrop_problem/model2/testing_result/output_test/'+img)
	image_f = cv2.resize(image_o, (width, height), interpolation = cv2.INTER_AREA)
	cv2.imwrite('/home/francisco/Desktop/raindrop_problem/model2/testing_result/original_test/'+name_img[number]+'.png',image_f)
	number+=1

print('Images are ready!')
	
	
