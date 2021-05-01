# 파이썬 게임 만들기
    # 파이게임 다운로드
    # File -> Settings -> Project:pythonProject -> pip더블클릭 -> pygame검색 -> 왼쪽 하단 버튼으로 install하기

import pygame # 파이게임 파일 불러오기

# Initialize the game engine
pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

size = [1000, 600]
screen = pygame.display.set_mode(size)

비행기이미지 = pygame.image.load("비행기이미지.jpeg")

pygame.display.set_caption("비행기 게임")

done = False
clock = pygame.time.Clock()

from pygame.locals import KEYDOWN, K_SPACE, K_LEFT, K_RIGHT

game_over = False   # 게임 종료 변수
ship_y = 250
walls = 80
ship_x = 960
is_right_down = True

while not done:
    is_space_down = False
    for event in pygame.event.get(): # 행동을 감지하고 어떤 행동을 했는지 알려주는 반복문
        if event.type == pygame.QUIT:
            done = True # 게임 끝내는 함수

        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                is_space_down = True

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                is_right_down = True

        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                is_right_down = False

    # 비행기 이동
    if not game_over:
        if is_space_down == True :
            ship_y += -9
        if is_space_down == False :
            ship_y += 3
        """
        if is_right_down == True :
            ship_x += -10
        if is_right_down == False :
            ship_x += 10
        """

    # 그리기
    screen.fill(WHITE) # 바탕화면을 흰색으로 바꾸기
    pygame.draw.rect(screen, BLACK, [0 , 75, 1000, 400])
    screen.blit(비행기이미지, (ship_x, ship_y))
    clock.tick(10)

    pygame.display.flip()
pygame.quit()