<h1>FlockingAlgorithm Attempt [Discontinued]</h1>
This is my own attempt at the flocking algorithm using class objects and Pygame.
<hr>
<h3>About</h3>
<hr>
<h4> Initial </h4>
I initially started with random objects moving in any random position from the center of the window. These objects carried on going past the wall, and no wall collision was implemented.
<p align='center'>
<img src='https://raw.githubusercontent.com/makiisthenes/FlockingAlgorithm/master/video.gif' width=40%>
</p>
<h4> Wall Collision Detection </h4>
I then implemented a wall detection, by telling the program if particle past the window size flip the direction of velocity in opposite direction but with same magnitude. But a problem is that the particles seem to be moving in a systemicatic (non-random) way.
<p align='center'>
<img src='https://raw.githubusercontent.com/makiisthenes/FlockingAlgorithm/master/video2.gif' width=40%>
</p>
<h4> Randomness Starting Point</h4>
Here I implemented a random start point using random.choice() to make it more realistic for random motion, they are in different regions surrounding the center in different angles.
<p align='center'>
<img src='https://raw.githubusercontent.com/makiisthenes/FlockingAlgorithm/master/video3.gif' width=40%>
</p>
<h4>Applying Particle Heading</h4>
Here I used the math modules asin, acos, sin and cos, in order to find out the heading of an particilur particle, I also drew a green heading line on the particle indicating thier direction, the length of each particles green line also is directly proportional to the overall magnitude of speed it is going by a scale factor x3.
<p align='center'>
<img src='https://raw.githubusercontent.com/makiisthenes/FlockingAlgorithm/master/video4.gif' width=40%>
</p>
<h4>Laws of the Algorithm</h4>
There are 3 main concepts that need to be implemented in order to make the particles move in a 'flocking' manner, the three concepts are as follows:
<ul>
  <li><strong>Cohesion</strong></li>
  <i>This concept concludes that particles in a specific range will tend to a mean distance point, where all the particles will want to bunch on, this concept was tested by making each particles registering thier postion on a database per cycle and finding all particles are in thier certain range. When all particles in thier range are found, a mean location is found and this is where we implement a driving force to that location (not implemented). However I did code a debugging version to show the lines of force to the cohesion point, shown in the gif below as red lines between the particles.</i>
  <p align='center'>
    <img src='https://raw.githubusercontent.com/makiisthenes/FlockingAlgorithm/master/cohesion.gif' width=40%>
  </p>
  <li><strong>Alignment</strong></li>
  <i>The concept here is that all particles in a certain area will follow the mean heading/ direction of the group. And so the particle will move towards that direction using a change of velocity. I did coded this, which printed the mean direction/heading the particle must turn to. The problem which I experienced is to do with the turning of these particles to the desired heading with respect to thier velocities, velocityx and velocityy and is mentioned in main problems.</i>
  <li><strong>Separation</strong></li>
  This just means that the particles have some sort of object detection and don't all munch up on one point, and seperate with thier respective 'personal space'. An object detection module was never coded, due to laziness... 
  <hr>
<h3>Final Notice</h3> 
There are of course many more challenging concepts that do pose a challenge for me, these include:
  <ul>
    <li> Particle Circle Radius</li>
    <li> Particle Radius Restricted</li>
    <li> Concept Implementation</li>
    <li> Object Detection</li>
    <li> Particle Object Avoidance</li>
    <li> Particle Calculated Trajectory</li>
    <li> Use of SUVAT Equations</li>
<hr>
<h3>Main Problems</h3>
  <h4>Direction and Velocity Sync Error</h4>
