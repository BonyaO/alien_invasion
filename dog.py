import pygame


class Dog:
    """A dog class"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load('images/dog.bmp')
        self.rect = self.image.get_rect()

        # Start new dog image at bottom left corner of screen
        self.rect.bottomleft = self.screen_rect.bottomleft

    def blitme(self):
        """Draw the dog at its current location"""
        self.screen.blit(self.image, self.rect)
