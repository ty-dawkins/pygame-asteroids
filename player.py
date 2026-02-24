
from ast import Call
import random
import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from shot import Shot



class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_cooldown_timer = 0
        self.thrusting = False


        # in the Player class
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius           # nose
        b = self.position - forward * self.radius - right  # left wing
        c = self.position - forward * self.radius * 0.3    # rear notch (concave)
        d = self.position - forward * self.radius + right  # right wing
        return [a, b, c, d]

    def thruster_points(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 3
        base = self.position - forward * self.radius * 0.7
        tip = self.position - forward * self.radius * (1.4 + random.random() * 0.6)
        return [base - right, tip, base + right]

    def draw(self, screen):
        if self.thrusting:
            pygame.draw.polygon(screen, "orange", self.thruster_points(), LINE_WIDTH)
        pygame.draw.polygon(screen, "black", self.triangle(), LINE_WIDTH)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        self.shoot_cooldown_timer -= dt
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        self.thrusting = bool(keys[pygame.K_w])
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shoot_cooldown_timer > 0:
            return
        self.shoot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        # create a new shot and add it to the shots group
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        Shot.containers[0].add(shot)
        # implement a cooldown timer to prevent shooting too fast
