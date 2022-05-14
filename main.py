from pygame import *

window = display.set_mode((1000, 700))
display.set_caption("Shooting Game")

class Sprite(sprite.Sprite):
    def __init__(self, img, x, y, width, height,speed):
        super().__init__()

        self.img = img
        self.x = x
        self.y = y
        self.speed = speed
        self.width = width
        self.height = height

        self.img = transform.scale(image.load(self.img).convert_alpha(), (self.width, self.height))

        self.rect = self.img.get_rect()
        self.rect.w = 70 
        self.rect.h = 50
        self.rect.x = self.x
        self.rect.y = self.y

    def reset(self):
        self.rect.x = self.x + 15
        self.rect.y = self.y + 30

        window.blit(self.img, (self.x, self.y))
        
class Player1(Sprite):
    def movement(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_w] and player1.y >= 10:
            player1.y -= player1.speed
        if key_pressed[K_s] and player1.y <= 550:
            player1.y += player1.speed
            
            
            
            
class Player2(Sprite):
    def movement(self):
        key_pressed = key.get_pressed()

        if key_pressed[K_UP] and player2.y >= 10:
            player2.y -= player2.speed
        if key_pressed[K_DOWN] and player2.y <= 550:
            player2.y += player2.speed
            
player1 = Player1('square.png', 10, 10 , 60, 150, 10)
player2 = Player2('square.png', 940, 10 , 60, 150, 10)
            
            
running = True
finish = False
clock = time.Clock()
FPS = 100

while running:
    window.fill((200, 200, 200))

    keystroke = key.get_pressed()

    print(player1.y)


    if not finish:
        player1.reset()
        player2.reset()
        player1.movement()
        player2.movement()
        pass

    for i in event.get():
        if i.type == QUIT:
            finish = True
            running = False


    display.update()
    clock.tick(FPS)

            
            
            
            
            
