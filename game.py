import pygame
pygame.init()

CELL_SIZE = 60
Sp_CELL_SIZE=180
COLUMN_COUNT = 9
ROW_COUNT = 9
Sp_COLUMN_COUNT = 3
Sp_ROW_COUNT = 3

WHITE = (255,255,255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

large_font = pygame.font.SysFont(None, 72)
small_font = pygame.font.SysFont(None, 36)
size = [600,600]
screen = pygame.display.set_mode(size)
turn = 1

P_X = 9
P_Y = 9
Sp_grid = [[0 for j in range(P_X)] for i in range(P_Y)]

done = False
clock = pygame.time.Clock()
#0-null x o / 3-xwin 4-owin Sp_mark
#작은 판 이기면 그 칸을 3으로 바꾼다
def is_valid_position(grid, position):
    if grid[position] == 0:
        return True
    else:
        return False

def is_winner(grid, mark):
    if  (grid[0] == mark and grid[1] == mark and grid[2] == mark) or \
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

def is_grid_full(grid):
    full = True
    for mark in grid:
        if mark == 0:
            full = False 
            break
    return full

def is_Sp_win(grid,Sp_mark): 
    if  (grid[0][0] == Sp_mark and grid[1][0] == Sp_mark and grid[2][0] == Sp_mark) or \
        (grid[3][0] == Sp_mark and grid[4][0] == Sp_mark and grid[5][0] == Sp_mark) or \
        (grid[6][0] == Sp_mark and grid[7][0] == Sp_mark and grid[8][0] == Sp_mark) or \
        (grid[0][0] == Sp_mark and grid[3][0] == Sp_mark and grid[6][0] == Sp_mark) or \
        (grid[1][0] == Sp_mark and grid[4][0] == Sp_mark and grid[7][0] == Sp_mark) or \
        (grid[2][0] == Sp_mark and grid[5][0] == Sp_mark and grid[8][0] == Sp_mark) or \
        (grid[0][0] == Sp_mark and grid[4][0] == Sp_mark and grid[8][0] == Sp_mark) or \
        (grid[2][0] == Sp_mark and grid[4][0] == Sp_mark and grid[6][0] == Sp_mark):
        return True
    else:
        return False

def Sp_postoindex(pos):
    column_index = pos[0] // Sp_CELL_SIZE
    row_index = pos[1] // Sp_CELL_SIZE
    index = column_index + 3 * row_index
    return index

def postoindex(pos):
    minposx = pos[0] % Sp_CELL_SIZE
    minposy = pos[1] % Sp_CELL_SIZE
    column_index = minposx// CELL_SIZE
    row_index =  minposy// CELL_SIZE
    index = column_index + 3 * row_index
    return index

def runGame():
    X_WIN = 1
    O_WIN = 2
    DRAW = 3
    game_over = 0
    global done, turn, Sp_grid
    while not done:
        clock.tick(30)
        screen.fill(BLACK)
        for event in pygame.event.get():
            for column_index in range(COLUMN_COUNT):
                for row_index in range(ROW_COUNT):
                    rect = (CELL_SIZE * column_index, CELL_SIZE * row_index, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, WHITE, rect, 1)
            for column_index in range(Sp_COLUMN_COUNT):
                for row_index in range(Sp_ROW_COUNT):
                    rect = (Sp_CELL_SIZE * column_index, Sp_CELL_SIZE * row_index, Sp_CELL_SIZE, Sp_CELL_SIZE)
                    pygame.draw.rect(screen,YELLOW, rect, 1)
            if event.type == pygame.QUIT:
                done=True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                index=postoindex(event.pos)
                Sp_index=Sp_postoindex(event.pos)
                if turn == 1:
                    if is_valid_position(Sp_grid[Sp_index], index):
                        Sp_grid[Sp_index][index] = 'X'
                        print('넣음')
                        print([Sp_index,index],)
                        print(Sp_grid[Sp_index])
                        if is_winner(Sp_grid[Sp_index], 'X'):
                            print('X 가 이겼습니다.')
                            game_over = X_WIN 
                            #break
                        elif is_grid_full(Sp_grid[Sp_index]):
                            print('무승부 입니다.')
                            game_over = DRAW 
                            #break
                        turn = 2
                if turn == 2:
                    if is_valid_position(Sp_grid[Sp_index], index):
                        Sp_grid[Sp_index][index] = 'O'
                        print('넣음')
                        print([Sp_index,index],)
                        print(Sp_grid[Sp_index])
                        if is_winner(Sp_grid[Sp_index], 'O'):
                            print('O 가 이겼습니다.')
                            game_over = X_WIN 
                            #break
                        elif is_grid_full(Sp_grid[Sp_index]):
                            print('무승부 입니다.')
                            game_over = DRAW 
                            #break
                        turn = 1
            pygame.display.update()

runGame()
pygame.quit()