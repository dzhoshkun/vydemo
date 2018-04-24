import pygame


class App(object):

    def __init__(self, worker):
        self.worker = worker

    def run(self):
        pygame.init()
        self.worker.run()
        pygame.quit()
