Here is my CNN source code. I'd recommend looking at the cat_dog folder and running Cat-Dog1.py
It's the one I've worked on the most and is the best one.

The Convolutional Neural Networks uses 2 Convolutional and Max pooling layers to detect high-level features such as edges and curves,
which is fed into the Neural Network. 

![Alt Text](https://miro.medium.com/max/2510/1*vkQ0hXDaQv57sALXAJquxA.jpeg)

Convolutions slide kernels (a square matrix of pixels) over a preprocessed image. Each kernel can detect a specific
high-level feature, depending on the weights of the pixels in it. An elementwise multiplication 
and sum is performed, which means each pixel in the image is multiplied by the weight/pixel in the kernel. This is then added to an output matrix. 

This is convolution: the 3x3 kernel slides over the 5x5 image, and the weights in the kernel and the pixels of the original image are multiplied and summed.
The final result then goes into an output matrix. 

![Alt Text](https://media.giphy.com/media/i4NjAwytgIRDW/giphy.gif)

These output matrixes are input into the fully connected hidden layers of the Neural Network, and through backpropagation the weights and biases of the hidden layers will adjust so that the NN reduces its loss and improves its accuracy.


![Alt Text](https://community.alteryx.com/t5/image/serverpage/image-id/42339i8BA3F2CCCEDE7458?v=1.0.png)

I have achieved around 70% accuracy with the kaggle cats-and-dogs dataset with 3 epochs.

