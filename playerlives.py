import pygame

class LivesManager:
    def __init__(self, lives=3, respawn_pos=(640,360), invul_seconds=1.5):
        self.lives = lives
        self.respawn_pos = pygame.Vector2(respawn_pos)
        self.invul_seconds = invul_seconds
        self.invul_timer = 0.0

    def hit(self):
        if self.invul_timer > 0:
            return True  # still alive, ignore hit
        self.lives -= 1
        self.invul_timer = self.invul_seconds
        return self.lives > 0

    def update(self, dt):
        if self.invul_timer > 0:
            self.invul_timer = max(0.0, self.invul_timer - dt)

    def is_invulnerable(self):
        return self.invul_timer > 0

    def is_dead(self):
        return self.lives <= 0

    def respawn(self, player):
        player.position = self.respawn_pos.copy()
        player.velocity = pygame.Vector2(0, 0)
        self.invul_timer = self.invul_seconds

    def render(self, screen, font):
        text = f"Lives: {self.lives}"
        surf = font.render(text, True, "black")
        screen.blit(surf, (10, 10))