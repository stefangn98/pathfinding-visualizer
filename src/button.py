import pygame
import colors

pygame.font.init()


class Button:
    def __init__(self, x, y, color, text, label):
        self.x = x
        self.y = y
        self.width = 90
        self.height = 30
        self.color = color
        self.clicked = False
        self.font = pygame.font.SysFont("comicsans", 25)
        self.text = self.font.render(text, 1, colors.WHITE)
        self.label = label   # could be just for debugging; could leave it till the end
        self.width = self.text.get_width() + 10

    def update(self, display):
        if self.clicked:
            pygame.draw.rect(display, colors.BLACK, (self.x-2,
                                                     self.y-2, self.width+4, self.height+4), 0)
        pygame.draw.rect(display, self.color,
                         (self.x, self.y, self.width, self.height), 0, border_radius=5)
        display.blit(self.text, (self.x + (self.width//2 - self.text.get_width()//2),
                                 self.y + (self.height//2 - self.text.get_height()//2)))

    def is_clicked(self, pos):
        within_x = pos[0] > self.x and pos[0] < self.width + self.x
        within_y = pos[1] > self.y and pos[1] < self.height + self.y
        if within_x and within_y:
            self.clicked = True
            return True
        return False
