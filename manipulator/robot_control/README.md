# Robot Control

In this phase, you will be working with the physical robot, and getting it to move. The goal for this phase of the project, is to be able to move the robot to an arbitrary position, as well as being able to get the location of the end effector, using the current angles of the robot.

## Forward Kinematics

Forward kinematics can be used to find the current position of the end effector of the robot, using only the angles the robot is currently at, as well as the length of each segment. Find the forward kinematic equations for the robot, and try finding the end position of a few different orientations. Make note of the formula, since it will be important for future tasks.

## Inverse Kinematics

Inverse kinematics can be used to figure out what angles the robot should be in order to have it's end effector as at arbitrary position. One way of finding the angles that are required for a position is a 'Monte Carlo' approach. [Learn more about Monte Carlo](https://towardsdatascience.com/an-overview-of-monte-carlo-methods-675384eb1694). Try making a Monte Carlo simulation to find the angles for some random points.

## Using the robot

Now that you can find where the end of the robot is, as well as calculating the required angles to go to a position, it's time to try it on the robot. Write a control program that given a coordinate, the robot can move from it's current position to the given coordinate. You can find some info on the robot in the Direct Lab robot repository. [Link to the repository.](https://github.com/DIRECTLab/robots/tree/master/green-manipulators).

## Picking up an object

Now that you can move the robot and have code to move to a given position, try writing a program to pick up an object. The object should be in the same position every time for this stage.