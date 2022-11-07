# Project

Perfect, good job getting to this task! This is where a lot more autonomy will come in and require a lot more searching on your end. There are two big pieces that you will want to get acquainted with before beginning this project.

## Step 1
Location awareness is incredibly important for navigation, as you want a way to understand where your robot is relative to where it started. While this is sometimes inaccurate, this is helpful for mapping among other tasks. Thus, learn how to use odometry to understand where the robot is at any given time

## Step 2
Another important task in pathfinding is planning routes to get to the end goal. Implement an A* planner on a grid structure. This could be done on the robot itself, or on a test environment where you know the whole map a priori and have to plan from the beginning to the end.

## Object Recognition
Implement YOLO for a basic object detection algorithm. There are others as well that you may try and implement for best results.

# Project Task
Combining all of the previous tasks together, we have the penultimate task!

Do a searching algorithm to search a room for a bowl. Make sure Yolo recognizes this object. (If not, substitute it for another object that is easier for YOLO or your implemented object detection algorithm to recognize). Upon finding the object, approach it and take a picture of it. Then navigate back to the starting location.

### Additional challenge
Instead of just taking a picture of it, attempt to grab it with the arm and bring it back to the start. This may be challenging with a bowl, so feel free to use a different object as desired.