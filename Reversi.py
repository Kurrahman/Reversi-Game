import pygame
import random

board = [
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,1,2,0,0,0],
    [0,0,0,2,1,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
]
valid_tile = [
    [2,2],[2,3],[2,4],[2,5],
    [3,2],[3,5],
    [4,2],[4,5],
    [5,2],[5,3],[5,4],[5,5]
]
piece = [2,2]
def init(screen):
    pygame.init()
    pygame.display.set_caption("Reversi")
    screen = pygame.display.set_mode((242,242))
    for i in range(0,8):
        for j in range(0,8):
            pygame.draw.rect(screen, (28, 140, 11), [i*30+2, j*30+2, 28 ,28])
    pygame.draw.circle(screen, (255,255,255), [106, 106], 14)
    pygame.draw.circle(screen, (0,0,0), [106, 136], 14)
    pygame.draw.circle(screen, (255,255,255), [136, 136], 14)
    pygame.draw.circle(screen, (0,0,0), [136, 106], 14)

def click_tile(tile, turn, screen):
    valid_tile.remove(tile)
    x = tile[0]
    y = tile[1]
    pygame.draw.circle(screen, (turn*255,turn*255,turn*255), [y*30+16, x*30+16], 14)
    turn = (turn + 1) % 2
    piece[turn] += 1 
    board[x][y] = turn + 1
    # mengecek ke arah mana harus mengubah sisi
    if (bot(x,y,((turn + 1) % 2) + 1)):
        swapbot(x,y,turn+1, screen)
    if (top(x,y,((turn + 1) % 2) + 1)):
        swaptop(x,y,turn+1, screen)
    if (left(x,y,((turn + 1) % 2) + 1)):
        swapleft(x,y,turn+1, screen)
    if (right(x,y,((turn + 1) % 2) + 1)):
        swapright(x,y,turn+1, screen)
    if (botleft(x,y,((turn + 1) % 2) + 1)):
        swapbotleft(x,y,turn+1, screen)
    if (topleft(x,y,((turn + 1) % 2) + 1)):
        swaptopleft(x,y,turn+1, screen)
    if (topright(x,y,((turn + 1) % 2) + 1)):
        swaptopright(x,y,turn+1, screen)
    if (botright(x,y,((turn + 1) % 2) + 1)):
        swapbotright(x,y,turn+1, screen)
    # menambahkan tile yang baru valid ke valid_tiles
    if (bot(x,y,0)) & ([x+1, y] not in valid_tile):
        valid_tile.append([x+1,y])
    if (top(x,y,0)) & ([x-1, y] not in valid_tile):
        valid_tile.append([x-1,y])
    if (left(x,y,0)) & ([x, y-1] not in valid_tile):
        valid_tile.append([x,y-1])
    if (right(x,y,0)) & ([x, y+1] not in valid_tile):
        valid_tile.append([x,y+1])
    if (botleft(x,y,0)) & ([x+1, y-1] not in valid_tile):
        valid_tile.append([x+1,y-1])
    if (topright(x,y,0)) & ([x-1, y+1] not in valid_tile):
        valid_tile.append([x-1,y+1])
    if (topleft(x,y,0)) & ([x-1, y-1] not in valid_tile):
        valid_tile.append([x-1,y-1])
    if (botright(x,y,0)) & ([x+1, y+1] not in valid_tile):
        valid_tile.append([x+1,y+1])
    if(valid_tile == []):
        if (piece[0] > piece[1]):
            print("WHITE WINS!")
            return 0
        elif(piece[0] < piece[1]):
            print("BLACK WINS!")
            return 0
        else:
            print("IT'S A DRAW!")
            return 0
    elif (piece[0] == 0):
        print("BLACK WINS!")
        return 0
    elif (piece[1] == 0):
        print("WHITE WINS!")
        return 0
# Vertical
def bot(x,y,side):
    if (0 <= x < 7) & (0 <= y < 8):
        return board[x+1][y] == side
    else:
        return False
def top(x,y,side):
    if (0 < x <= 7) & (0 <= y < 8):
        return board[x-1][y] == side
    else:
        return False
# Horizontal
def left(x,y,side):
    if (0 <= x < 8) & (0 < y <= 7):
        return board[x][y-1] == side
    else:
        return False
def right(x,y,side):
    if (0 <= x < 8) & (0 <= y < 7):
        return board[x][y+1] == side
    else:
        return False
# Diagonal
def topleft(x,y,side):
    if (0 < x < 8) & (0 < y < 8):
        return board[x-1][y-1] == side
    else:
        return False
def topright(x,y,side):
    if (0 < x < 8) & (0 <= y < 7):
        return board[x-1][y+1] == side
    else:
        return False
def botleft(x,y,side):
    if (0 <= x < 7) & (0 < y < 8):
        return board[x+1][y-1] == side
    else:
        return False
def botright(x,y,side):
    if (0 <= x < 7) & (0 <= y < 7):
        return board[x+1][y+1] == side
    else:
        return False

def swapbot(x,y, side, screen):
    swap = False
    if side == 1:
        op = 2
    else:
        op = 1
    xtmp = x
    while bot(x,y,op):
        x += 1
        if bot(x,y,side):
            swap = True
    x = xtmp
    if (swap):
        while bot(x,y,op):
            x += 1
            board[x][y] = side
            piece[side-1] += 1
            piece[op-1] -= 1
            pygame.draw.circle(screen, ((side%2)*255,(side%2)*255,(side%2)*255), [y*30+16, x*30+16], 14)
            pygame.display.flip()
    
def swaptop(x,y,side,screen):
    swap = False
    if side == 1:
        op = 2
    else:
        op = 1
    xtmp = x
    while top(x,y,op):
        x -= 1
        if top(x,y,side):
            swap = True
    x = xtmp
    if (swap):
        while top(x,y,op):
            x -= 1
            board[x][y] = side
            piece[side-1] += 1
            piece[op-1] -= 1
            pygame.draw.circle(screen, ((side%2)*255,(side%2)*255,(side%2)*255), [y*30+16, x*30+16], 14)
            pygame.display.flip()

def swapleft(x,y,side,screen):
    swap = False
    if side == 1:
        op = 2
    else:
        op = 1
    ytmp = y
    while left(x,y,op):
        y -= 1
        if left(x,y,side):
            swap = True
    y = ytmp
    if (swap):
        while left(x,y,op):
            y -= 1
            board[x][y] = side
            piece[side-1] += 1
            piece[op-1] -= 1
            pygame.draw.circle(screen, ((side%2)*255,(side%2)*255,(side%2)*255), [y*30+16, x*30+16], 14)
            pygame.display.flip()

def swapright(x,y,side,screen):
    swap = False
    if side == 1:
        op = 2
    else:
        op = 1
    ytmp = y
    while right(x,y,op):
        y += 1
        if right(x,y,side):
            swap = True
    y = ytmp
    if (swap):
        while right(x,y,op):
            y += 1
            board[x][y] = side
            piece[side-1] += 1
            piece[op-1] -= 1
            pygame.draw.circle(screen, ((side%2)*255,(side%2)*255,(side%2)*255), [y*30+16, x*30+16], 14)
            pygame.display.flip()

def swaptopleft(x,y,side,screen):
    swap = False
    if side == 1:
        op = 2
    else:
        op = 1
    xtmp = x
    ytmp = y
    while topleft(x,y,op):
        x -= 1
        y -= 1
        if topleft(x,y,side):
            swap = True
        print(x)
    x = xtmp
    y = ytmp
    if (swap):
        while topleft(x,y,op):
            x -= 1
            y -= 1
            board[x][y] = side
            piece[side-1] += 1
            piece[op-1] -= 1
            pygame.draw.circle(screen, ((side%2)*255,(side%2)*255,(side%2)*255), [y*30+16, x*30+16], 14)
            pygame.display.flip()

def swaptopright(x,y,side,screen):
    swap = False
    if side == 1:
        op = 2
    else:
        op = 1
    xtmp = x
    ytmp = y
    while topright(x,y,op):
        x -= 1
        y += 1
        if topright(x,y,side):
            swap = True
        print(x)
    x = xtmp
    y = ytmp
    if (swap):
        while topright(x,y,op):
            x -= 1
            y += 1
            board[x][y] = side
            piece[side-1] += 1
            piece[op-1] -= 1
            pygame.draw.circle(screen, ((side%2)*255,(side%2)*255,(side%2)*255), [y*30+16, x*30+16], 14)
            pygame.display.flip()

def swapbotleft(x,y,side,screen):
    swap = False
    if side == 1:
        op = 2
    else:
        op = 1
    xtmp = x
    ytmp = y
    while botleft(x,y,op):
        x += 1
        y -= 1
        if botleft(x,y,side):
            swap = True
        print(x)
    x = xtmp
    y = ytmp
    if (swap):
        while botleft(x,y,op):
            x += 1
            y -= 1
            board[x][y] = side
            piece[side-1] += 1
            piece[op-1] -= 1
            pygame.draw.circle(screen, ((side%2)*255,(side%2)*255,(side%2)*255), [y*30+16, x*30+16], 14)
            pygame.display.flip()

def swapbotright(x,y,side,screen):
    swap = False
    if side == 1:
        op = 2
    else:
        op = 1
    xtmp = x
    ytmp = y
    while botright(x,y,op):
        x += 1
        y += 1
        if botright(x,y,side):
            swap = True
        print(x)
    x = xtmp
    y = ytmp
    if (swap):
        while botright(x,y,op):
            x += 1
            y += 1
            board[x][y] = side
            piece[side-1] += 1
            piece[op-1] -= 1
            pygame.draw.circle(screen, ((side%2)*255,(side%2)*255,(side%2)*255), [y*30+16, x*30+16], 14)
            pygame.display.flip()

#greedy
def greedbot(x,y):
    swap = False
    black = piece[1]
    xtmp = x
    while bot(x,y,1):
        x += 1
        if bot(x,y,2):
            swap = True
    x = xtmp
    if (swap):
        while bot(x,y,1):
            x += 1
            black += 1
    return black

def greedtop(x,y):
    swap = False
    black = piece[1]
    xtmp = x
    while top(x,y,1):
        x -= 1
        if top(x,y,2):
            swap = True
    x = xtmp
    if (swap):
        while top(x,y,1):
            x -= 1
            black += 1
    return black

def greedright(x,y):
    swap = False
    black = piece[1]
    ytmp = y
    while right(x,y,1):
        y += 1
        if right(x,y,2):
            swap = True
    y = ytmp
    if (swap):
        while right(x,y,1):
            y += 1
            black += 1
    return black

def greedleft(x,y):
    swap = False
    black = piece[1]
    ytmp = y
    while left(x,y,1):
        y -= 1
        if left(x,y,2):
            swap = True
    y = ytmp
    if (swap):
        while left(x,y,1):
            y -= 1
            black += 1
    return black

def greedtopleft(x,y):
    swap = False
    black = piece[1]
    xtmp = x
    ytmp = y
    while topleft(x,y,1):
        x -= 1
        y -= 1
        if topleft(x,y,2):
            swap = True
    x = xtmp
    y = ytmp
    if (swap):
        while topleft(x,y,1):
            x -= 1
            y -= 1
            black += 1
    return black

def greedtopright(x,y):
    swap = False
    black = piece[1]
    xtmp = x
    ytmp = y
    while topright(x,y,1):
        x -= 1
        y += 1
        if topright(x,y,2):
            swap = True
    x = xtmp
    y = ytmp
    if (swap):
        while topright(x,y,1):
            x -= 1
            y += 1
            black += 1
    return black

def greedbotright(x,y):
    swap = False
    black = piece[1]
    xtmp = x
    ytmp = y
    while botright(x,y,1):
        x += 1
        y += 1
        if botright(x,y,2):
            swap = True
    x = xtmp
    y = ytmp
    if (swap):
        while botright(x,y,1):
            x += 1
            y += 1
            black += 1
    return black

def greedbotleft(x,y):
    swap = False
    black = piece[1]
    xtmp = x
    ytmp = y
    while botleft(x,y,1):
        x += 1
        y -= 1
        if botleft(x,y,2):
            swap = True
    x = xtmp
    y = ytmp
    if (swap):
        while botleft(x,y,1):
            x += 1
            y -= 1
            black += 1
    return black

def greed(screen):
    tmp = []
    mak = 0
    for tile in valid_tile:
        point = (
            greedright(tile[0],tile[1]) +
            greedleft(tile[0], tile[1]) +
            greedtop(tile[0], tile[1]) +
            greedbot(tile[0], tile[1]) +
            greedtopleft(tile[0], tile[1]) +
            greedtopright(tile[0], tile[1]) +
            greedbotleft(tile[0], tile[1]) +
            greedbotright(tile[0], tile[1])
        )
        if point >= mak:
            tmp = tile
            mak = point
    if click_tile(tmp, 0, screen) != None:
        return 0
    
def main():
    screen = pygame.display.set_mode((242,242))
    init(screen)
    turn = 1
    running = True
    while running:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x = (mouse_pos[1] // 30)
                y = (mouse_pos[0] // 30)
                tile = [x,y]
                if  tile in valid_tile:
                    if click_tile(tile, turn, screen) != None:
                        return
                    if greed(screen) != None:
                        return
                

if __name__ ==  "__main__":
    main()