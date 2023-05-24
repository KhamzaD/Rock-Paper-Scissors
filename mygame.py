import pygame

pygame.init()
razmer = (1000, 700)
ecran = pygame.display.set_mode(razmer)
pygame.display.set_caption("My Game")

new_razmer_1 = 100
new_razmer_2 = 100
konan = pygame.image.load("paper.png")
skala = pygame.image.load("rock.png")
nozh = pygame.image.load("scissors.png")
small_konan = pygame.transform.scale(konan, (new_razmer_1, new_razmer_2))
small_skala = pygame.transform.scale(skala, (new_razmer_1, new_razmer_2))
small_nozh = pygame.transform.scale(nozh, (new_razmer_1, new_razmer_2))

sur = (220, 220, 220)
aq = (255, 255, 255)

x, y = 200, 150
direct_x = 1
direct_y = 1

x_2, y_2 = 600, 150
direct_x2 = 1
direct_y2 = 1

x_3, y_3 = 400, 250
direct_x3 = 1
direct_y3 = 1

uaqyt = pygame.time.Clock()
V = 300
width, height = small_konan.get_size()
while True:
    ecran.fill(aq)
    uaqyt.tick(V)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    ecran.blit(small_konan, (x, y))

    x += direct_x
    y += direct_y

    if (x + width >= 1000 or x < 0):
        direct_x = - direct_x
    if (y + height >= 700 or y < 0):
        direct_y= - direct_x

    ecran.blit(small_skala, (x_2, y_2))
    x_2 += direct_x2
    y_2 += direct_y2
    if (x_2 + width >= 1000 or x_2 < 0):
        direct_x2 = -direct_x2
    if (y_2 + height >= 700 or y_2 < 0):
        direct_y2 = -direct_y2

    ecran.blit(small_nozh, (x_3, y_3))
    x_3 += direct_x3
    y_3 += direct_y3
    if (x_3 + width >= 1000 or x_3 < 0):
        direct_x3 = -direct_x3
    if (y_3 + height >= 700 or y_3 < 0):
        direct_y3 = -direct_y3

    pygame.display.update()