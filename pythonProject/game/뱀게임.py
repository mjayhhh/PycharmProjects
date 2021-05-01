import pygame # pygame 파일 불러오기
from pygame.locals import QUIT, Rect, KEYDOWN, K_UP, K_LEFT,K_RIGHT, K_DOWN
#                         종료   직각  키 종료   위방향키 왼쪽   오른쪽    아래
import random # random 파일 불러오기
import sys # sys 파일 불러오기

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)

pygame.init() # pygame 초기화
size = [600,600] # 화면 크기
screen = pygame.display.set_mode(size) # 화면 크기 정하기
fps = pygame.time.Clock() # fps 설정(화면재기)
(X,Y) = (20,20) # 가로길이 세로길이

음식 = [] # 음식 리스트 선언  # 리스트 : 여러개의 변수를 저장할 수 있는 저장소
뱀 = [] # 뱀 리스트 선언

def 음식생성() : # 임의의 장소에 음식을 배치 하는 함수[코드 묶음]을 선언
    while True: # 무한 반복
        위치 = [random.randint(0,X-1),random.randint(0, Y-1)]
        if 위치 in 음식 or 위치 in 뱀 : # 위치안에 음식이 있거나 뱀이 있으면
            continue # while문 다시 실행
        음식.append(위치) # 음식 리스트에 위치 추가
        break # while문 끝내기

def 음식이동(위치): # 음식을 다른 위치로 이동하게 하는 함수
    i = 음식.index(위치) # 음식리스트에서 위치에 해당하는 음식 찾기
    del 음식[i] # 찾은 음식 삭제
    음식생성() # 새로운 음식 생성

def 그리기(메시지): # 화면 그리기 { 좌표, 뱀, 음식, 게임종료 }
    screen.fill(black)
    for food in 음식 :
        pygame.draw.ellipse(screen,green, Rect(food[0]*30, food[1]*30, 30, 30))
            # 타월그리기(화면이름, 색깔(green),타원(x축,y축,가로,세로))

    for body in 뱀 :
        pygame.draw.rect(screen, (0,255,255), Rect(body[0]*30, body[1]*30, 30, 30))
                    # 사각형그리기(화면이름, 색깔, 타원( x축, y출, 가로, 세로))

    for index in range(20):
        pygame.draw.line(screen, (64,64,64), (index*30, 0), (index*30, 600)) # x축 그리기
        pygame.draw.line(screen, (64,64,64), (0,index*30), (600, index*30)) # y축 그리기

    if 메시지 != None: # 메시지 내용이 존재하면
        screen.blit(메시지,(150,300)) # 화면에 출력하기
    pygame.display.update() # 화면 업데이트

myfont = pygame.font.SysFont( None,80)
key = K_DOWN
메시지 = None # 종료시 나타나는 메시지
게임종료 = False # 게임 종료 스위치
뱀.append((int(X/2), int(Y/2))) # 첫 실행시 뱀을 화면 가운데 위치
for _ in range(10):
    음식생성()
while True:
    for event in pygame.event.get(): # 파이게임 이벤트 감지 반복문
        if event.type == QUIT: # 끝내기 이벤트면
            pygame.quit() # 게임종료
            sys.exit()  # 프로그램 종료
        elif event.type == KEYDOWN: # 키를 눌렀을때
            key = event.key # 누른 키를 키에 대입

    if not 게임종료: # 만약 게임 종료가 아니면 : False이면
        if key == K_LEFT:
            머리 = (뱀[0][0] - 1, 뱀[0][1]) # 머리부분의 x축 이동
        elif key == K_RIGHT:
            머리 = ( 뱀[0][0] + 1, 뱀[0][1]) # 머리부분의 x축 이동
        elif key == K_UP:
            머리 = (뱀[0][0], 뱀[0][1] - 1)  # 머리부분의 y축 이동
        elif key == K_DOWN:
            머리 = (뱀[0][0], 뱀[0][1] + 1)  # 머리부분의 y축 이동

        if 머리 in 뱀 or 머리[0] < 0 or 머리[0] >= X or 머리[1] < 0 or 머리[1] >= Y :
            메시지 = myfont.render("Game Over",True,(255,255,0))
            게임종료 = True

        뱀.insert(0,머리)
        if 머리 in 음식 :
            음식이동(머리)
        else :
            뱀.pop()
    그리기(메시지)
    fps.tick(5)  # fps를 5으로 설정하기

