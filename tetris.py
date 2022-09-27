from tkinter import Grid
import pygame
import random

pygame.font.init()

# Global Variables:

s_width = 800
s_height = 700
play_width = 300  # meaning 300 // 10 = 30 width per block
play_height = 600  # meaning 600 // 20 = 20 height per block
block_size = 30

top_left_x = (s_width - play_width) // 2
top_left_y = s_height - play_height


# Shapes:

blocks = [
                # O
                [
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 0, 0, 0]
                        ]
                ],

                # I
                [
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [1, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 1],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0]
                        ]
                ],

                # T
                [
                        [
                                [0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 1, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 0, 1, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 1, 0, 0, 0],
                                [0, 1, 1, 0, 0],
                                [0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0]
                        ],
                ],

                # S
                [
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 1, 0],
                                [0, 1, 1, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 0, 1, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 1, 0],
                                [0, 1, 1, 0, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 1, 0, 0, 0],
                                [0, 1, 1, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0]
                        ]
                ],

                # Z
                [
                        [
                                [0, 0, 0, 0, 0],
                                [0, 1, 1, 0, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 1, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 1, 1, 0, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 1, 1, 0, 0],
                                [0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0]
                        ]
                ],

                # L
                [
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 0],
                                [0, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 1, 1, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 1, 0],
                                [0, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0]
                        ]
                ],

                # J
                [
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 1, 1, 0, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 1, 0, 0, 0],
                                [0, 1, 1, 1, 0],
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 1, 1, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0]
                        ],
                        [
                                [0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0],
                                [0, 1, 1, 1, 0],
                                [0, 0, 0, 1, 0],
                                [0, 0, 0, 0, 0]
                        ],
                ]
        ]


# Start Posiitons:

starty = [
                # O
                [-2, -2, -2, -2],
                # I
                [-1, -2, 0, -2],
                # T
                [-1, -1, -2, -1],
                # S
                [-1, -1, -2, -1],
                # Z
                [-1, -1, -2, -1],
                # L
                [-1, -2, -1, -1],
                # J
                [-1, -1, -1, -2]
]


class block(object):

    def __init__(self):
        self.type = getRandomBlockType()
        self.rotation = random.randint(0, 3)
        self.color = random.randint(1, 7)
        print(self.type)
        print(self.rotation)
        print(self.color)
        self.x = getStartX(self.type, self.rotation, self.color)
        self.y = getStartY(self.type, self.rotation)

def getBlock():
    return block()
        
        
def getRandomBlockType():
    n = random.randint(0, 6)
    return n
    # O, I, T, S, Z, L, J
    # 0, 1, 2, 3, 4, 5, 6

def getStartX(type, rotation, color):
    i = 0
    while i < 5:
        j = 0
        while j < 5:
            if getCell(type, rotation, i , j, color) != 0:
                return 4 - i
            j += 1
        i += 1
    return 0

def getStartY(type, rotation):
    return starty[type][rotation]

def getCell(type, rotation, u, v, color):
    return (blocks[type][rotation][v][u])*color

def makeBoard():
    global grid
    grid = [[0 for x in range(10)] for x in range(20)]
    return grid

def addBlock(block):
    x = block.x
    y = block.y
    for i in range(5):
        for j in range(5):
            if getCell(block.type, block.rotation, i, j, block.color) != 0:
                grid[x + 1][y + j] = getCell(block.type, block.rotation, i, j, block.color)

def clearLine(y):
    j = y
    while j > 0:
        for i in range(10):
            grid[i][j] = grid[i][j - 1]
        j = j - 1

def findFilledLines():
    cleared = 0
    for j in range(10):
        full = True
        for i in range(20):
            if grid[i][j] == 0: full = False
        if full:
            clearLine(j)
            cleared += 1
    return cleared

def goodMove(block):
    if getStartY(block.type, block.rotation) > block.y: return False
    x = block.x
    y = block.y
    for j in range(5):
        for i in range(5):
            if getCell(block.type, block.rotation, i, j, block.color) != 0:
                if ((x + i) < 0 or (x + i) > 9 or (y + j) > 19):
                    return False
                if (grid[y + j][x + i] != 0):
                    return False
    return True

def gameOver():
    for i in range(10):
        if grid[0][i] != 0:
            return True
    return False

def inbounds(x, y):
    return (x >= 0 and x < 10 and y >= 0 and y < 20)


def draw_text_middle(surface, text, size, color):
    font = pygame.font.SysFont("comicsans", size, bold=True)
    label = font.render(text, 1, color)

    surface.blit(label, (top_left_x + play_width /2 - (label.get_width()/2), top_left_y + play_height/2 - label.get_height()/2))


def draw_grid(surface, grid):
    sx = top_left_x
    sy = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, (128,128,128), (sx, sy + i*block_size), (sx+play_width, sy+ i*block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (sx + j*block_size, sy),(sx + j*block_size, sy + play_height))

def draw_window(surface, grid, score=0, last_score = 0):
    surface.fill((0, 0, 0))

    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 60)
    label = font.render('Tetris', 1, (255, 255, 255))

    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    # current score
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Score: ' + str(score), 1, (255,255,255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100

    surface.blit(label, (sx + 20, sy + 160))
    # last score
    label = font.render('High Score: ' + last_score, 1, (255,255,255))

    sx = top_left_x - 260
    sy = top_left_y + 200

    surface.blit(label, (sx + 20, sy + 160))
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j], (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)

    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)

    draw_grid(surface, grid)

def draw_next_shape(shape, surface):
    font = pygame.font.SysFont('comicsans', 30)
    label = font.render('Next Shape', 1, (255,255,255))

    sx = top_left_x + play_width + 50
    sy = top_left_y + play_height/2 - 100

    ##
    for i in range(5):
        for j in range(5):
            getCell(shape.type, shape.rotation, i, j, shape.color)

    format = shape.type[shape.rotation % len(shape.type)]

    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == '0':
                pygame.draw.rect(surface, shape.color, (sx + j*30, sy + i*30, 30, 30), 0)

    surface.blit(label, (sx + 10, sy- 30))


def main(win):  # *
    last_score = max_score()
    grid = makeBoard()
    

    change_piece = False
    run = True
    current_piece = getBlock()
    next_piece = getBlock()
    clock = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.27
    level_time = 0
    score = 0

    while run:
        fall_time += clock.get_rawtime()
        level_time += clock.get_rawtime()
        clock.tick()

        if level_time/1000 > 5:
            level_time = 0
            if level_time > 0.12:
                level_time -= 0.005

        if fall_time/1000 > fall_speed:
            fall_time = 0
            current_piece.y += 1
            if not(goodMove(current_piece)) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not(goodMove(current_piece)):
                        current_piece.x += 1
                if event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not(goodMove(current_piece)):
                        current_piece.x -= 1
                if event.key == pygame.K_DOWN:
                    current_piece.y += 1
                    if not(goodMove(current_piece)):
                        current_piece.y -= 1
                if event.key == pygame.K_UP:
                    current_piece.rotation += 1
                    if current_piece.rotation > 3:
                        current_piece.rotation = 0
                    if not(goodMove(current_piece)):
                        current_piece.rotation -= 1

        ###

        addBlock(current_piece)

        if change_piece:
            #addBlock(current_piece)
            current_piece = next_piece
            next_piece = getBlock()
            change_piece = False
            score += findFilledLines() * 10

        draw_window(win, grid, score, last_score)
        #draw_next_shape(next_piece, win)
        pygame.display.update()

        if gameOver():
            draw_text_middle(win, "YOU LOST!", 80, (255,255,255))
            pygame.display.update()
            pygame.time.delay(1500)
            run = False
            update_score(score)

def update_score(nscore):
    score = max_score()

    with open('scores.txt', 'w') as f:
        if int(score) > nscore:
            f.write(str(score))
        else:
            f.write(str(nscore))

def max_score():
    with open('scores.txt', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()

    return score


def main_menu(win):  # *
    run = True
    while run:
        win.fill((0,0,0))
        draw_text_middle(win, 'Press Any Key To Play', 60, (255,255,255))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                main(win)

    pygame.display.quit()

win = pygame.display.set_mode((s_width, s_height))
pygame.display.set_caption('Tetris')
main_menu(win)
