import numpy as np
def my_imfilter(image, imfilter):

    '''
    Input:
        image: A 3d array represent the input image.
        imfilter: The gaussian filter.
    Output:
        output: The filtered image.
    '''
    ###################################################################################
    # TODO:                                                                           #
    # This function is intended to behave like the scipy.ndimage.filters.correlate    #
    # (2-D correlation is related to 2-D convolution by a 180 degree rotation         #
    # of the filter matrix.)                                                          #
    # Your function should work for color images. Simply filter each color            #
    # channel independently.                                                          #
    # Your function should work for filters of any width and height                   #
    # combination, as long as the width and height are odd (e.g. 1, 7, 9). This       #
    # restriction makes it unambigious which pixel in the filter is the center        #
    # pixel.                                                                          #
    # Boundary handling can be tricky. The filter can't be centered on pixels         #
    # at the image boundary without parts of the filter being out of bounds. You      #
    # should simply recreate the default behavior of scipy.signal.convolve2d --       #
    # pad the input image with zeros, and return a filtered image which matches the   #
    # input resolution. A better approach is to mirror the image content over the     #
    # boundaries for padding.                                                         #
    # Uncomment if you want to simply call scipy.ndimage.filters.correlate so you can # 
    # see the desired behavior.                                                       #
    # When you write your actual solution, you can't use the convolution functions    #
    # from numpy scipy ... etc. (e.g. numpy.convolve, scipy.signal)                   #
    # Simply loop over all the pixels and do the actual computation.                  #
    # It might be slow.                                                               #
    ###################################################################################
    ###################################################################################
    # NOTE:                                                                           #
    # Some useful functions                                                           #
    #     numpy.pad or numpy.lib.pad                                                  #
    # #################################################################################
    
    # Uncomment if you want to simply call scipy.ndimage.filters.correlate so you can 
    # see the desired behavior.

    #import scipy.ndimage as ndimage
    #output = np.zeros_like(image)
    #for ch in range(image.shape[2]):
    #    output[:,:,ch] = ndimage.filters.correlate(image[:,:,ch], imfilter, mode='constant')
    
    output = np.zeros_like(image) #Create output matrix of the same size as input image
   
    ix, iy, iz = image.shape #Collect the input size in each dimension
    fx, fy = imfilter.shape  #Collect the filter size in each dimension
    px, py = fx//2, fy//2    #Calculate the padding length of each dimension
   
   
    pimage = np.zeros((ix+2*px, iy+2*py, iz)) #Create a new matrix for zero-padding
   
    for z in range(iz):
        pimage[:, :, z] = np.pad(image[:, :, z], ((px, px), (py, py)), 'constant', constant_values=0)#Copy and Fill the new matrix
   
   
    for x in range(ix):
        for y in range(iy):
            for z in range(iz):
                output[x,y,z] = np.sum(imfilter*pimage[x:x+fx, y:y+fy, z]) #Filtering zero-padding matrix with imfilter
    
    
    ###################################################################################
    #                                 END OF YOUR CODE                                #
    ###################################################################################
    return output
