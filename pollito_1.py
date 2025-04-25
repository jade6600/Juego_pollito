import pygame
import sys

# Inicializar Pygame
pygame.init()

# Pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi pollito amarillito")

# Colores
NEGRO = (0, 0, 0)
GRIS = (100, 100, 100)
VERDE = (34, 139, 34)
BLANCO = (255, 255, 255)
ROJO = (200, 0, 0)
AMARILLO = (255, 255, 0)

# Clase Casa
class Casa(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.image.fill(ROJO)
        self.rect = self.image.get_rect(topleft=(x, y))

# Clase Pollito
class Pollito(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(AMARILLO)
        self.rect = self.image.get_rect()
        self.rect.x = 385
        self.rect.y = 220

# Crear casas
casas = pygame.sprite.Group()
x = 0
while x < ANCHO - 60:
    casas.add(Casa(x, 10))
    casas.add(Casa(x, ALTO - 70))
    x += 80

# Pollito amarillito
pollito = Pollito()
grupo_pollito = pygame.sprite.GroupSingle(pollito)


# Bucle principal
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    # Movimiento del pollito
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        pollito.rect.y -= 0.8
    if teclas[pygame.K_DOWN]:
        pollito.rect.y += 0.5

    

    pantalla.fill(VERDE)

    # Carreteras
    pygame.draw.rect(pantalla, GRIS, (0, 200, 800, 60))
    pygame.draw.rect(pantalla, GRIS, (0, 340, 800, 60))

    # Líneas blancas
    linea_x = 0
    while linea_x < ANCHO:
        pygame.draw.line(pantalla, BLANCO, (linea_x, 230), (linea_x + 20, 230), 3)
        pygame.draw.line(pantalla, BLANCO, (linea_x, 370), (linea_x + 20, 370), 3)
        linea_x += 30

    # Mostrar casas y pollito
    casas.draw(pantalla)
    grupo_pollito.draw(pantalla)

    pygame.display.flip()
    

pygame.quit()
sys.exit()