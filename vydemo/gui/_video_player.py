import pygame.display
import pygame.time
import pygame.image
import pygame.event
from vydemo.giftgrab import IObserver


class VideoPlayer(IObserver):

    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.display = pygame.display.set_mode(self.size, 0)
        self.clock = pygame.time.Clock()
        self.running = False

    def run(self):
        if self.running:
            return
        self.running = True
        while self.running:
            events = pygame.event.get()
            for e in events:
                if e.type == pygame.QUIT or \
                   (e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE):
                    self.running = False

            self.clock.tick()

    def update(self, image):
        if not self.running:
            return
        # TODO: FORMAT
        surface = pygame.image.frombuffer(image.data.transpose(1, 0, 2).ravel(),
                                          image.shape,
                                          'RGB')
        self.display.blit(surface, (0, 0))
        pygame.display.flip()
