import pygame
import math


class Projectile(pygame.sprite.Sprite):

    def __init__(self, start_x, start_y, dest_x, dest_y, player):
        super().__init__()
        self.velocity = 10
        self.player = player

        self.image = pygame.Surface([4, 4])
        self.image.fill((0, 0, 0))

        self.rect = self.image.get_rect()

        self.rect.x = start_x
        self.rect.y = start_y

        self.floating_point_x = start_x
        self.floating_point_y = start_y

        x_diff = dest_x - start_x
        y_diff = dest_y - start_y
        angle = math.atan2(y_diff, x_diff)

        self.change_x = math.cos(angle) * self.velocity
        self.change_y = math.sin(angle) * self.velocity

    def remove(self):
        self.player.all_projectiles.remove(self)

    def move(self):
        self.floating_point_y += self.change_y
        self.floating_point_x += self.change_x

        self.rect.y = int(self.floating_point_y)
        self.rect.x = int(self.floating_point_x)

        for enemy in self.player.game.all_enemies:
            if self.player.game.check_collision_projectile(self, enemy):
                self.remove()
                enemy.damage(self.player.attack)

        if self.rect.x < 0 or self.rect.x > 1344 or self.rect.y < 0 or self.rect.y > 768:
            self.remove()
