import pygame # 1. pygame 선언
pygame.init() # 2. pygame 초기화

# 3. pygame에 사용되는 전역변수 선언
WHITE = (255,255,255) 
BLACK = (0, 0, 0) #화면 색
YELLOW = (255, 255, 0) #X도형 색
RED = (255, 0, 0)#게임 종료 폰트 색

large_font = pygame.font.SysFont(None, 72) #종료 메시지 폰트와 크기
small_font = pygame.font.SysFont(None, 36) #OX 도형 표시 폰트와 크기
size = [600,600] #화면 크기
screen = pygame.display.set_mode(size) 
turn = 0 #게임 순서(턴) 을 확인할 변수-(0=X)(1=O)