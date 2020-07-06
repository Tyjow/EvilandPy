import pygame
from projectile import Projectile

class Player(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load("assets/characters/mage.png")
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(self.rect.x, self.rect.y, 64, 64)
        self.rect.x = 400
        self.rect.y = 500
        self.frame_animation = 0
        self.max_frame_animation = 3
        self.frame = 120
        self.tick_animation = pygame.time.get_ticks()
        self.idle_animation = (self.frame_animation * 64, 128, 64, 64)
        self.animation_top = (self.frame_animation * 64, 128, 64, 64)
        self.animation_bottom = (self.frame_animation * 64, 0, 64, 64)
        self.animation_right = (self.frame_animation * 64, 64, 64, 64)
        self.animation_left = (self.frame_animation * 64, 192, 64, 64)
        self.player_projectile_X = 0
        self.player_projectile_Y = 0
        self.camera_X = 0
        self.camera_Y = 0

    def launch_projectile(self):
        pos = pygame.mouse.get_pos()
        mouse_x = pos[0]
        mouse_y = pos[1]

        projectile = Projectile((self.rect.x + self.player_projectile_X) - self.camera_X, (self.rect.y + self.player_projectile_Y) - self.camera_Y, mouse_x, mouse_y, self)

        self.all_projectiles.add(projectile)

    def get_player_rect_width(self):
        return round(self.rect.width / 4)

    def get_player_rect_height(self):
        return round(self.rect.height / 4)

    def move_right(self):
        # if not self.game.check_collision(self, self.game.all_monsters):
        self.rect.x += self.velocity
        self.camera_X += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
        self.camera_X -= self.velocity

    def move_top(self):
        self.rect.y -= self.velocity
        self.camera_Y -= self.velocity

    def move_bottom(self):
        self.rect.y += self.velocity
        self.camera_Y += self.velocity

    def move_animation(self):
        time_now = pygame.time.get_ticks()

        if time_now - self.tick_animation >= self.frame:
            self.tick_animation = pygame.time.get_ticks()
            if self.frame_animation == self.max_frame_animation:
                self.frame_animation = 0
            else:
                self.frame_animation += 1

    def move_animation_top(self):
        self.move_animation()
        if self.frame_animation == 0:
            self.idle_animation = self.animation_top
            self.player_projectile_X = 0
            self.player_projectile_Y = 0

        return self.frame_animation * 64, 128, 64, 64

    def move_animation_bottom(self):
        self.move_animation()
        if self.frame_animation == 0:
            self.idle_animation = self.animation_bottom
            self.player_projectile_X = 64
            self.player_projectile_Y = 0

        return self.frame_animation * 64, 0, 64, 64

    def move_animation_right(self):
        self.move_animation()
        if self.frame_animation == 0:
            self.idle_animation = self.animation_right
            self.player_projectile_X = 64
            self.player_projectile_Y = 16

        return self.frame_animation * 64, 64, 64, 64

    def move_animation_left(self):
        self.move_animation()
        if self.frame_animation == 0:
            self.idle_animation = self.animation_left
            self.player_projectile_X = 0
            self.player_projectile_Y = 16

        return self.frame_animation * 64, 192, 64, 64
