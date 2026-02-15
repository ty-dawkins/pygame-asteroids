
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
		center = (int(self.position.x), int(self.position.y))
		pygame.draw.circle(screen, "black", center, int(self.radius), LINE_WIDTH)

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
		a3 = Asteroid(self.position.x, self.position.y, new_radius)
		#add third fragment with opposite velocity to the original

		# assign velocities to fragments
		a1.velocity = vel1
		a2.velocity = vel2



