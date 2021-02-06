Here is my CNN source code and my Q learning algorithms.
The Convolutional Neural Networks uses 2 Convolutional and Max pooling layers to detect high-level features such as edges and curves,
which is fed into the Neural Network. Convolutions slide kernels (a square matrix of pixels) over a preprocessed image. Each kernel can detect a specific
high-level feature, depending on the weights of the pixels in it. An elementwise multiplication 
and sum is performed, which means each pixel in the image is multiplied by the weight/pixel in the kernel. This is then added to an output matrix. 

This is convolution: the 3x3 kernel slides over the 5x5 image, and the weights in the kernel and the pixels of the original image are multiplied and summed.
The final result then goes into an output matrix. 

![Alt Text](https://media.giphy.com/media/i4NjAwytgIRDW/giphy.gif)


I have achieved around 70% accuracy with the kaggle cats-and-dogs dataset with 3 epochs.

The Q learning algorithm has 2 versions - terminal and fire. The fire version allows you to edit the maze in a graphical user interface
(python turtle), which makes the maze-making far easier. You can click on squares/states to give a negative reward when the agent moves into that 
square/state. This is like setting the square on fire. 

The terminal version runs in your terminal. You can change the map of the maze
by adjusting the Feasibility and Reward Matrix; F[a,b] = 1 means that the agent can move from state a to state b. R[a,b] = 10 means the agent
receives a reward of +10 when it goes from state a to state b. 

The algorithm works by allowing the agent to start at a random point in the maze, then having it make random actions until it reaches the destination.
It records the action and reward in a Q matrix, where it stores all its experience and can use that data to make smarter decisions in the future. This happens
1000 times and the agent shows the best possible path through the maze

For more information, check out my YT channel: https://www.youtube.com/channel/UCc4aOjr2slK0zZnk6O7Qj9w