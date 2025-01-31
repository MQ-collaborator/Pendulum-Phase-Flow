# Pendulum Phase Flow
 Visuals and ODE solutions for a damped pendulum

This project was created to put together numerical solutions for the motion of a damped pendulum. Initial Conditions are easily changeable.

The motion of a damped torsional (rotating) pendulum can be described by: 

![image](https://github.com/user-attachments/assets/aa0f7cb8-e971-4985-8d0d-9516de069cbc)

Where I is moment of inertia, and tau is analagous to mg/l in a conventional pendulum. The current iteration of the project does not consider forced motion (caused by cosine term), but only damped motion. Restoring force is proportional to angular displacement and a drag/resistance term is added which is proportional to angular velocity. 

The file 'phasespacependulum.py' was used to create the visuals for a damped and heavily damped pendulum. These images have on the x axis angular displacment from equilibrium and on the y axis angular velocity. The vector field plotted (arrows) shows the direction in which the system would move based on its current conditions. 
Using the above second order linear differential equation SOLDE (excluding consine term) we can complete predict the state the system will evolve to given its current state. This allows us to numerically predict a future position of the system based on its current position. 
A homogenous SOLDE of this form does indeed possess analytical solutions. 
The purpose of this program is to provide a more visual guide, using easily visible physical properties (displalcement and speed in an angular sesnse) in addition to making it clear how changes in initial conditions alter how the system evolves. 
