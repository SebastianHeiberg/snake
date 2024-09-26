class Head:
    def __init__(self, rect, pygame_module):
        self.rect = rect
        self.pygame = pygame_module

    def move(self, direction):
        if direction == "up":
            self.rect.move_ip(0, -1)
        elif direction == "down":
            self.rect.move_ip(0, 1)
        elif direction == "left":
            self.rect.move_ip(-1, 0)
        elif direction == "right":
            self.rect.move_ip(1, 0)