#Create a new Shot class to represent a bullet in a new shot.py file.
#It should also inherit from CircleShape, similar to the Asteroid class.
#Don't forget to override its draw and update methods, just like you did in the Asteroid class!
import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
	def __init__(self, x, y, radius=SHOT_RADIUS):
		super().__init__(x, y, radius)

	def draw(self, screen):
		# draw a filled small circle to represent the bullet
		center = (int(self.position.x), int(self.position.y))
		pygame.draw.circle(screen, "white", center, int(self.radius))

	def update(self, dt):
		# move in a straight line at constant speed
		self.position += self.velocity * dt

