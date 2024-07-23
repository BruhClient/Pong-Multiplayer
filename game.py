import pygame.rect


class Paddle :
    def __init__(self,x,y,barrier,paddle_width):
        self.rect = pygame.Rect(x,y,paddle_width,10)
        self.color = (255,255,255)
        self.lower_limit_x = barrier[0]
        self.upper_limit_x = barrier[1]


    def movePaddle(self,dx):
        new_x = self.rect.x + dx
        if new_x > self.upper_limit_x - self.rect.width or new_x < self.lower_limit_x:
            dx = 0

        self.rect.x += dx





    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect,0,3,)



class Ball:
    def __init__(self,center,speed):
        self.start_pos = center
        self.color = (255,255,255)
        self.rect = pygame.Rect(0,0,10,10)
        self.rect.center = center
        self.dx = -speed
        self.dy = speed

    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect,0,10)

    def updatePos(self,center):

        self.rect.center = center

    def update(self):


        self.rect.x += self.dx
        self.rect.y += self.dy

    def collided(self,rects,screen_width):

        if self.rect.x <= 0 :
            self.dx *= -1
        if self.rect.x >= screen_width - self.rect.width :
            self.dx *= -1



        if self.rect.y > 600 - self.rect.height or self.rect.y <= 0 :
            self.rect.center = self.start_pos
            self.dy  *= -1



        rect1 = pygame.Rect(self.rect.x + self.dx ,self.rect.y + self.dy ,self.rect.width,self.rect.height)
        for rect in rects :
            if rect1.colliderect(rect) :
                if rect1.bottom >  rect.top  :
                    self.rect.y +=  rect1.bottom -rect.top
                    self.dy *= -1









class Game:
    def __init__(self,gameId):
        self.player1 = None
        self.player2 = None
        self.player1 = (50,50)
        self.player2 = (100,100)
        self.ball = ()
        self.ball_dx = 0
        self.ball_dy = 0
        self.score = (0,0)
        self.active = False

    def startGame(self):
        if self.player1 is True and self.player2 is True :
            self.active = True

    def connectPlayer(self,player):
        if player == 1 :
            self.player1_connected = True
        if player == 2 :
            self.player2_connected = True






