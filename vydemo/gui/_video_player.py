import pygame.display
import pygame.time
import pygame.surface
import pygame.event
from vydemo.giftgrab import IObserver


class VideoPlayer(IObserver):

    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.display = pygame.display.set_mode(self.size, 0)
        self.clock = pygame.time.Clock()
        self.snapshot = pygame.surface.Surface(self.size, 0, self.display)

    def run(self):
        running = True
        while running:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT or \
                   (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                    running = False

            self.clock.tick()

    def update(self, image):
        print('update')
