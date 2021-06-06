import pygame           # pygame 불러오기
import random           # random 파일 불러오기
import threading        # time 파일 불러오기

# 색깔 정리( RGB 값 )
red = (255, 0, 0)       # 빨간색 RGB 값
green = (0, 255, 0)     # 초록색 RGB 값
blue = (0, 0, 255)      # 파란색 RGB 값
black = (0, 0, 0)       # 검정색 RGB 값
white = (255, 255, 255) # 하얀색 RGB 값
yellow = (255, 255, 0)  # 노란색 RGB 값


# 게임 기초 설정
pygame.init()                                       # 게임 초기화

size = [600, 900]                                   # 화면 크기 변수 만들기
screen = pygame.display.set_mode(size)              # 게임 화면 크기 정하기

pygame.display.set_caption("피하기 게임")             # 게임 제목 정하기

clock = pygame.time.Clock()                         # 초당 몇번 출력하는지 설정할 수 있는 변수 만들기(FPS 설정)

score = 0                                           # 점수를 0으로 설정하기
돌사진 = pygame.image.load('돌.png')                  # 돌 png의 이미지를 로드해서 돌사진에 넣기
캐릭터사진 = pygame.image.load('도라에몽 사진.jpg')     # 도라에몽 사진 jpg의 이미지를 로드해서 캐릭터 사진에 넣기
벽돌화면 = pygame.image.load('벽돌화면.png')           # 벽돌화면 png의 이미지를 로드해서 캐릭터 사진에 넣기


# 돌이 랜덤한 위치에 떨어지게 위치하는 코드
돌개수 = []                                  # 돌의 개체의 정보랑 속도를 저장하는 돌 개수 리스트
for i in range(10) :                        # 10번 반복하기( 10개의 돌 변수를 만들기 돌 개수 리스트에 저장하기 )
    돌 = pygame.Rect(돌사진.get_rect())      # 돌 이미지로 만든 돌 변수 만들기
    돌.left = random.randint(0, size[0])    # 돌의 x의 위치를 0부터 화면의 가로 크기 까지 랜덤하게 위치하기
    돌.top = -100                           # 돌의 y의 위치를 -100 ( 화면 밖 ) 에 위치하게 하기
    돌속도 = random.randint(3, 9)            # 돌의 속도를 3부터 9까지 랜덤하게 설정하기
    돌개수.append((돌, 돌속도))               # 돌의 정보들을 돌 개수 리스트에 저장하기


# 캐릭터가 정 중앙에 위치하게 하는 코드
캐릭터 = pygame.Rect(캐릭터사진.get_rect())        # 캐릭터 이미지로 만든 캐릭터 변수 만들기
캐릭터.left = size[0] // 2 - 캐릭터.width // 2    # 캐릭터의 x의 위치를 화면에 가운데 에다가 위치하게 하기
캐릭터.top = size[1] - 캐릭터.height              # 캐릭터를 화면 맨 아래에 위치하게 하기
캐릭터_x = 0                                     # 캐릭터가 이동하게 하는 변수


# 캐릭터가 움직이게 할수 있게 하는 코드 및 게임 종료하게 하는 코드
게임종료 = False                                   # 게임 종료 함수
while not 게임종료 :                               # 게임 종료를 했을 때 오류가 걸릴 걸 대비해서 만든 무한 반복문
    screen.blit(벽돌화면, (0,0))                   # 화면을 벽돌화면 이미지로 채우기
    for event in pygame.event.get():              # 화면 안에서 일어나는 이벤트( 행동 ) 을 감지해서 그 행동이 뭔지 알려주는 반복문
        if event.type == pygame.QUIT :            # 만약에 그 행동의 종류가 나가는 거라면
            게임종료 = True                        # 게임 종료를 True로 만들기 = 반복문을 종료하기
            pygame.quit()                         # pygame을 나가기
        elif event.type == pygame.KEYDOWN :       # 만약 위에 조건문이 아니고 행동의 종류가 키를 누르는 거라면
            if event.key == pygame.K_RIGHT:       # 그리고 만약에 그 키가 오른쪽 방향키라면
                캐릭터_x += 5                      # 캐릭터의 x값에 5를 더하기
            if event.key == pygame.K_LEFT:        # 그리고 만약에 그 키가 왼쪽 방향키라면
                캐릭터_x -= 5                      # 캐릭터의 x값에 -5를 더하기
        elif event.type == pygame.KEYUP :         # 만약 행동이 키를 누르고 있지 않는 거라면 = 계속 움직이는걸 막기 위해서
            if event.key == pygame.K_RIGHT:       # 만약에 그 키가 오른쪽 방향키라면
                캐릭터_x = 0                       # 움직이는 x의 값을 0으로 정하기
            if event.key == pygame.K_LEFT:        # 만약에 그 키가 왼쪽 방향키라면
                캐릭터_x = 0                       # 움직이는 x의 값을 0으로 정하기


# 캐릭터와 돌이 부딪혔을때 게임을 종료하게 하는 코드
    for (돌, 돌속도) in 돌개수:        # 돌 개수 안에 있는 정보를 차례로 돌과 돌속도에 대입하면서 반복
        if 돌.colliderect(캐릭터):    # 만약에 돌이 캐릭터와 부딪혔다면
            게임종료 = True           # 게임종료를 True로 만들기 = 반복문 종료하기



# 돌을 화면에 출력하기 및 돌이 떨어진뒤 다시 생성하게 하는 코드
    for (stone, speed) in 돌개수 :                   # 돌개수 안에 있는 정보를 stone과 speed에 차례로 담으면서 반복하기
        stone.top += speed                          # 돌의 y의 값에 speed를 더하기
        if stone.top > size[1] :                    # 만약에 돌의 y의 값이 화면의 크기보다 더 커진다면 = 돌이 화면 밖으로 나간다면
            돌개수.remove((stone, speed))            # 그 돌을 돌개수 리스트에서 없애기
            stone = pygame.Rect(돌사진.get_rect())   # 돌 이미지를 가진 새로운 stone 변수 만들기
            score += 1                              # 돌이 없어졌을 때 점수에 1점씩 더하기
            stone.left = random.randint(0, size[0]) # 새로운 돌의 가로 위치를 0부터 화면에 가로크기 까지 랜덤하게 하기
            stone.top = -100                        # 새로운 돌의 세로 위치를 -100 으로 맞추기
            speed = random.randint(3, 9)            # 새로운 돌의 속도를 3부터 9까지의 랜덤하게 하기
            돌개수.append((stone, speed))            # 새로운 돌의 정보를 리스트에 담기


# 캐릭터가 움직이게 하는 코드
    캐릭터.left = 캐릭터.left + 캐릭터_x         # 캐릭터의 x의 값에 움직이는 거리를 더하기
    if 캐릭터.left < 0 :                      # 만약에 캐릭터가 왼쪽 벽을 나갈려고 한다면
        캐릭터.left = 0                       # 캐릭터를 왼쪽 끝에 위치하게 하기
    if 캐릭터.left > size[0] - 캐릭터.width:   # 만약 캐릭터가 오른쪽 벽을 넘어갈려고 한다면
        캐릭터.left = size[0] - 캐릭터.width   # 캐릭터를 오른쪽 끝에 위치하게 하기

    # 게임 종료 메시지 띄우기
    if 게임종료:                                                         # 만약 게임 종료가 됬다면
        font = pygame.font.SysFont("malgungothic", 75)                  # 맑은 고딕체의 75크기의 폰트 변수 만들기
        message = font.render("Game Over", True, yellow)                # Game Over을 담은 message함수
        threading.Timer(2.0, screen.blit(message, (120, 375))).start()  # 2초 동안 메시지 띄우기

    # 점수 띄우기
    font1 = pygame.font.SysFont("malgungothic", 35)                     # 맑은 고딕체의 35크기의 폰트 변수 만들기
    message1 = font1.render(str(score) + "점", True, yellow)             # 점수를 담은 message함수
    threading.Timer(2.0, screen.blit(message1, (500, 850))).start()     # 2초 동안 메시지 띄우기

# 돌을 돌의 개수만큼 생성하게 하는 코드
    for(돌, 돌속도) in 돌개수:         # 돌개수 안에 있는 정보를 돌과 돌속도에 담아 차례로 반복하기
        screen.blit( 돌사진, 돌)      # 화면에 돌을 추가하기


# 캐릭터를 화면에 출력하게 하는 코드
    screen.blit(캐릭터사진, 캐릭터)    # 화면에 캐릭터 추가하기


# 화면 업데이트 및 FPS설정하는 코드
    pygame.display.update()         # 화면에 작성한 모든 행위를 업데이트해주기 위한 함수(메인 루프 마지막에 꼭 넣기)
    clock.tick(100)                 # FPS를 100으로 설정(초당 100번의 화면을 출력)