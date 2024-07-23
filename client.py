import sys

import pygame
from game import Paddle,Ball

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60


def render_text(surface,text,font_filename,text_col,size,x,y) :
    font = pygame.font.Font(font_filename,size)
    img = font.render(text,True,text_col)
    surface.blit(img,(x,y))




# Paddles
distance_y = 50
paddle_width = 70
paddle_speed = 3
Player1 = Paddle(SCREEN_WIDTH//2 - paddle_width//2,SCREEN_HEIGHT - distance_y ,(0,SCREEN_WIDTH),paddle_width)
Player2 = Paddle(SCREEN_WIDTH//2 - paddle_width//2 ,distance_y ,(0,SCREEN_WIDTH),paddle_width)

# Ball
ball = Ball((SCREEN_WIDTH//2, SCREEN_HEIGHT//2),2.5)


# Center Line
Line_Width = 20
gap = 10
lines = SCREEN_WIDTH // (Line_Width + gap ) + 1
line_height = 5


def main() :
    run = True

    while run :
        clock.tick(FPS)
        keys = pygame.key.get_pressed()
        screen.fill((0,0,0))

        for event in pygame.event.get() :
            if event.type == pygame.QUIT:
                run = False


        dx = 0
        if keys[pygame.K_LEFT] :
            dx +=  -paddle_speed
        if keys[pygame.K_RIGHT]:
            dx += paddle_speed


        for line in range(lines) :

            pygame.draw.rect(screen,(255,255,255), pygame.Rect(line * (Line_Width + gap) ,SCREEN_HEIGHT//2 - line_height//2 ,Line_Width,line_height))
        ball.update()
        ball.collided([Player1.rect,Player2.rect],SCREEN_WIDTH)

        ball.draw(screen)
        Player1.movePaddle(dx)
        Player1.draw(screen)
        Player2.draw(screen)
        pygame.display.update()


def menu() :
    while True :
        clock.tick(FPS)
        screen.fill((0,0,0))
        render_text(screen,"PONG MULTIPLAYER","assets/fonts/kenpixel_future.ttf",(255,255,255),28,45,250)
        render_text(screen, "CLICK TO FIND A MATCH", "assets/fonts/kenpixel_future.ttf", (255, 255, 255), 20, 75, 300)
        for event in pygame.event.get() :
            if event.type == pygame.QUIT:

                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN :
                main()



        pygame.display.update()




menu()






