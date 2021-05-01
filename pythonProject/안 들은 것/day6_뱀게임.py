import pygame # 파이게임 파일 불러오기 [ 임포트 ]
from pygame.locals import QUIT , Rect , KEYDOWN , K_UP , K_LEFT , K_RIGHT , K_DOWN
                        # 종료 , 직각 , 키 눌렀을때 , 위방향키 , 왼쪽방향키 , 오른쪽방향키 , 아래방향키
import random # 랜덤 파일 불러오기 [ 임포트 ]
import sys # 시스템 파일 불러오기 [ 일포트 ]
pygame.init() # 파이게임 초기값
SURFACE = pygame.display.set_mode( (600,600) ) # 화면 구성
FPSCLOCK = pygame.time.Clock() #시간 체크

#####################################################################################
음식 = [] # 음식 리스트 선언   #리스트 : 여러개의 변수 저장
뱀 = [ ] # 뱀 리스트 선언 # 리스트
(W,H) = (20,20) # 가로길이 세로길이

####################################################################################
def 음식생성() : # 임의의 장소에 음식을 배치 하는 함수[코드묶음]를 선언
    while True : # 무한반복
        위치 = ( random.randint( 0 , W-1 ) , random.randint( 0 , H-1) )
        if 위치 in 음식 or 위치 in 뱀 :
            continue # while 다시 실행
        음식.append(위치) #음식리스트에 위치 추가
        break # while 끝내기
################################################################################################
def 음식이동(위치) : #음식을 다른 위치로 이동
    i = 음식.index(위치)  # 음식리스트에서 위치에 해당하는 음식찾기
    del 음식[i]           # 찾은 음식 삭제
    음식생성()          # 새로운 음식 생성
###################################################################################################
def 그리기(메시지) : # 화면 그리기 함수 [ 좌표 , 뱀 , 음식 , 게임종료 ]
    SURFACE.fill( (0,0,0) )
    for food in 음식 : # 음식리스트에 있는 음식 갯수만큼 반복
        pygame.draw.ellipse( SURFACE , (0 ,255,0) , Rect( food[0]*30 , food[1]*30 , 30 , 30 ) )
                    # 타원그리기( 화면이름 , 칼라[RGB] , 타원( x축 , y축 , 가로크기 , 세로크기)
    for body in 뱀 :
        pygame.draw.rect( SURFACE , (0,255,255) , Rect( body[0]*30 , body[1]*30 , 30 , 30 ) )
                    # 사각형그리기( 화면이름 , 칼라[RGB] , 사각형( X축 , Y축 , 가로크기 , 세로크기 )
    for index in range(20) :
        pygame.draw.line( SURFACE , (64,64,64) , ( index*30 , 0 ) ,(index*30 , 600) ) # x축 그리기
        pygame.draw.line( SURFACE , (64,64,64) , (0 , index*30) , ( 600 , index*30) ) # y축 그리기

    if 메시지 !=None : # 메시지 내용이 존재하면
        SURFACE.blit(메시지,(150,300)) # 화면에 메시지 출력하기
    pygame.display.update() # 화면 업데이트

#########################################################################################################

myfont = pygame.font.SysFont( None , 80)
key = K_DOWN
메시지 = None  #게임종료시 나타나는 메시지
게임종료 = False  #게임종료 스위치
뱀.append( ( int(W/2) , int(H/2) ) ) # 실행시 뱀을 화면 가운데 위치
for _ in range(10) : # 10번 반복하기
    음식생성() # 음식생성 함수 불러오기

while True: # 무한 반복
    for 동작 in pygame.event.get(): # 파이게임 이벤트[동작] 있을경우
        if 동작.type == QUIT : # 끝내기 이벤트 이면
            pygame.quit() # 게임 종료
            sys.exit()  # 프로그램 종료
        elif 동작.type == KEYDOWN: # 키 눌렀을때
            key = 동작.key # 눌른키를 키에 대입
    ##################################################
    if not 게임종료 : # 만약에 게임종료가 아니면 [ False 이면 ]
        if key == K_LEFT:
            머리 = ( 뱀[0][0] - 1 , 뱀[0][1] ) # 머리부분을 X축[왼쪽]으로 이동
        elif key == K_RIGHT :
            머리 = ( 뱀[0][0] +1 , 뱀[0][1] ) # 머리부분을 X축[오른쪽]으로 이동
        elif key == K_UP :
            머리 =( 뱀[0][0] , 뱀[0][1] -1 )   # 머리부분을 Y축[위]으로 이동
        elif key == K_DOWN :
            머리 = ( 뱀[0][0] , 뱀[0][1] +1 )   # 머리부분을 Y축[아래]으로 이동

        if 머리 in 뱀 or 머리[0] < 0 or 머리[0] >= W or 머리[1] < 0 or 머리[1] >=H :
            메시지 = myfont.render("over game",True,(255,255,0) )
            게임종료 = True
        뱀.insert( 0 , 머리 )
        if 머리 in 음식 :
            음식이동(머리)
        else :
            뱀.pop()
    그리기( 메시지 )
    FPSCLOCK.tick(5)

