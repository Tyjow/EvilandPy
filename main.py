import pygame
import pytmx

from game import Game

pygame.init()

pygame.display.set_caption("Evil Land")
screen = pygame.display.set_mode((1344, 768))
game_map = pytmx.load_pygame('assets/Eviland.tmx')

game = Game()

clock = pygame.time.Clock()

running = True

while running:

    screen.fill(0)

    # draw map data on screen
    for layer in game_map.visible_layers:
        for x, y, gid, in layer:
            tile = game_map.get_tile_image_by_gid(gid)
            for player in game.all_players:
                screen.blit(tile, ((x * game_map.tilewidth) - player.camera_X, (y * game_map.tileheight) - player.camera_Y))

    game.update(screen)

    pygame.display.flip()

    clock.tick(60)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("Game Closed")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            game.player.launch_projectile()

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
