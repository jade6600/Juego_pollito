
import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi pollito amarillito")

# Colores
NEGRO = (0, 0, 0)
GRIS = (100, 100, 100)
VERDE = (34, 139, 34)
BLANCO = (255, 255, 255)
ROJO = (200, 0, 0)

# Clase para las casas
class Casa(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect(topleft=(x, y))

# Crear grupo de casas
casas = pygame.sprite.Group()
for i in range(5):
    casas.add(Casa(30, 30 + i / 60))
    casas.add(Casa(ANCHO - 100, 30 + i / 60))



# Bucle principal
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    pantalla.fill(VERDE)

    # Dibujar dos carreteras (una arriba y otra más abajo)
    pygame.draw.rect(pantalla, GRIS, (0, 200, ANCHO, 60)) # primera carretera
    pygame.draw.rect(pantalla, GRIS, (0, 340, ANCHO, 60)) # segunda carretera

    # Dibujar líneas blancas en ambas carreteras
    for i in range(0, ANCHO, 35):
        pygame.draw.line(pantalla, BLANCO, (i, 230), (i + 20, 230), 3)
        pygame.draw.line(pantalla, BLANCO, (i, 370), (i + 20, 370), 3)

    # Dibujar las casas
    casas.draw(pantalla)

    # Actualizar pantalla
    pygame.display.flip()
   

# Salir del juego
pygame.quit()
sys.exit()
