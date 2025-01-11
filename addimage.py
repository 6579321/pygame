import pygame

pygame.init( )
SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500

display_surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Adding image and background image')

background_image = pygame.transfers.scale(pygame.image.load('background.png').convert(),(SCREEN_WIDTH, SCREEN_HEIGHT))

penguin_image = pygame.transfer.scale(
    pygame.image.load('hello penguin.png').convert_alpha(), (200, 200))
penguin_react = penguin_image.get_react(center=(SCREEN_WIDTH // 2,
                                                ))

