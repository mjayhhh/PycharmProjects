#파이썬 게임 만들기
    # 파이게임 다운로드
    #file => setting => project => pip => pygame검색
import pygame #파이게임 파일 불러오기
from pygame.locals import QUIT , Rect , KEYDOWN , K_SPACE
SURFACE = pygame.display.set_mode( (800,600) ) #파이게임 화면크기
pygame.init() #파이게임 시작
pygame.key.set_repeat(5,5)
FPSCLOCK = pygame.time.Clock()
import sys
from random import randint

def main():
    ship_y = 250
    holes = [] # 리스트
    비행기이미지 = pygame.image.load("비행.png")    # 조작할 비행기 이미지
    game_over = False   # 게임종료 변수
    score = 0           # 점수 변수
    velocity =0         # 비행기 위치 변수
    walls = 80          # 벽 변수
    for xpos in range(walls) :          # 벽 그리기
        holes.append( Rect( xpos*10 , 100 , 10 , 400))
    slope = randint(1 , 6) #난수 만들기 변수

    while True :    # 무한반복하기
        is_space_down = False
        for event in pygame.event.get(): # 반복하기기
            if event.type == QUIT:
                pygame.quit() #파이게임 끝내기
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    is_space_down = True

        if not game_over:   # 비행기 이동
            score +=10
            velocity += -3 if is_space_down else 3
            ship_y += velocity

            # 충돌 : 벽에 닿으면 게임 끝
            if holes[0].top > ship_y or holes[0].bottom < ship_y + 80 :
                game_over = True

            # 동굴 모양 변경
            edge = holes[-1].copy()             # 복제하기
            test = edge.move( 0 , slope )       # 벽 랜덤으로 이동하기
            if test.top <=0 or test.bottom >= 600 :
                slope = randint( 1 , 6 ) * ( -1 if slope >0 else 1 )
                edge.inflate_ip( 0 , -20)
            edge.move_ip( 10 , slope )
            holes.append( edge )
            holes = [x.move(-10,0) for x in holes ]

        SURFACE.fill( (0,255,0) )      # 그리기
        for hole in holes:
            pygame.draw.rect( SURFACE, (0,0,0) , hole )
        SURFACE.blit(비행기이미지 , ( 0,ship_y) )
        pygame.display.update()
        FPSCLOCK.tick(15)

if __name__=='__main__':
    main()