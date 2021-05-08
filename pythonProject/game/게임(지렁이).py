# 모든 줄에 주석 넣기

# 게임에 필요한 라이브러리를 import
import pygame # 파이게임 불러오기
from pygame import QUIT, Rect, KEYDOWN, K_UP,K_DOWN,K_LEFT,K_RIGHT
                #  종료  그리기 키눌렀을떄 위쪽키 아래키  왼쪽키  오른쪽키
import random # 랜덤 파일 불러오기
import sys # sys 파일 불러오기

# 색깔
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
white = (255, 255, 255)
yellow = (255, 255, 0)

# 기초 설정
pygame.init() # 파이게임 초기화
size = [ 1000 , 800 ] # 화면 크기 변수 만들기
SURFACE = pygame.display.set_mode( (900,750) ) # 화면 구성
FPSCLOCK = pygame.time.Clock() #시간 체크
# Frame Per Second : FPS : 초당 프레임[정지사진] 수
speed = 1 # 기본 스피드 = 1

# 이미지 불러오기
background = pygame.image.load('지렁이 배경화면.jpg') # 파이게임에 이미지 넣기

# 저장할 변수 생성
음식 = [] # 음식 리스트 선언   #리스트 : 여러개의 변수 저장
뱀 = [ ] # 뱀 리스트 선언 # 리스트
점수 = 0  # 점수 변수 선언
(W,H) = (30,25) # 가로길이 세로길이

# 함수 만들기
    # 1. 음식 함수 2. 음식이동 3. 그리기함수

# 음식 생성
def 음식생성() : # 임의의 장소에 음식을 배치 하는 함수[코드묶음]를 선언
    while True : # 무한반복
        위치 = ( random.randint( 0 , W-1 ) , random.randint( 0 , H-1) ) # 랜덤한 위치에 음식 설치
        if 위치 in 음식 or 위치 in 뱀 : # 만약 그 자리에 음식이나 뱀이 있다면
            continue # while 다시 실행
        음식.append(위치) #음식리스트에 위치 추가
        break # while 끝내기

# 점수가 10점 오를때마다 속도 빨라지게 하기
if 점수 % 10 == 0: # 점수가 10점으로 나눠지면
    speed + 1 # 속도 2배로 증가시키기
    점수 += 1 # 점수에 1점 더하기

# 음식 이동
def 음식이동(위치) : #음식을 다른 위치로 이동
    i = 음식.index(위치)  # 음식리스트에서 위치에 해당하는 음식찾기
    del 음식[i]           # 찾은 음식 삭제
    음식생성()          # 새로운 음식 생성

# 그리기
def 그리기(메시지) : # 화면 그리기 함수 [ 좌표 , 뱀 , 음식 , 게임종료 ]
    SURFACE.blit(background, (0, 0)) # 화면에 그림 넣기
    SURFACE.blit(background, (0, 500)) # 화면에 그림 넣기
    # SURFACE.fill( (0,0,0) )
    for food in 음식 : # 음식리스트에 있는 음식 갯수만큼 반복
        pygame.draw.ellipse( SURFACE , (0 ,255,0) , Rect( food[0]*30 , food[1]*30 , 30 , 30 ) )
                    # 타원그리기( 화면이름 , 칼라[RGB] , 타원( x축 , y축 , 가로크기 , 세로크기)
    for body in 뱀 :
        pygame.draw.rect( SURFACE , (0,255,255) , Rect( body[0]*30 , body[1]*30 , 30 , 30 ) )
                    # 사각형그리기( 화면이름 , 칼라[RGB] , 사각형( X축 , Y축 , 가로크기 , 세로크기 )
    for index in range(30) :
        pygame.draw.line( SURFACE , (64,64,64) , ( index*30 , 0 ) ,(index*30 , 750) ) # x축 그리기
        pygame.draw.line( SURFACE , (64,64,64) , (0 , index*30) , ( 900 , index*30) ) # y축 그리기

    if 메시지 != None : # 메시지 내용이 존재하면
        SURFACE.blit(메시지,(300,300)) # 화면에 메시지 출력하기
    pygame.display.update() # 화면 업데이트
myfont = pygame.font.SysFont( None , 80)
key = K_DOWN
메시지 = None  #게임종료시 나타나는 메시지
게임종료 = False  #게임종료 스위치
뱀.append( ( int(W/2) , int(H/2) ) ) # 실행시 뱀을 화면 가운데 위치
for _ in range(15) : # 10번 반복하기
    음식생성() # 음식생성 함수 불러오기

while True: # 무한 반복
    for 동작 in pygame.event.get(): # 파이게임 이벤트[동작] 있을경우
        if 동작.type == QUIT : # 끝내기 이벤트 이면
            pygame.quit() # 게임 종료
            sys.exit()  # 프로그램 종료
        elif 동작.type == KEYDOWN: # 키 눌렀을때
            key = 동작.key # 눌른키를 키에 대입
    if not 게임종료 : # 만약에 게임종료가 아니면 [ False 이면 ]
        if key == K_LEFT:
            머리 = ( 뱀[0][0] - speed , 뱀[0][1] ) # 머리부분을 X축[왼쪽]으로 이동
        elif key == K_RIGHT :
            머리 = ( 뱀[0][0] + speed , 뱀[0][1] ) # 머리부분을 X축[오른쪽]으로 이동
        elif key == K_UP :
            머리 =( 뱀[0][0] , 뱀[0][1] - speed )   # 머리부분을 Y축[위]으로 이동
        elif key == K_DOWN :
            머리 = ( 뱀[0][0] , 뱀[0][1] + speed )   # 머리부분을 Y축[아래]으로 이동

        if 머리 in 뱀 or 머리[0] < 0 or 머리[0] >= W or 머리[1] < 0 or 머리[1] >= H : # 만약 머리에 뱀이 닿는다면
            메시지 = myfont.render("Game Over",True,(255,255,0) ) # 맑은고딕 폰트로 출력하기
            게임종료 = True # 게임 종료하기
        뱀.insert( 0 , 머리 ) # 화면에 뱀 출력하기
        if 머리 in 음식 :
            음식이동(머리) # 음식 이동하기
            점수 += 1 # 점수에 1을 더하기
        else :
            뱀.pop() # 뱀리스트에서 없애기
        font = pygame.font.SysFont("malgungothic", 30)  # 글꼴 설정
        score_message = font.render(str(점수), True, (0, 0, 0))  # score를 화면에 띄우기
        SURFACE.blit(score_message, (590, 360))  # 메시지를 10,10에 띄우기
    그리기( 메시지 ) # 메시지( Game Over ) 출력
    FPSCLOCK.tick(5) # FPS 5로 설정
