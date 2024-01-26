import pygame

def changColor(image, color):
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(color)
    
    finalImage = image.copy()
    finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
    return finalImage

pygame.init()
window = pygame.display.set_mode((300, 160))

image = pygame.image.load('./apoca.bmp').convert_alpha()
image.set_colorkey((0, 0, 0))
hue = 0

clock = pygame.time.Clock()
nextColorTime = 0
run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    color = pygame.Color(255, 124, 0)

    color_image = changColor(image, color)
    color_image.set_alpha(150)

    window.fill((96, 96, 64))
    window.blit(color_image, color_image.get_rect(center = window.get_rect().center))
    window.blit(color_image, color_image.get_rect(center = window.get_rect().center))
    window.blit(color_image, color_image.get_rect(center = window.get_rect().center))
    window.blit(color_image, color_image.get_rect(center = window.get_rect().center))
    window.blit(color_image, color_image.get_rect(center = window.get_rect().center))
    window.blit(color_image, color_image.get_rect(center = window.get_rect().center))
    window.blit(color_image, color_image.get_rect(center = window.get_rect().center))

    pygame.display.flip()

pygame.quit()
exit()