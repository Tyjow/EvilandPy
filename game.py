import pygame
from player import Player
from enemy import Enemy


class Game:

    def __init__(self):
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.all_enemies = pygame.sprite.Group()
        self.pressed = {}
        self.spawn_enemy()

    def update(self, screen):

        player_animation = self.player.idle_animation

        if self.pressed.get(
                pygame.K_d) and self.player.rect.x > 0:
            """self.player.rect.x + self.player.get_player_rect_width() < screen.get_width()"""
            player_animation = self.player.move_animation_right()
            self.player.move_right()
        if self.pressed.get(pygame.K_a) and self.player.rect.x > 0:
            player_animation = self.player.move_animation_left()
            self.player.move_left()
        if self.pressed.get(pygame.K_w) and self.player.rect.y > 0:
            player_animation = self.player.move_animation_top()
            self.player.move_top()
        if self.pressed.get(
                pygame.K_s) and self.player.rect.y > 0:
            """self.player.rect.y + self.player.get_player_rect_height() < screen.get_height()"""
            player_animation = self.player.move_animation_bottom()
            self.player.move_bottom()

        for projectile in self.player.all_projectiles:
            projectile.move()

        for enemy in self.all_enemies:
            enemy.move(screen)
            enemy.update_health_bar(screen)

        """for i, s in enumerate(self.player.top):
            screen.blit(s, [i * 64, 128])
            pygame.draw.rect(screen, (0, 0, 0), [i * 64, 128, 64, 64], 1)"""
        pygame.draw.rect(screen, (255, 0, 0), [self.player.rect.x - self.player.camera_X, self.player.rect.y - self.player.camera_Y, 64, 64], 1)
        screen.blit(self.player.image, (self.player.rect.x - self.player.camera_X, self.player.rect.y - self.player.camera_Y), player_animation)

        self.player.all_projectiles.draw(screen)

        #self.all_enemies.draw(screen)

    def spawn_enemy(self):
        self.all_enemies.add(Enemy(self))

    def check_collision(self, sprite, sprite_2):
        return sprite.rect.colliderect(pygame.Rect(sprite_2.rect.x, sprite_2.rect.y, 64, 64))

    def check_collision_projectile(self, sprite, sprite_2):
        return sprite.rect.colliderect(sprite_2.rect)
