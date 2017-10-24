# Huang Cong Yao <span style="color:red">(103000002)</span>

# Project 1 / Image Filtering and Hybrid Images

## Overview
The project is related to image filtering, github and python training.
> Build a 2D-convolution algorithm on my own, get the high/low frequencies of two images, and conbime them into a hybrid.

## Implementation
1. Image Filtering : [my_imfilter](https://github.com/gary1346aa/homework1/blob/master/code/my_imfilter.py)
	* First we collect the input/filter size in each dimension using ```shape``` (so it can process either color or grayscale images), and then calculate the padding size through calculating the floor of half number. 
	* Next we create an empty padding matrix and fill the corresponding area with the input image data, and the padding region remains zero.
	* Finally, by using loops for each dimensions, we sum up the multiplication of padding matrix and image filter using ```np.sum()```, and assign them into the corresponding output index.
	* We use the given test filtering code for validation, the result is same as native algorihm, but slightly slower.
2. Hybrid Image Generation : [proj1](https://github.com/gary1346aa/homework1/blob/master/code/proj1.py)
	* In this part, we use the completed ```my_imfilter``` to implement hybrid image.
	* First we decide the cutoff frequency of the gaussian filter.
	* Then we use the filter to collect low/high frequency filtered image of the first/second image.
	* By normalizing the sum of the above results, we can get a hybrid image.
	* I revised the code into a loop, which runs all possible pairs of images with their cutoff frequencies for convenience, and added an extra pair of image for validation.

## Installation
* Other required packages.
* How to compile from source?	
> Simply run ```proj1```.
### Results

<table border=1>
<tr>
<td><p>Dog Cat</p></td>
<td><img src="low_frequencies dog.png" width="90%"/><p>low frequency dog</p></td>
<td><img src="high_frequencies cat.png" width="90%"/><p>high frequency cat</p></td>
<td><img src="hybrid_image dog_cat.png" width="90%"/><p>hybrid image</p></td>
</tr>

<tr>
<td><p>Cat Dog</p></td>
<td><img src="low_frequencies cat.png" width="90%"/><p>low frequency cat</p></td>
<td><img src="high_frequencies dog.png" width="90%"/><p>high frequency dog</p></td>
<td><img src="hybrid_image cat_dog.png" width="90%"/><p>hybrid image</p></td>
</tr>

<tr>
<td><p>Plane Bird</p></td>
<td><img src="low_frequencies plane.png" width="90%"/><p>low frequency plane</p></td>
<td><img src="high_frequencies bird.png" width="90%"/><p>high frequency bird</p></td>
<td><img src="hybrid_image plane_bird.png" width="90%"/><p>hybrid image</p></td>
</tr>

<tr>
<td><p>Bird Plane</p></td>
<td><img src="low_frequencies bird.png" width="90%"/><p>low frequency bird</p></td>
<td><img src="high_frequencies plane.png" width="90%"/><p>high frequency plane</p></td>
<td><img src="hybrid_image bird_plane.png" width="90%"/><p>hybrid image</p></td>
</tr>

<tr>
<td><p>Bicycle Motorcycle</p></td>
<td><img src="low_frequencies bicycle.png" width="90%"/><p>low frequency bicycle</p></td>
<td><img src="high_frequencies motorcycle.png" width="90%"/><p>high frequency motorcycle</p></td>
<td><img src="hybrid_image bicycle_motorcycle.png" width="90%"/><p>hybrid image</p></td>
</tr>

<tr>
<td><p>Motorcycle Bicycle</p></td>
<td><img src="low_frequencies motorcycle.png" width="90%"/><p>low frequency motorcycle</p></td>
<td><img src="high_frequencies bicycle.png" width="90%"/><p>high frequency bicycle</p></td>
<td><img src="hybrid_image motorcycle_bicycle.png" width="90%"/><p>hybrid image</p></td>
</tr>

<tr>
<td><p>Fish Submarine</p></td>
<td><img src="low_frequencies fish.png" width="90%"/><p>low frequency fish</p></td>
<td><img src="high_frequencies submarine.png" width="90%"/><p>high frequency submarine</p></td>
<td><img src="hybrid_image fish_submarine.png" width="90%"/><p>hybrid image</p></td>
</tr>

<tr>
<td><p>Submarine Fish</p></td>
<td><img src="low_frequencies submarine.png" width="90%"/><p>low frequency submarine</p></td>
<td><img src="high_frequencies fish.png" width="90%"/><p>high frequency fish</p></td>
<td><img src="hybrid_image submarine_fish.png" width="90%"/><p>hybrid image</p></td>
</tr>

<tr>
<td><p>Einstein Marilyn</p></td>
<td><img src="low_frequencies einstein.png" width="90%"/><p>low frequency einstein</p></td>
<td><img src="high_frequencies marilyn.png" width="90%"/><p>high frequency marilyn</p></td>
<td><img src="hybrid_image einstein_marilyn.png" width="90%"/><p>hybrid image</p></td>
</tr>

<tr>
<td><p>Marilyn Einstein</p></td>
<td><img src="low_frequencies marilyn.png" width="90%"/><p>low frequency marylyn</p></td>
<td><img src="high_frequencies einstein.png" width="90%"/><p>high frequency einstein</p></td>
<td><img src="hybrid_image marilyn_einstein.png" width="90%"/><p>hybrid image</p></td>
</tr>

<tr>
<td><p>Man Cat</p></td>
<td><img src="low_frequencies test1.png" width="90%"/><p>low frequency man</p></td>
<td><img src="high_frequencies test2.png" width="90%"/><p>high frequency cat</p></td>
<td><img src="hybrid_image test1_test2.png" width="90%"/><p>hybrid image</p></td>
</tr>
