<h1>FlockingAlgorithm [Discontinued]</h1>
This is my own attempt at the flocking algorithm using class objects and Pygame.
<hr>
<h3>About</h3>
<hr>
<h4> Initial </h4>
I initially started with random objects moving in any random position from the center of the window. These objects carried on going past the wall, and no wall collision was implemented.
<p align='center'>
<img src='https://raw.githubusercontent.com/makiisthenes/FlockingAlgorithm/master/ezgif.com-crop.gif'>
</p>
<h4> Wall Collision Detection </h4>
I then implemented a wall detection, by telling the program if particle past the window size flip the direction of velocity in opposite direction but with same magnitude. But a problem is that the particles seem to be moving in a systemicatic (non-random) way.
<p align='center'>
<img src='https://raw.githubusercontent.com/makiisthenes/FlockingAlgorithm/master/video2.gif'>
</p>
<h4> Randomness Starting Point</h4>
Here I implemented a random start point using random.choice() to make it more realistic for random motion, they are in different regions surrounding the center in different angles.
<p align='center'>
<img src='https://raw.githubusercontent.com/makiisthenes/FlockingAlgorithm/master/video3.gif'>
</p>
<h4>Applying Particle Heading</h4>
