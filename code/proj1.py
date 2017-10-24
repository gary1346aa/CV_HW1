from my_imfilter import my_imfilter
from vis_hybrid_image import vis_hybrid_image
from normalize import normalize
from gauss2D import gauss2D
import numpy as np
import matplotlib.image as mpimg
from PIL import Image
import matplotlib.pyplot as plt
import scipy
import os

''' Setup '''
main_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

source1 = ['dog','cat','bicycle','motorcycle','bird','plane','fish','submarine','einstein','marilyn','test1']
source2 = ['cat','dog','motorcycle','bicycle','plane','bird','submarine','fish','marilyn','einstein','test2']
cut_freq  = [7,15,10,5,9,12,10,4,2,3,6];



for name1, name2, cut in zip(source1,source2,cut_freq) :
    
    image1 = mpimg.imread(main_path + '/data/' + name1 +'.bmp')
    image2 = mpimg.imread(main_path + '/data/' + name2 +'.bmp')
    image1 = image1.astype(np.single)/255
    image2 = image2.astype(np.single)/255
    
    cutoff_frequency = cut
    gaussian_filter = gauss2D(shape=(cutoff_frequency*4+1,cutoff_frequency*4+1), sigma = cutoff_frequency)
    
    low_frequencies = my_imfilter(image1, gaussian_filter)
    high_frequencies = image2 - my_imfilter(image2, gaussian_filter)
    hybrid_image = normalize(low_frequencies + high_frequencies)
    
    ''' Visualize and save outputs '''
    plt.figure(1)
    plt.imshow(low_frequencies)
    plt.figure(2)
    plt.imshow(high_frequencies+0.5)
    vis = vis_hybrid_image(hybrid_image)
    plt.figure(3)
    plt.imshow(vis)
    plt.imsave(main_path+'/results/low_frequencies ' + name1 +'.png', low_frequencies, 'quality', 95)
    plt.imsave(main_path+'/results/high_frequencies ' + name2 + '.png', high_frequencies + 0.5, 'quality', 95)
    plt.imsave(main_path+'/results/hybrid_image ' + name1 + '_' + name2 +'.png', hybrid_image, 'quality', 95)
    plt.imsave(main_path+'/results/hybrid_image_scales ' + name1 + '_' + name2 +'.png', vis, 'quality', 95)
    plt.show()


    
  