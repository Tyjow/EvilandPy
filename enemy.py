import pygame
import random

class Enemy(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load("assets/enemies/blue-slime.png")
        self.rect = self.image.get_rect()
        self.rect = pygame.Rect(self.rect.x, self.rect.y, 64, 64)
        self.frame_animation = 0
        self.max_frame_animation = 3
        self.frame = 80
        self.tick_animation = pygame.time.get_ticks()
        self.idle_animation = (self.frame_animation * 64, 0, 64, 64)
        self.animation_top = (self.frame_animation * 64, 128, 64, 64)
        self.animation_bottom = (self.frame_animation * 64, 0, 64, 64)
        self.animation_right = (self.frame_animation * 64, 64, 64, 64)
        self.animation_left = (self.frame_animation * 64, 192, 64, 64)
        self.rect.x = 500
        self.rect.y = 200
        self.velocity = 1
        self.list_animation = random.choice([self.move_right(), self.move_left(), self.move_top(), self.move_bottom()])
        self.time_move = 0
        self.max_time_move = 25
        self.enemy_animation = self.idle_animation
        self.tick_move = pygame.time.get_ticks()

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.health = self.max_health
            self.remove()

    def remove(self):
        self.game.all_enemies.remove(self)

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (60, 63, 60), [(self.rect.x + 11) - self.game.player.camera_X, (self.rect.y + 15) - self.game.player.camera_Y, self.max_health / 2.5, 4])
        pygame.draw.rect(surface, (111, 210, 46), [(self.rect.x + 11) - self.game.player.camera_X, (self.rect.y + 15) - self.game.player.camera_Y, self.health / 2.5, 4])

    def get_enemy_rect_width(self):
        return round(self.rect.width / 4)

    def get_enemy_rect_height(self):
        return round(self.rect.height / 4)

    def move_animation(self):
        if self.frame_animation == self.max_frame_animation:
            self.frame_animation = 0
        else:
            self.frame_animation += 1

    def move_animation_top(self):
        if self.frame_animation == 0:
            self.idle_animation = self.animation_top

        return self.frame_animation * 64, 128, 64, 64

    def move_animation_bottom(self):
        if self.frame_animation == 0:
            self.idle_animation = self.animation_bottom

        return self.frame_animation * 64, 0, 64, 64

    def move_animation_right(self):
        if self.frame_animation == 0:
            self.idle_animation = self.animation_right

        return self.frame_animation * 64, 64, 64, 64

    def move_animation_left(self):
        if self.frame_animation == 0:
            self.idle_animation = self.animation_left

        return self.frame_animation * 64, 192, 64, 64

    def move_right(self):
        self.move_animation()
        self.move_animation_right()
        self.rect.x += self.velocity

    def move_left(self):
        self.move_animation()
        self.move_animation_left()
        self.rect.x -= self.velocity

    def move_top(self):
        self.move_animation()
        self.move_animation_top()
        self.rect.y -= self.velocity

    def move_bottom(self):
        self.move_animation()
        self.move_animation_bottom()
        self.rect.y += self.velocity

    def move(self, screen):

        pygame.draw.rect(screen, (255, 0, 0), [self.rect.x - self.game.player.camera_X, self.rect.y - self.game.player.camera_Y, 64, 64], 1)

        #if not self.game.check_collision(self, self.game.player):
        time_now = pygame.time.get_ticks()

        if time_now - self.tick_animation >= self.frame:
            self.tick_animation = pygame.time.get_ticks()
            if self.time_move == self.max_time_move:
                self.time_move = 0
                self.enemy_animation = random.choice([self.move_animation_right(), self.move_animation_left(), self.move_animation_top(), self.move_animation_bottom()])
            else:
                self.time_move += 1
                if self.enemy_animation == self.move_animation_right():
                    self.move_right()
                    self.enemy_animation = self.move_animation_right()
                elif self.enemy_animation == self.move_animation_left():
                    self.move_left()
                    self.enemy_animation = self.move_animation_left()
                elif self.enemy_animation == self.move_animation_top():
                    self.move_top()
                    self.enemy_animation = self.move_animation_top()
                elif self.enemy_animation == self.move_animation_bottom():
                    self.move_bottom()
                    self.enemy_animation = self.move_animation_bottom()

        screen.blit(self.image, (self.rect.x - self.game.player.camera_X, self.rect.y - self.game.player.camera_Y), self.enemy_animation)
