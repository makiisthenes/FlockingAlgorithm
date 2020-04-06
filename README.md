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
  <li>Cohesion</li>
  <li>Alignment</li>
  <li>Alignment</li>
