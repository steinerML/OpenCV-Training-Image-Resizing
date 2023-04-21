#Import libraries
import cv2
import numpy as np
	
# Reading image
image = cv2.imread('bugatti.jpg')

# Get original height and width
h,w,c = image.shape
print("Original Height and Width:",h,"x",w)
#Print channels
print("Channels:",c)
#Print size altogether
print('Image Size:',image.size)

#Set DOWNSIZING width and height.
down_width = 300
down_height = 200
down_points = (down_width, down_height)
resized_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)

#Set UPSCALING width and height.
up_width = 600
up_height = 400
up_points = (up_width, up_height)
resized_up = cv2.resize(image, up_points, interpolation = cv2.INTER_LINEAR)

# Scaling Up the image 1.2 times by specifying both scaling factors
scale_up_x = 1.2
scale_up_y = 1.2
# Scaling Down the image 0.6 times specifying a single scale factor.
scale_down = 0.6
scaled_f_down = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_LINEAR)
scaled_f_up = cv2.resize(image, None, fx= scale_up_x, fy= scale_up_y, interpolation= cv2.INTER_LINEAR)

# Scaling Down the image 0.6 times using different Interpolation Method
#Inter-Area
res_inter_area = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_AREA)
#Inter-Linear
res_inter_linear = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_LINEAR)
#Inter-Linear
res_inter_nearest = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_NEAREST)


#Printing images:

#By Setting width and height
cv2.imshow('Resized Down by defining height and width', resized_down)
#With scale factor
cv2.imshow('Resizing Down with Scale Factor', scaled_f_down) #resizing_by_factor
#cv2.waitKey(0)
#By Setting width and height
cv2.imshow('Resized Up image by defining height and width', resized_up)
#With scale factor
cv2.imshow('Resizing Up with Scale Factor', scaled_f_up) #resizing_by_factor

# Concatenate images in vertical axis for comparison
vertical= np.concatenate((res_inter_area, res_inter_linear, res_inter_nearest), axis = 1)
# Display the image Press any key to continue
cv2.imshow('Inter Area :: Inter Linear :: Inter Nearest ::', vertical)


#Wait 1 second and destroy All Windows
cv2.waitKey()
cv2.destroyAllWindows()
