#recreation of 3b1b phase space diagram for a pendulum but for E5 mechanical resonance
#This is for unforced pendulum (well represented by vector field)
#Forced pendulum would require a 3d input space in which vector field sits
#That is, simply damped motion ( no forcing)

# This code has not yet been modified to accomodate forcedpendulum - to do task
# Need to add a function of time to make ODE non homogeneous
import numpy as np
import matplotlib.pyplot as plt

THETA_0 = np.pi * 2/ 3
THETA_DOT_0 = 0
#tau is constant of proportionality between angular diplacement and angular acceleration (analagous to spring constant in a mass spring system)
TAU = 5
#B is the constant of proportionality between angular velocity and opposing torque (like drag coefficient in mass spring system)
B= 10

#moment of inertia of pendulum
#analagous to mass in a mass-spring system
IPEND=20


#solve ODE
def get_theta_doubledot(theta,thetadot):
    return (-TAU*theta - B*thetadot)/IPEND

def time_theta_doubledot(theta,thetadot, t=0):
    return (-TAU*theta - B*thetadot)/IPEND
#create a meshgrid onto which we will overlay vector field

x,y = np.meshgrid(np.linspace(-5,5,20),np.linspace(-3,3,20))

u = y

v = get_theta_doubledot(x,y)

#plot a general path through phase space using a small time interval
def main():
    #optionally take use input for duration of phase flow and precision used
    #interval = int(input("Time inverval considered: "))
    #deltat = float(input("Delta t:"))
    interval = 10000
    deltat= 0.0001
    points = round(interval/deltat)
    path = np.zeros((points,2))
    path[0,0] = THETA_0
    path[0,1] = THETA_DOT_0
    for i in range(points-1):
        theta = path[i,0]
        theta_dot=path[i,1]

        theta+=theta_dot*deltat
        theta_dot+=deltat*time_theta_doubledot(theta, theta_dot,i)

        path[i+1,0] = theta
        path[i+1,1] = theta_dot
    #print(path)

    plt.plot(path[:,0], path[:,1])
    plt.xlabel("Angle theta in radian")
    plt.ylabel("Angular Velocity")
    plt.quiver(x,y,u,v)
    plt.show()

main()


