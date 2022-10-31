# Object Detection Phase

In this phase, you will be learning about transfer learning, as well as a SLAM algorithm to help determine where an object is located.

## Transfer Learning

The first step will be learning about transfer learning. Transfer learning allows us to use pre-existing and pre-trained networks as a starting point for our specific tasks, which will help reduce the amount of time we have to spend doing so. You can find a tutorial on it here. [https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html#](https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html#). If you want to learn more about transfer learning itself, rather than just how to do it, more info can be found here (https://cs231n.github.io/transfer-learning/)[https://cs231n.github.io/transfer-learning/]. The first tutorial will teach you more about how you can do it, while the one below will be more helpful in the project.

[Transfer Learning for Project](https://towardsdatascience.com/training-yolo-for-object-detection-in-pytorch-with-your-custom-dataset-the-simple-way-1aa6f56cf7d9)

Once you have successfully trained the network to find and mark your objects, you are done with this section!

## ORB-SLAM

ORB-SLAM is a SLAM (Simultaneous Localization and Mapping) algorithm that can let us do SLAM with only a single camera. This can allow us to get a good representation of our environment without having to buy expensive sensors. Read over the following repository and get it working.

[https://github.com/UZ-SLAMLab/ORB_SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3)