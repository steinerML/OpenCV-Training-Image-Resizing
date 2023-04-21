# OpenCV Image Resizing.
Image resizing using OpenCV.
## Contents :

Various interpolation techniques come into play to accomplish these operations. Several methods are available in OpenCV, the choice typically depends on the particular application.
I have used the following functions/methods:

| Function        |Action                                                                        | 
|----------------:|------------------------------------------------------------------------------|
|cv2.imread()     | Read the image using imread() function.|
|**cv2.resize()**    | Resizes image according to given parameters.                 |
|     **src**    |  It is the required input image, it could be a string with the path of the input image.                                                             |
|    **dsize** |    It is the desired size of the output image, it can be a new height and width.                                                 |
|     **fx**      |  Scale factor along the horizontal axis.                     |
|     **fy**         |  Scale factor along the vertical axis.                                     |
|     **interpolation**   |  It gives us the option of different methods of resizing the image.                                             |
|     **isColor**     |  If not zero, the encoder will expect and encode color frames. Else it will work with grayscale frames.|


## Test Image used: 
I have used bugatti.jpg that can be found in the repository.

![Source Image Sequence](https://github.com/steinerML/OpenCV-Training-Image-Resizing/blob/main/bugatti.jpg)


## Summary:

```python
#Resizes image by given amount (downscaling)
resize_down = cv2.resize(image, down_points, interpolation= cv2.INTER_LINEAR)
```

```python
# Resizes image by given amount (upscaling)
resized_up = cv2.resize(image, up_points, interpolation = cv2.INTER_LINEAR)

```
```python
# Resizing using scaling factor
 
scaled_f_down = cv2.resize(image, None, fx= scale_down, fy= scale_down, interpolation= cv2.INTER_LINEAR)
scaled_f_up = cv2.resize(image, None, fx= scale_up_x, fy= scale_up_y, interpolation= cv2.INTER_LINEAR)

```

