# Movement (XRRobot)

Your first step is movement. The black robots work through a system called ROS (while there is control through GPIO pins, ROS is easier) The robot is running ROS 1 Melodic for reference. As referenced by the github provided in Getting Connected, there should be basic controls under `~/catkin_ws/src/basic_navigation/src`.

For other references, see:

https://docs.ros.org/en/api/geometry_msgs/html/msg/Twist.html (This is the format that the movement commands will take)

https://www.theconstructsim.com/ros-qa-053-how-to-move-a-robot-to-a-certain-point-using-twist/


## Task
Just as was done with the blue robot, build a program that will navigate the black robot in a 5 x 5 meter box, this time using ROS.