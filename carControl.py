import vrep
import time
import numpy as np
from math import cos, sin
from scipy.linalg import expm,logm



# ======================================================================================================= #
# ======================================= Start Simulation ============================================== #
# ======================================================================================================= #

# Close all open connections (Clear bad cache)
vrep.simxFinish(-1)
# Connect to V-REP (raise exception on failure)
clientID = vrep.simxStart('127.0.0.1', 19997, True, True, 5000, 5)
if clientID == -1:
	raise Exception('Failed connecting to remote API server')

# ======================================== Setup "handle"  =========================================== #
result, lineTracerBase=vrep.simxGetObjectHandle(clientID, "LineTracerBase", vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for lineTracerBase')
result, leftSensor=vrep.simxGetObjectHandle(clientID, "LeftSensor", vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for LeftSensor')
result, middleSensor=vrep.simxGetObjectHandle(clientID, "MiddleSensor", vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for MiddleSensor')
result, rightSensor=vrep.simxGetObjectHandle(clientID, "RightSensor", vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for RightSensor')
result, leftJoint=vrep.simxGetObjectHandle(clientID, "LeftJoint", vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for LeftJoint')
result, rightJoint=vrep.simxGetObjectHandle(clientID, "RightJoint", vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for RightJoint')
result, leftJointDynamic=vrep.simxGetObjectHandle(clientID, "DynamicLeftJoint", vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for DynamicLeftJoint')
result, rightJointDynamic=vrep.simxGetObjectHandle(clientID, "DynamicRightJoint", vrep.simx_opmode_blocking)
if result != vrep.simx_return_ok:
	raise Exception('could not get object handle for DynamicRightJoint')

nominalLinearVelocity=0.15
wheelRadius=0.027
interWheelDistance=0.119

'''
# Print object name list
result,joint_name,intData,floatData,stringData = vrep.simxGetObjectGroupData(clientID,vrep.sim_appobj_object_type,0,vrep.simx_opmode_blocking)
print(stringData)
'''

vrep.simxStartSimulation(clientID, vrep.simx_opmode_oneshot)
while(1):
    """ Read the sensors:"""
    sensorReading=[False,False,False]
    sensorReading[0]=(vrep.simxReadVisionSensor(clientID, leftSensor, vrep.simx_opmode_oneshot)[1]==1)
    sensorReading[1]=(vrep.simxReadVisionSensor(clientID, middleSensor, vrep.simx_opmode_oneshot)[1]==1)
    sensorReading[2]=(vrep.simxReadVisionSensor(clientID, rightSensor, vrep.simx_opmode_oneshot)[1]==1)
    isRed = False
    if vrep.simxReadVisionSensor(clientID, middleSensor, vrep.simx_opmode_oneshot)[2]:
        isRed=(vrep.simxReadVisionSensor(clientID, middleSensor, vrep.simx_opmode_oneshot)[2][0][6]>0.9)
        if(isRed == True):
            print("STOP")
            linearVelocityRight=0
            linearVelocityLeft=0
            vrep.simxSetJointTargetVelocity(clientID, leftJointDynamic, linearVelocityLeft/(wheelRadius), vrep.simx_opmode_oneshot)
            vrep.simxSetJointTargetVelocity(clientID, rightJointDynamic, linearVelocityRight/(wheelRadius), vrep.simx_opmode_oneshot)
            break
    # Set the sensor indicators:
    # Decide about left and right velocities:
    linearVelocityLeft=nominalLinearVelocity
    linearVelocityRight=nominalLinearVelocity
    if (sensorReading[0]==False):
        linearVelocityLeft=linearVelocityLeft*0.1
    if (sensorReading[2]==False):
        linearVelocityRight=linearVelocityRight*0.1
        # Now make it move!
    vrep.simxSetJointTargetVelocity(clientID, leftJointDynamic, linearVelocityLeft/(wheelRadius), vrep.simx_opmode_oneshot)
    vrep.simxSetJointTargetVelocity(clientID, rightJointDynamic, linearVelocityRight/(wheelRadius), vrep.simx_opmode_oneshot)

# Wait two seconds
time.sleep(5)
# **************************************************************************************************** #

# Stop simulation
vrep.simxStopSimulation(clientID, vrep.simx_opmode_oneshot)
# Before closing the connection to V-REP, make sure that the last command sent out had time to arrive. You can guarantee this with (for example):
vrep.simxGetPingTime(clientID)
# Close the connection to V-REP
vrep.simxFinish(clientID)
print("==================== ** Simulation Ended ** ====================")

# ======================================================================================================= #
# ======================================== End Simulation =============================================== #
# ======================================================================================================= #
