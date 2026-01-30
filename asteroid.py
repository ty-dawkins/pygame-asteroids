#Create a new class called Asteroid in a new file called asteroid.py that inherits from CircleShape.
#Give it a constructor with this signature:
#def __init__(self, x, y, radius):

#Override the draw() method to draw the asteroid using the pygame.draw.circle function. It accepts:
#The "surface" to draw on (the screen object)
#The color of the circle ("white")
#Its own position as the center
#Its own radius
#The width of the line to draw the circle (use LINE_WIDTH from constants.py)
#Override the update() method so that it moves in a straight line at constant speed. On each frame, it should add (self.velocity * dt) to its position (get self.velocity from its parent class, CircleShape).
#In main.py before the game loop starts, create a new empty pygame.sprite.Group for the asteroids.
#Like we did with the Player class, set the static containers field of the Asteroid class to the new asteroids group, as well as the updatable and drawable groups. This ensures that every instance of the Asteroid class is automatically added to these groups upon creation.
from collections.abc import Set
import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS



class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		# draw a circle at the asteroid's position with its radius
		# pygame.draw.circle accepts a center as (x, y) tuples or Vector2
		center = (int(self.position.x), int(self.position.y))
		pygame.draw.circle(screen, "white", center, int(self.radius), LINE_WIDTH)

	def update(self, dt):
		# move in a straight line at constant speed
		self.position += self.velocity * dt

	#add new .split() method  immediataly .kill() itself
	def split(self):
		# remove this asteroid from all groups
		self.kill()
		# log event
		log_event("asteroid_split")

		# compute new radius for fragments
		new_radius = self.radius - ASTEROID_MIN_RADIUS
		# if the resulting fragments would be too small, don't spawn them
		if new_radius <= 0:
			return

		# randomly choose a direction offset between 20 and 50 degrees
		angle = random.uniform(20, 50)

		# rotate the current velocity to produce two new velocity vectors
		vel1 = self.velocity.rotate(angle) * 1.2
		vel2 = self.velocity.rotate(-angle) * 1.2

		# create two new asteroid fragments at the same position
		a1 = Asteroid(self.position.x, self.position.y, new_radius)
		a2 = Asteroid(self.position.x, self.position.y, new_radius)

		# assign velocities to fragments
		a1.velocity = vel1
		a2.velocity = vel2

#Otherwise, we need to spawn 2 new asteroids like so:
#Call log_event("asteroid_split") (be sure to import log_event at the top of the file).
#Call random.uniform to generate a random angle between 20 and 50 degrees (be sure to import the standard random library at the top of the file).
#Call the .rotate method on the asteroid's velocity vector to create a new vector representing the first new asteroids movement.
#Call the .rotate again for the second new asteroid, but this time rotate it in the opposite direction (negative angle).
#Compute the new radius of the smaller asteroids using the formula old_radius - ASTEROID_MIN_RADIUS.
#Create two new Asteroid objects at the current asteroid position with the new radius.
#Set the first's .velocity to the first new vector, but make it move faster by scaling it up (multiplying) by 1.2.
#Do the same for the second asteroid, but with the second new vector.
#In the game loop in main.py, replace asteroid.kill() with asteroid.split().





