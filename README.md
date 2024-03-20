# Automatic-Lane-Detection-using-OpenCV-python

Lane detection is a developing technology that is implemented in vehicles to enable
autonomous navigation.Most lane detection systems are designed for roads with proper
structure relying on the existence of markings. The main shortcoming of these approaches
is that they might give inaccurate results or not work at all in situations involving unclear
markings or the absence of them. The approach is based on digital image processing
techniques and purely work on vision or camera data. The main aim is to obtain a real time
curve value to assist the driver/autonomous vehicle for taking required turns and not go off
the road.
This project is about lane lines detection in an image/video with **Python and OpenCV**.
OpenCV is a package containing many useful tools to analyze images.

Here, instead of using the entire road pixels only the edges of the path are
considered. The initial steps of Capturing the image, Warping and Thresholding are as below
. 

**Initial steps :**
Thresholding and warping
1) Thresholding: : Since the approach is for the unmarked roads, Colour thresholding is
done in order to detect the color of the road instead of detecting the lane markings. The
thresholding is not applied directly on the image obtained from the video feed. Images
obtained from video feed are in BGR (Blue Green Red) format, and are converted into
HSV(Hue Saturation Value) since it is better for object or color detection. HSV color space
represents how colors behave under light. Mathematically HSV consists of three matrices
for ‘Hue’, ‘Saturation’, and ‘Value’ with ranges lying between 0-179, 0-255 and 0-255
respectively. The main application for HSV is color based image segmentation which is used
in both of the approaches for separating the road from its surroundings. Thresholding will
convert the image into a binary image i.e the area where the color of the path is detected
will be white and the rest of the part of that image will be kept black.

![image](https://github.com/vivekmorariya/Automatic-Lane-Detection-using-OpenCV-python/assets/69449048/c2f15532-058e-4e3d-b067-b80fdc675b4b)

2) Warping: : The image obtained via the camera module has an angled perspective. The
lane edges cannot be precisely located using this image as is. In order to fix this image
warping concept is used. Image warping is used to get a birds eye / top view of the path by
changing the perspective of the image. In Perspective Transformation[14], the perspective
of an image or a video frame is changed in order to get certain insights in a better way. For
warping a set of points is provided over the image. The values of these points will
determine the Region of Interest (ROI). With these two sets of points the perspective of the
image or a video frame is transformed. It is done by passing these coordinates to OpenCV
library functions. The resultant would be an image which would be cropped as per the ROI
and having a bird’s eye perspective. Warping is one of the most common preprocessing
techniques used in lane detection systems as it provides an image upon which further
calculations would be easier as compared to original image obtained through camera. The
basic idea is to get a rectangle shape when the road is straight.

A few image pre-processing procedures are performed to
get a clearer view of the path edges. The extracted edge geometry is then used to
determine the curvature using a sliding window algorithm.

1) Gaussian Blurring: : Due to uneven road conditions, the edges of the thresholded image
are too sharp. This may lead to improper edge extraction. Thus the imperfections are
smoothed out by applying a blur function to the image. Various methods are available like
averaging, bilateral filtering, Gaussian blurring and median blurring[13]. For the test case in
consideration, Gaussian blurring provided the best balance in reducing noise and
smoothing out the sharp edge imper- fections.
This algorithm scans the entire image pixels, followed by recalculating the pixel values. The
intensity of this operation is adjusted by a kernel. The greater the kernel size greater is the
blur effect but at the same time can lead to decreased details.
Gaussian blur mixes the values of the neighboring pixels depending on the distance to the
reference pixel. The pixels right next to the reference pixel get more of the colors from the
reference pixel while the pixels farther away get less of the colours. This can be viewed
graphically wherein the values closer to 0 on the x-axis have higher magnitude on the y-axis
which gradually decreases as we go further away from the center.

2. Canny edge detection:
The objective of edge recognition is to recognize the limits of articles inside pictures. A
discovery is utilized to attempt to discover areas in a picture where there is a change in
force. We can perceive a picture as a lattice or a variety of pixels. A pixel contains the light
power at some area in the picture. Every pixel's power is meant by a numeric value that
goes from 0 to 255, an power estimation of zero shows no force if something is totally dark
while 255 speaks to greatest force something being totally white.
By following out every one of these pixels, we get the edges. We will utilize this idea to
recognize the edges in our street picture.
We will load and add our picture to an exhibit: image = cv2.imread('test_image.jpg')
To change the picture over to grayscale we will initially make a duplicate of the first picture
utilizing Numpy:
**lane_image= np.copy(image)
gray=cv2.cvtColor(lane_image1,cv2.COLOR_RGB2GRAY)**

![image](https://github.com/vivekmorariya/Automatic-Lane-Detection-using-OpenCV-python/assets/69449048/eca96ff1-988b-4cae-a28c-c74d36ba3c69)

3) Image dilation: The result of the canny detection function is an image with just the edge
geometry of the path with the remaining image features removed. This needs to be passed
to a searching algorithm for detection of this geometry. But before doing so image dilation
is performed which makes the edges more clear and filled with less breaks. Dilation
expands the image pixels and adds pixels to object boundaries.

![image](https://github.com/vivekmorariya/Automatic-Lane-Detection-using-OpenCV-python/assets/69449048/fdc98a09-fcbb-4d36-94d1-4cd2bc2538a9)



