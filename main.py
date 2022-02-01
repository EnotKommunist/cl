import requests
import pygame


response = requests.get("https://static-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&ll=133.694111,-25.757718&spn=40.006457,0.00619&l=map")
if response:
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    img_file = open('photo.png', 'wb')
    img_file.write(response.content)
    img_file.close()
    bg_surf = pygame.image.load("photo.png")
    screen.blit(bg_surf, (0, 0))
    clock = pygame.time.Clock()
    screen.blit(bg_surf, (0, 0))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(bg_surf, (0, 0))
        pygame.display.update()
    pygame.display.quit()

    pygame.quit()