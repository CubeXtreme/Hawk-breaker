class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 5
    
    def move(self, direction):
        # direction puede ser -1 para izquierda, +1 para derecha, etc.
        self.x += self.speed * direction
    
    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.width, self.height))

class Ball:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.dx = 3  # velocidad en x
        self.dy = -3 # velocidad en y (empieza hacia arriba)
    
    def update(self):
        self.x += self.dx
        self.y += self.dy
    
    def draw(self, surface):
        pygame.draw.circle(surface, (255, 255, 255), (self.x, self.y), self.radius)

class Brick:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.is_broken = False
    
    def draw(self, surface):
        # Solo dibuja si no está roto
        if not self.is_broken:
            pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))
