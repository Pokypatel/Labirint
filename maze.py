#создай игру "Лабиринт"!
from pygame import *

class Wall():
    def __init__(self, color_red, color_green, color_blue, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_red = color_red
        self.color_green = color_green
        self.color_blue = color_blue
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_red, color_green, color_blue))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))
    def upravlenie(self):
        keys = key.get_pressed()
        if keys[K_a]:
            self.rect.x -= self.speed
        if keys[K_d]:
            self.rect.x += self.speed
        if keys[K_w]:
            self.rect.y -= self.speed
        if keys[K_s]:
            self.rect.y += self.speed
    '''def dvizvraga(self):
        if self.rect.x <= #добавить координаты врага нижнего
            self.direction = 'right'
        elif self.rect.x >= #добавить координаты врага нижнего
            self.direction = 'left'

        if self.direction == 'right':
            self.rect.x += self.speed
        elif self.direction == 'left':
            self.rect.x -= self.speed'''
        

#стены создать
stena_1 = Wall(255, 242, 24, 100, 100, 10, 400)
stena_2 = Wall(255, 242, 24, 100, 100, 650, 10)
stena_3 = Wall(255, 242, 24, 200, 300, 10, 400)
stena_4 = Wall(255, 242, 24, 300, 200, 350, 10)
stena_5 = Wall(255, 242, 24, 750, 100, 10, 400)

igrok = GameSprite('hero.png', 25, 300, 3)
'''vrag = gameSprite('cyborg.png', x, y, 5)'''
okno = display.set_mode((900, 600))
display.set_caption('Догонялки')

clock = time.Clock()
FPS = 60

background = transform.scale(image.load('background.jpg'), (900, 600))

game = True
while game:
    
    okno.blit(background, (0, 0))
    stena_1.draw_wall()
    stena_2.draw_wall()
    stena_3.draw_wall()
    stena_4.draw_wall()
    stena_5.draw_wall()
    igrok.reset()
    igrok.upravlenie()

    for e in event.get():
        if e.type == QUIT:
            game = False

    '''if sprite.collide_rect(igrok, vrag):
        igrok.rect.x = 25
        igrok.rect.y = 225
    if sprite.collide_rect'''



    clock.tick(FPS)
    display.update()