import pygame

# --- class ---

class Button(object):

    def __init__(self, position, size, imagen):


        # get image size and position
        self._rect = pygame.Rect(position, size)
        self.apretado = False
        self.imagen = imagen

    def draw(self, screen):

        # draw selected image
        screen.blit(pygame.transform.scale(pygame.image.load(self.imagen), (40, 40)), self._rect)

    def event_handler(self, event):

        # change selected color if rectange clicked
        if event.type == pygame.MOUSEBUTTONDOWN: # is some button clicked
 # is left button clicked
            if self._rect.collidepoint(event.pos): # is mouse over button
                self.apretado = True