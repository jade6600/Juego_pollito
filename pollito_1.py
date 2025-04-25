import pygame
import sys
import random
# Inicializar Pygame
pygame.init()
# Pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi pollito amarillito")
# Colores
NEGRO = (0, 0, 0)
GRIS = (112, 128, 115)
VERDE = (0, 255, 42)
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AMARILLO = (255, 247, 0)
AZUL = (0, 247, 255)
MORADOBONITO = (230, 143, 255)
ROSITAPINK = (255, 100, 167)

# Fuente
fuente = pygame.font.SysFont("arial", 30)

# Clase Casa
class Casa:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 60, 60)
        self.x = x
        self.y = y

    def dibujar(self):
        pygame.draw.rect(pantalla, ROSITAPINK, self.rect)
        punto1 = (self.x, self.y)
        punto2 = (self.x + 60, self.y)
        punto3 = (self.x + 30, self.y - 30)
        pygame.draw.polygon(pantalla, MORADOBONITO, [punto1, punto2, punto3])

# Clase Pollito
class Pollito:
    def __init__(self):
        self.rect = pygame.Rect(380, 450, 30, 30)

    def dibujar(self):
        pygame.draw.rect(pantalla, AMARILLO, self.rect)

# Clase Auto
class Auto:
    def __init__(self, x, y, velocidad):
        self.rect = pygame.Rect(x, y, 40, 30)
        self.velocidad = velocidad

    def update(self):
        self.rect.x += self.velocidad
        if self.velocidad > 0 and self.rect.left > ANCHO:
            self.rect.right = 0
        elif self.velocidad < 0 and self.rect.right < 0:
            self.rect.left = ANCHO

    def dibujar(self):
        pygame.draw.rect(pantalla, AZUL, self.rect)

# Crear casas
casas = []
x = 0
while x < ANCHO - 20:
    casas.append(Casa(x, 70))
    casas.append(Casa(x, ALTO - 130))
    x += 80

# Crear pollito
pollito = Pollito()

# Crear autos
autos = []
for i in range(4):
    autos.append(Auto(i * 200, 205, -3))
    autos.append(Auto(i * 200, 345, 3))

# Vidas y reloj
vidas = 3
tiempo_colision = 0
reloj = pygame.time.Clock()

# Bucle principal
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False

    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        pollito.rect.y -= 5
    if teclas[pygame.K_DOWN]:
        pollito.rect.y += 5

    if pollito.rect.top < 0:
        pollito.rect.top = 0
    if pollito.rect.bottom > ALTO:
        pollito.rect.bottom = ALTO

    for auto in autos:
        auto.update()

    # Colisiones
    for auto in autos:
        if pollito.rect.colliderect(auto.rect) and pygame.time.get_ticks() - tiempo_colision > 1000:
            vidas -= 1
            pollito.rect.y = 450
            tiempo_colision = pygame.time.get_ticks()
            if vidas <= 0:
                jugando = False

    # Dibujar todo
    pantalla.fill(VERDE)

    pygame.draw.rect(pantalla, GRIS, (0, 200, 800, 60))
    pygame.draw.rect(pantalla, GRIS, (0, 340, 800, 60))

    linea_x = 0
    while linea_x < ANCHO:
        pygame.draw.line(pantalla, BLANCO, (linea_x, 230), (linea_x + 20, 230), 5)
        pygame.draw.line(pantalla, BLANCO, (linea_x, 370), (linea_x + 20, 370), 5)
        linea_x += 40

    for casa in casas:
        casa.dibujar()

    for auto in autos:
        auto.dibujar()

    pollito.dibujar()

    texto_vidas = fuente.render(f"Vidas: {vidas}", True, BLANCO)
    pantalla.blit(texto_vidas, (10, 10))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
