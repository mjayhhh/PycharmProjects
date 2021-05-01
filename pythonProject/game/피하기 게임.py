import pygame # pygame 파일 불러오기
import random # random 파일 불러오기
import threading # time 파일 불러오기

# 색 설정
red = (255, 0, 0)       # 빨간색 RGB값
green = (0, 255, 0)     # 초록색 RGB값
blue = (0, 0, 255)      # 파란색 RGB값
black = (0, 0, 0)       # 검정색 RGB값
white = (255, 255, 255) # 하얀색 RGB값
yellow = (255, 255, 0)  # 노란색 RGB값

# 기본 설정
pygame.init() # 게임 초기화

size = [600, 800] # 화면 크기 변수 만들기
screen= pygame.display.set_mode(size) # 게임 화면 크기 정하기

clock = pygame.time.Clock() # 초당 몇번 출력하는지 설정(FPS 설정)

pygame.display.set_caption("피하기 게임") # 게임 화면의 제목을 똥 피하기 게임으로 정하기

score = 0 # 시작할때의 점수 변수
game_over = False # 게임을 시작하게 해주는 변수

# 소리 가져오기
pygame.mixer.music.load('배경음악.mp3') # 파이게임 배경소리 넣기
pygame.mixer.music.play(-1) # -1 : 무한 반복, 0 : 한번 재생

# 이미지 불러오기
character = pygame.image.load('스폰지밥.png') # 파이게임에 이미지 넣기
stone = pygame.image.load('돌.png')          # 파이게임에 이미지 넣기
background_brick = pygame.image.load('벽돌화면.png')

# 피해야하는 개체 여러개 만들기 -> 랜덤 위치에 생성하기
stone_number = [] # 돌의 개수와 속도를 저장하는 리스트
for i in range(10): # 미사일 개수(반복 개수)
    stone_clone = pygame.Rect(stone.get_rect()) # ()안에 이미지로 돌 그리기
    stone_clone.left = random.randint(0, size[1] ) # 0부터 화면 가로크기 까지의 객체 생성
    stone_clone.top = -100 # 화면 밖에 -100 부터 생성
    speed = random.randint(3,9) # 돌이 내려오는 속도
    stone_number.append((stone_clone, speed)) # stone2에 돌과 그 돌의 속도를 리스트에 저장

# 캐릭터 만들기
character_clone = pygame.Rect( character.get_rect() ) # 내가 가져온 이미지로 캐릭터 그리기
character_clone.left = size[0] // 2 - character_clone.width // 2 # 화면 최대 가로 크기에서 나누기 2를 한후 캐릭터의 가로의 길이에 나누기 2를 한 값을 뺀 위치를 저장하기
character_clone.top = size[1] - character_clone.height # 화면 최대 세로 크기에서 캐릭터의 세로의 길이를 뺀 위치를 저장하기
character_clone_x = 0 # 캐릭터의 x축 위치
character_clone_y = 0 # 캐릭터의 y축 위치

# 게임 메인 코드
while not game_over: # game_over이 True가 될 때 까지 무한 반복
    # screen.fill(white) # 바탕화면을 검정색으로 설정하기
    screen.blit(background_brick, (0,0))

# 캐릭터 조작
    event = pygame.event.poll() # 이벤트 가져오기
    if event.type == pygame.QUIT : # 만약 그 이벤트의 종류가 종료이면
        game_over = True # 반복 멈추기
        pygame.quit()
    elif event.type == pygame.KEYDOWN : # 만약 키를 눌렀으면
        if event.key == pygame.K_LEFT : # 만약 왼쪽 키를 눌렀을 때
            character_clone_x = -5 # x축을 -5만큼 이동(왼쪽으로 이동)
        if event.key == pygame.K_RIGHT : # 만약 오른쪽 키를 눌렀을 때
            character_clone_x = 5 # x축을 5만큼 이동(오른쪽으로 이동)
    elif event.type == pygame.KEYUP : # 키를 안 눌렀으면
        if event.key == pygame.K_LEFT :  # 만약 왼쪽 키를 눌렀을 때
            character_clone_x = 0  # x축을 -5만큼 이동(왼쪽으로 이동)
        if event.key == pygame.K_RIGHT :  # 만약 오른쪽 키를 눌렀을 때
            character_clone_x = 0  # x축을 5만큼 이동(오른쪽으로 이동)

# 돌 떨어지게 하기
    for (stone_clone, speed) in stone_number:  # stone_number 리스트에 있는 물체의 개수 만큼 반복
        stone_clone.top += speed # 물체에 속도를 계속 더하기
        if stone_clone.top > size[1]: # 만약에 돌이 화면 밖으로 나가면(바닥에 닿으면)
            score += 1 # 점수에 1점 더하기
            stone_number.remove((stone_clone,speed)) # 물체 삭제
            stone_clone = pygame.Rect(stone.get_rect()) # 새로운 물체 만들기
            stone_clone.left = random.randint(0, size[0]) # 새로운 물체의 가로 위치
            stone_clone.top = -100 # 새로운 물체의 세로 위치
            speed = random.randint(3,9) # 새로운 물체의 속도
            stone_number.append((stone_clone, speed)) # 새로운 물체를 리스트에 담기

# 캐릭터 이동하기
    character_clone.left = character_clone.left + character_clone_x
    if character_clone.left < 0 : # 캐릭터가 왼쪽 벽보다 더 가면
        character_clone.left = 0 # 벽을 못 넘게 막기
    if character_clone.left > size[0] - character_clone.width: # 캐릭터가 오른쪽 벽보다 더 나아가면
        character_clone.left = size[0] - character_clone.width # 벽을 못 넘게 막기

# 돌과 캐릭터가 닿았을때 종료하기
    for (stone_clone, speed) in stone_number:
        if stone_clone.colliderect( character_clone ) : # 만약 돌이 캐릭터와 닿았다면
            game_over = True # 반복 멈추기

# 화면(캐릭터 그리기) 그리기
    for(stone_clone, speed) in stone_number : # stone_number 리스트에 있는 물체의 개수 만큼 반복하기
        screen.blit( stone, stone_clone ) # 화면에 물체 그리기

    screen.blit( character, character_clone ) # 화면에 캐릭터 그리기

# 게임 종료 메시지 띄우기
    if game_over :
        font1 = pygame.font.SysFont("malgungothic", 72 ) # 글꼴 설정
        message = font1.render("Game Over", True, yellow) # Game Over을 담은 message함수
        threading.Timer(2.0, screen.blit( message, (125,275))).start() # 2초 동안 메시지 띄우기

# 점수 띄우기
    font2 = pygame.font.SysFont("malgungothic", 30) # 글꼴 설정
    score_message = font2.render( str(score) , True, yellow) # score를 화면에 띄우기
    screen.blit(score_message, (10,10)) # 메시지를 10,10에 띄우기

    pygame.display.update()  # 화면에 작성한 모든 행위를 업데이트해주기 위한 함수(메인 루프 마지막에 꼭 넣기)

    clock.tick(100)  # FPS를 10으로 설정(초당 10번의 화면을 출력)