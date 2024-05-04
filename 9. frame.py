import pygame
############################################################
# 0. 초기화 설정 값 #
pygame.init() # 초기화 반드시 필요함

# 화면 크기 설정
screen_width = 480 # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("HY GAME") # 게임이름

# FPS
clock = pygame.time.Clock()

############################################################
# 1. 사용자 게임 초기화 (배경화면, 게임이미지, 좌표, 속도, 폰트 등)

# 이벤트 루프
running = True 
while running:
    dt = clock.tick(30) 
    
    # 2. 이벤트 처리
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            running = False 
    
    # 3. 게임 캐릭터 위치 정의
    
    # 4. 충돌 처리
    
    # 5. 화면에 그리기
        
    pygame.display.update() # 반드시 계속해서 화면 그리기 필요

# pygame 종료 처리
pygame.quit()
