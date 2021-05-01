"""
pygame의 기본 구조
    1. pygame 선언

    2. pygame 초기화

    3. pygame에서 사용할 전역 변수 선언
        예) - size(크기)
            - screen(화면 변수 만들기)
            - clock(FPS 설정)

    4. pygame 메인 루프(while문)
        4-1. pygame의 event 설정

        4-2. pygame의 화면 설정

        4-3. 사용자 행위

import pygame # pygame 파일 불러오기

참고(색깔)(RGB값) :

    red : (255, 0, 0)
    green : (0, 255, 0)
    blue : (0, 0, 255)
    black : (0, 0, 0)
    white : (255, 255, 255)
    yellow : (255, 255, 0)


초기 설정과 관련된 코드 :

    pygame.init() # 게임 초기화

    size  = [ x값 ,y값 ] # 화면 크기 변수 만들기
    screen= pygame.display.set_mode(size) # 게임 화면 크기 정하기

    pygame.display.set_caption("게임 제목") # 게임 제목 정하기

    clock = pygame.time.Clock() # 초당 몇번 출력하는지 설정(FPS 설정)

메인 루프와 관련된 코드 :

   While True : # 무한 반복 안에 넣기

    for eventin pygame.event.get(): # 이벤트가 발생하면 이를 감지하고 무슨 이벤트가 일어났는지 알려주는 반복문

     * 중요 *
     if event.type == pygame.QUIT: # 이 코드는 GUI 창에서 x 버튼을 누르면 발생하는 이벤트다
        break # 만약 PC에서 오류가 발생하여, 게임이 꺼져야 함에도 불구하고 꺼지지 않을 경우, while문이 돌아가지 않게 하여 강제로 꺼질 수 있도록 하는 일종의 안전장치

    screen.fill(색깔) # 화면을 변수 색깔로 채우기

    * 중요 *
     clock.tick(10) # FPS를 10으로 설정(초당 10번의 화면을 출력) # 이걸 안 넣으면 이상해 질수 있음(while문 안에 넣기)

    * 중요 *
    pygame.display.flip() # 화면에 작성한 모든 행위를 업데이트해주기 위한 함수(메인 루프 마지막에 꼭 넣기)


참고(pygame.draw와 관련된 코드) :

    사각형 - pygame.draw.rect
    삼각형 - pygame.draw.polygon
    원 - pygame.draw.circle
    타원 - pygame.draw.ellipse
    원(특정 부분까지 그리기) - pygame.draw.arc
    선 - pygame.draw.line
    여러 개의 선 - pygame.draw.lines
    부드러운 선 - pygame.draw.aaline
    여러 개의 부드러운 선 - pygame.draw.aalines

참고(pygame에 이미지를 넣는 코드) :

    pygame.image.load('이미지의 이름')
    a = pygame.Rect(이미지 이름.get_rect()) # a를 선택한 이미지로 바꾸기

참고(pygame에 소리 넣는 코드) :

    pygame.mixer.music.load('파일 이름') # 파이게임 배경소리 넣기
    pygame.mixer.music.play(-1) # -1 : 무한 반복, 0 : 한번 재생
"""
