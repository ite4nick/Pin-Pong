from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed

background = (200,255,255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(background)

FPS = 60
clock = time.Clock()
game = True 
finish = False

player_left = Player("Player1.png",0,200,20,70,4)
player_right = Player("Player1.png",544,200,20,70,4)
ball = GameSprite("ping_pong.png",200,200,50,50,4)

font.init()
font = font.SysFont("Arial", 35)
lose_left = font.render("Left Lose!", True, (100,0,0))
lose_right = font.render("Right Lose!", True, (100,0,0))

speed_x = 5
speed_y = 5

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False


    if not finish:
        window.fill(background)
        player_left.update_left()
        player_right.update_right()
        ball.rect.x += speed_x
        ball.rect.y += speed_y


        if sprite.collide_rect(player_left, ball) or sprite.collide_rect(player_right, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y <0:
            speed_x *= 1
            speed_y *= -1
        if ball.rect.x < -50:
            finish = True
            window.blit(lose_left, (200,200))
        if ball.rect.x > win_width:
            finish = True
            window.blit(lose_right, (200,200))
        player_left.reset()
        player_right.reset()
        ball.reset()
    display.update()
    clock.tick(FPS)
         

