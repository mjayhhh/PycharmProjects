import pygame
from pygame.locals import *
import threading # time 파일 불러오기
import time

pygame.init() # 게임 초기화

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

game_over = False

size  = [ 620 , 400 ] # 화면 크기 변수 만들기
screen = pygame.display.set_mode(size) # 게임 화면 크기 정하기

pygame.display.set_caption("벽돌깨기") # 게임 제목 정하기

clock = pygame.time.Clock() # 초당 몇번 출력하는지 설정(FPS 설정)

# 이미지 불러오기
background = pygame.image.load('벽돌화면2.jpg') # 파이게임에 이미지 넣기

pygame.key.set_repeat(1, 1)

# 벽돌그리기 함수
def 벽돌그리기():
    for 벽돌 in 벽돌리스트 :
        pygame.draw.rect( screen, yellow, 벽돌, 1)
    # draw : 그리기 rect : 사각형
                        # 위치 , 색상, 크기(x축 크기, y축 크기, x축 위치, y축 위치)

# 원 그리기 함수
def 원():
    pygame.draw.circle(screen, yellow, (int(x),int(y)), 10) # 마지막 숫자 원의 크기

# 사각형 테두리 그리기 함수
def 사각형테두리() :
    pygame.draw.rect(screen,blue,(160, 60, 160, 50), 5) # 맨 마지막 숫자 = 테두리의 크기

# 공 변수
x = int(size[0]/2)
y = size[1]- 30
ax = 3 # 오른쪽
ay = -3 # 아래로

# 패달 변수
패달세로 = 10
패달가로 = 75
패달x = (size[0] - 패달가로 ) / 2
패달 = pygame.Rect(패달x, 400 - 패달세로 - 10, 패달가로, 패달세로)

def 패달그리기():
    pygame.draw.rect(screen,(0,211,149), 패달)

# 벽돌 변수
점수 = 0
벽돌리스트 = []
for 열 in range(7):
    for 행 in range(6) :
        벽돌 = pygame.Rect(열 * (60 + 20) + 35, 행 * (16 + 5) + 24, 68, 16)
        벽돌리스트.append(벽돌)

# 실행 코드
while not game_over :
    x += ax
    y += ay

    # 공과 벽돌 충돌 검사
    if x + ax > 620 or x + ax < 0 : # 화면에 공의 x축이 최대 가로 480 - 7 보다 커지면
        ax = -ax # 반대로 가게 하기
    if y + ay < 0 or y + ay > 400 : # 화면에 공의 y축이 최대 가로 320 - 7 보다 커지면
        ay = -ay # 반대로 가게 하기
    elif y + ay > 390 : # 실패시 종료
        if x > 패달x and x < 패달x + 패달가로: # 패달에 공이 닿으면
            ay = -ay # 공을 반대로 가기
        else :
            game_over = True

    # 플랫폼이 벽 밖으로 나가지 않게
    if 패달x + 패달가로 > 620 :
        패달.x = 610 - 패달가로
        패달x = 610 - 패달가로
    if 패달x < 0 :
        패달.x = 10
        패달x = 10

    # 벽돌 충돌
    for 벽돌 in 벽돌리스트 :
        if x > 벽돌.x and x < 벽돌.x + 벽돌.width and y > 벽돌.y and y < 벽돌.y + 벽돌.height :
            ay = -ay
            벽돌리스트.remove(벽돌)
            점수 += 1

    # 동작
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit() # 파이게임 끝내기
            game_over = True # 반복문 멈추기(오류가 걸렸을 때의 비상용 코드)
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT:
                패달.left -= 1
                패달x -= 1
            if event.key == pygame.K_RIGHT:
                패달.right += 1
                패달x += 1

    # screen.fill(black) # 화면을 검정색으로 채우기
    screen.blit(background, (0, 0))

    # 점수 출력
    font = pygame.font.SysFont("malgungothic", 30)  # 글꼴 설정
    score_message = font.render(str(점수), True, (0,0,0))  # score를 화면에 띄우기
    screen.blit(score_message, (590, 360))  # 메시지를 10,10에 띄우기

    벽돌그리기() # 함수 호출
    원() # 함수 호출
    # 사각형테두리() # 함수 호출
    패달그리기() # 함수 호출

    clock.tick(100)

    if game_over == True:
        font = pygame.font.SysFont("malgungothic", 72)  # 글꼴 설정
        message = font.render("Game over", True, (0, 0, 0))  # score를 화면에 띄우기
        threading.Timer(2.0, screen.blit(message, (135, 150))).start()  # 2초 동안 메시지 띄우기

    if 점수 == 42:
        font = pygame.font.SysFont("malgungothic", 72)  # 글꼴 설정
        message = font.render("Clear", True, (0, 0, 0))  # score를 화면에 띄우기
        threading.Timer(2.0, screen.blit(message, (135, 150))).start()  # 2초 동안 메시지 띄우기
        game_over == True

    pygame.display.update() # 함수 업데이트