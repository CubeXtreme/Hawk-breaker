import pygame
import sys
from game_objects import Paddle, Ball, Brick


# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

def main():
    # Inicializar Pygame
    pygame.init()
    
    # Crear la ventana
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Brick Breaker - ¡Hola, mundo!")
    
    # Reloj para controlar FPS
    clock = pygame.time.Clock()
    
    # Bucle principal del juego
    running = True
    while running:
        # Manejo de eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Lógica del juego
        
        # Dibujar en pantalla
        screen.fill((0, 0, 0))  # Fondo negro
        pygame.display.flip()
        
        # Controlar FPS (opcional, 60 como estándar)
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
