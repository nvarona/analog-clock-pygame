import sys
import pygame
from analog import AnalogClock

pygame.init()

# Definicion de variables ----------------
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
LIGHT_BLUE = (225, 239, 240)

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Analogic Clock  v1.3")

clock = pygame.time.Clock()
analog_clock = AnalogClock(250, (300, 300), WINDOW_WIDTH, WINDOW_HEIGHT)

# Main Loop
while True:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # 2. Updating
    analog_clock.update()

    # 3. Drawing Objects
    window.fill(LIGHT_BLUE)
    analog_clock.draw(window)

    pygame.display.update()
    clock.tick(15)
