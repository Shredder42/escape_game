import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 1060))
pygame.display.set_caption("Escape!")
clock = pygame.time.Clock()
running = True

backdrop = pygame.image.load("images/backdrop.jpg")

while running:

    screen.blit(backdrop, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    clock.tick(60)  # frame rate in fps

pygame.quit()
