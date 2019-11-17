# 470-Robotics-Project
#### Final Project for Introduction to Robotics ECE 470: Camera Oriented Robot Navigation (CORN)

##### Team Members:
- Deniz Yildirim (dy2)
- Gus Kroll (ackroll2)
- Ayush Khanna (akhanna4)

## Project Update 1
No new code was written for this update. This update was merely a declaration of our project statement. The end goal of our project is to have a car that interacts with a robotic arm as well as multiple sensors. We would like to have the car follow some predetermined path (using sensors), reach a certain point and stop, and use the robotic arm to provide some service to the car such as changing the tires after which the car will continue on its way. For more information on the project statement, see our individual project update documents.

## Project Update 2
The main file relevant to this update is: `carControl.py`. This file contains all the code for control of the car module. In particular, this file lays out how the sensors attached to the car govern its movement. The main loop of this file takes care of constantly updating the sensor readings at each time step. The speed of the car's individual wheels is determined by the sensor readings that are passed in. If the sensors pass in readings that indicate that our car has reached a red line, then both of the car's wheels have their speed set to 0 so that the car stops and the simulation reaches its end. If the sensors detect that the car is on normal grey ground, then the car's wheels each have the same speed so that the car continues to go straight. When the sensors detect a green line, the speed of the wheels are set according to which way the green line goes so that the car will follow along the green line. For instance, if the green line turns right, then the speed of the right wheel is lowered so that the speed imbalance between the wheels causes the car to turn right along the green line. The same principle applies in the code for left turns as well.
Note that the other files in this commit/update are used to setup the V-Rep python API and were generated automatically. Also, `example.py` was merely for reference and has not yet been used to implement any new functionality (it will be modified in later updates).

## Project Update 3
The main file relevant to this update is: `carControl.py`. This file contains all new code for control of the car module as well as code to control the arm for this update. In this update, we added code to handle the new sensors that we added for this update. In particular, we added code to use sensor readings from the sensor mounted on the car to tell the car when to stop. Effectively, this would allow the car to stop if it detects that there is an obstacle directly in front of it that is too close. We also added code to tell when the arm should remove the obstacle from the car's path. This was done by using an additional sensor to detect when the car had reached our first checkpoint. Finally, we added the necessary code to actually perform the removal of the obstacle by the arm.
For future updates we plan to split off the code for the arm into its own file and we also plan to design a more dynamic system for removal of obstacles. Additionally, we want to implement a more complex course for the care to traverse. We want this course to contain multiple turns and obstacles that must be either avoided or removed.

## Project Update 4
FILL THIS IN
