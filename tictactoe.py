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

grid = [' ', ' ', ' ', 
        ' ', ' ', ' ', 
        ' ', ' ', ' '] #3곱하기3내부 게임판 

done = False #
clock = pygame.time.Clock()

def is_valid_position(grid, position):
    if grid[position] == ' ':
        return True
    else:
        return False

#이겼는지 확인하는 함수 이겼으면 true, 아직 아니면 Fulse 리턴함
def is_winner(grid, mark): 
    if (grid[0] == mark and grid[1] == mark and grid[2] == mark) or \
        (grid[3] == mark and grid[4] == mark and grid[5] == mark) or \
        (grid[6] == mark and grid[7] == mark and grid[8] == mark) or \
        (grid[0] == mark and grid[3] == mark and grid[6] == mark) or \
        (grid[1] == mark and grid[4] == mark and grid[7] == mark) or \
        (grid[2] == mark and grid[5] == mark and grid[8] == mark) or \
        (grid[0] == mark and grid[4] == mark and grid[8] == mark) or \
        (grid[2] == mark and grid[4] == mark and grid[6] == mark):
        return True
    else:
        return False
#모든 칸이 다 찼는지 확인합니다
def is_grid_full(grid):
    full = True
    for mark in grid:
        if mark == ' ':
            full = False 
            break
    return full
turn = 0 

def runGame():
    #게임 활용 변수
    CELL_SIZE = 60#셀 사이즈
    COLUMN_COUNT = 3#세로수 #이거 고치면 OX 그리는 함수에서 오류남 시발 이럴거면 왜 만들어놓은거임?
    ROW_COUNT = 3#가로수
    #게임 종료시 가능성
    X_WIN = 1
    O_WIN = 2
    DRAW = 3
    game_over = 0

    Sp_CELL_SIZE = 180#셀 사이즈
    Sp_COLUMN_COUNT = 3#세로수 #이거 고치면 OX 그리는 함수에서 오류남 시발 이럴거면 왜 만들어놓은거임?
    Sp_ROW_COUNT = 3#가로수
    #게임 종료시 가능성
    Sp_X_WIN = 1
    Sp_O_WIN = 2
    Sp_S0DRAW = 3
    Sp_game_over = 0

#글로벌 변수 done-긑났는가? turn몇번째 턴인가? grid-뭐지
    global done, turn, grid
    while not done: #끝나지 않았을때까지 반복
        clock.tick(30)
        screen.fill(BLACK)
        
        #화면 그리는 함수
<<<<<<< HEAD

        for column_index in range(COLUMN_COUNT):
                for row_index in range(ROW_COUNT):
=======
        for column_index in range(COLUMN_COUNT*3):
                for row_index in range(ROW_COUNT*3):
>>>>>>> 80507236c760effe3ee0a72e05a892e24ecba7af
                    rect = (CELL_SIZE * column_index, CELL_SIZE * row_index, CELL_SIZE, CELL_SIZE)
                    if column_index<=2 and row_index<=2:
                        pygame.draw.rect(screen, YELLOW, rect, 1)
                    else:
                        pygame.draw.rect(screen, WHITE, rect, 1)
        
        for event in pygame.event.get():#이 for문 안에서 if문을 읽음
            if event.type == pygame.QUIT: #이벤트-종료시 done을 ture로
                done=True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if turn == 0:
                    column_index = event.pos[0] // CELL_SIZE
                    row_index = event.pos[1] // CELL_SIZE
                    position = column_index + 3 * row_index
                    if is_valid_position(grid, position):
                        grid[position] = 'X'
                        if is_winner(grid, 'X'):
                            print('X 가 이겼습니다.')
                            game_over = X_WIN 
                            #break
                        elif is_grid_full(grid):
                            print('무승부 입니다.')
                            game_over = DRAW 
                            #break
                        turn += 1
                        turn = turn % 2
                else:       
                    column_index = event.pos[0] // CELL_SIZE
                    row_index = event.pos[1] // CELL_SIZE
                    position = column_index + 3 * row_index
                    if is_valid_position(grid, position):
                        grid[position] = 'O'   
                        if is_winner(grid, 'O'):
                            print('O 가 이겼습니다.')
                            game_over = O_WIN 
                            #break
                        elif is_grid_full(grid):
                            print('무승부 입니다.')
                            game_over = DRAW 
                            #break
                        turn += 1
                        turn = turn % 2
            #도형 찍는 함수 입력한번 들어올 때마다 모든 칸 확인하고 모두 채워넣음 ...( 는 또 왜 여따넣음???)
            for column_index in range(COLUMN_COUNT):
                for row_index in range(ROW_COUNT):
                    position = column_index + 3 * row_index
                    mark = grid[position]
                    if mark == 'X':
                        X_image = small_font.render('{}'.format('X'), True, YELLOW)
                        screen.blit(X_image, (CELL_SIZE * column_index + 10, CELL_SIZE * row_index + 10)) 
                    elif mark == 'O':
                        O_image = small_font.render('{}'.format('O'), True, WHITE)
                        screen.blit(O_image, (CELL_SIZE * column_index + 10, CELL_SIZE * row_index + 10)) 
            #결과 출력 안끝났으면 다시 이벤트 받기
            if not game_over: 
                pass
            else:
                if game_over == X_WIN:
                    game_over_image = large_font.render('X wins', True, RED)
                elif game_over == O_WIN:
                    game_over_image = large_font.render('O wins', True, RED)
                else:
                    game_over_image = large_font.render('Draw', True, RED)
                screen.blit(game_over_image, (600 // 2 - game_over_image.get_width() // 2, 600 // 2 - game_over_image.get_height() // 2))
            pygame.display.update() #모든 화면 그리기 업데이트
            
runGame()
pygame.quit()
