import pygame
import random

pygame.font.init()

class GameInfo:
    def __init__(self, score, piece_type, holes, height, bumpiness):
        self.score = score
        self.piece_type = piece_type
        self.holes = holes
        self.height = height
        self.bumpiness = bumpiness
        self.blocks_placed = 0

class Game:
    def __init__(self, window, width, height):
        self.width = width
        self.height = height
        self.win = window
        pygame.display.set_caption('Tetris')
        #Game.main(self.win)
        
    # GLOBALS VARS
    s_width = 800
    s_height = 700
    play_width = 300  # meaning 300 // 10 = 30 width per block
    play_height = 600  # meaning 600 // 20 = 30 height per block
    block_size = 30

    top_left_x = (s_width - play_width) // 2
    top_left_y = s_height - play_height


    # SHAPE FORMATS

    S = [['.....',
        '.....',
        '..00.',
        '.00..',
        '.....'],
        ['.....',
        '..0..',
        '..00.',
        '...0.',
        '.....']]

    Z = [['.....',
        '.....',
        '.00..',
        '..00.',
        '.....'],
        ['.....',
        '..0..',
        '.00..',
        '.0...',
        '.....']]

    I = [['..0..',
        '..0..',
        '..0..',
        '..0..',
        '.....'],
        ['.....',
        '0000.',
        '.....',
        '.....',
        '.....']]

    O = [['.....',
        '.....',
        '.00..',
        '.00..',
        '.....']]

    J = [['.....',
        '.0...',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..00.',
        '..0..',
        '..0..',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '...0.',
        '.....'],
        ['.....',
        '..0..',
        '..0..',
        '.00..',
        '.....']]

    L = [['.....',
        '...0.',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..0..',
        '..0..',
        '..00.',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '.0...',
        '.....'],
        ['.....',
        '.00..',
        '..0..',
        '..0..',
        '.....']]

    T = [['.....',
        '..0..',
        '.000.',
        '.....',
        '.....'],
        ['.....',
        '..0..',
        '..00.',
        '..0..',
        '.....'],
        ['.....',
        '.....',
        '.000.',
        '..0..',
        '.....'],
        ['.....',
        '..0..',
        '.00..',
        '..0..',
        '.....']]

    shapes = [S, Z, I, O, J, L, T]
    shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
    # index 0 - 6 represent shape




    def create_grid(locked_pos={}):  # *
        grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (j, i) in locked_pos:
                    c = locked_pos[(j,i)]
                    grid[i][j] = c
        return grid


    def convert_shape_format(shape):
        positions = []
        format = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    positions.append((shape.x + j, shape.y + i))

        for i, pos in enumerate(positions):
            positions[i] = (pos[0] - 2, pos[1] - 4)

        return positions


    def valid_space(shape, grid):
        accepted_pos = [[(j, i) for j in range(10) if grid[i][j] == (0,0,0)] for i in range(20)]
        accepted_pos = [j for sub in accepted_pos for j in sub]

        formatted = Game.convert_shape_format(shape)

        for pos in formatted:
            if pos not in accepted_pos:
                if pos[1] > -1:
                    return False
        return True


    def check_lost(positions):
        for pos in positions:
            x, y = pos
            if y < 1:
                return True

        return False


    def get_shape():
        x = random.choice([0, 1, 2, 3, 4, 5, 6])
        y = Game.shapes[x]
        return Piece(5, 0, x, y)


    def draw_text_middle(surface, text, size, color):
        font = pygame.font.SysFont("comicsans", size, bold=True)
        label = font.render(text, 1, color)

        surface.blit(label, (Game.top_left_x + Game.play_width /2 - (label.get_width()/2), Game.top_left_y + Game.play_height/2 - label.get_height()/2))


    def draw_grid(surface, grid):
        sx = Game.top_left_x
        sy = Game.top_left_y

        for i in range(len(grid)):
            pygame.draw.line(surface, (128,128,128), (sx, sy + i*Game.block_size), (sx+Game.play_width, sy+ i*Game.block_size))
            for j in range(len(grid[i])):
                pygame.draw.line(surface, (128, 128, 128), (sx + j*Game.block_size, sy),(sx + j*Game.block_size, sy + Game.play_height))


    def clear_rows(grid, locked):

        inc = 0
        for i in range(len(grid)-1, -1, -1):
            row = grid[i]
            if (0,0,0) not in row:
                inc += 1
                ind = i
                for j in range(len(row)):
                    try:
                        del locked[(j,i)]
                    except:
                        continue

        if inc > 0:
            for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
                x, y = key
                if y < ind:
                    newKey = (x, y + inc)
                    locked[newKey] = locked.pop(key)

        return inc


    def draw_next_shape(shape, surface):
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Next Shape', 1, (255,255,255))

        sx = Game.top_left_x + Game.play_width + 50
        sy = Game.top_left_y + Game.play_height/2 - 100
        format = shape.shape[shape.rotation % len(shape.shape)]

        for i, line in enumerate(format):
            row = list(line)
            for j, column in enumerate(row):
                if column == '0':
                    pygame.draw.rect(surface, shape.color, (sx + j*Game.block_size, sy + i*Game.block_size, Game.block_size, Game.block_size), 0)

        surface.blit(label, (sx + 10, sy - 30))


    def update_score(nscore):
        score = Game.max_score()

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


    def draw_window(surface, grid, score=0, last_score = 0):
        surface.fill((0, 0, 0))

        pygame.font.init()
        font = pygame.font.SysFont('comicsans', 60)
        label = font.render('Tetris', 1, (255, 255, 255))

        surface.blit(label, (Game.top_left_x + Game.play_width / 2 - (label.get_width() / 2), 30))

        # current score
        font = pygame.font.SysFont('comicsans', 30)
        label = font.render('Score: ' + str(score), 1, (255,255,255))

        sx = Game.top_left_x + Game.play_width + 50
        sy = Game.top_left_y + Game.play_height/2 - 100

        surface.blit(label, (sx + 20, sy + 160))
        # last score
        label = font.render('High Score: ' + last_score, 1, (255,255,255))

        sx = Game.top_left_x - 260
        sy = Game.top_left_y + 200

        surface.blit(label, (sx + 20, sy + 160))

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                pygame.draw.rect(surface, grid[i][j], (Game.top_left_x + j*Game.block_size, Game.top_left_y + i*Game.block_size, Game.block_size, Game.block_size), 0)

        pygame.draw.rect(surface, (255, 0, 0), (Game.top_left_x, Game.top_left_y, Game.play_width, Game.play_height), 5)

        Game.draw_grid(surface, grid)
        #pygame.display.update()

    def find_holes(grid):
        holes = 0
        i = 0
        while i < 10:
            counting = False
            j = 0
            while j < 20:
                if grid[j][i] != 0 and not counting:
                    counting = True
                elif grid[j][i] == 0 and counting:
                    holes += 1
                j += 1
            i += 1
        return holes

    def find_bumpiness(grid):
        bumpiness = 0
        prev = -1
        i = 0
        max_height = 0
        while i < 10:
            height = 0
            j = 0
            while j < 20:
                if grid[j][i] != 0:
                    height = 20 - j
                    if height > max_height:
                        max_height = height
                    break
                j += 1
            if prev != -1:
                temp = height - prev
                if temp >= 0:
                    bumpiness += temp
                else:
                    bumpiness -= temp
            prev = height
            i += 1
        return bumpiness, max_height


    def main(x, win, last_score, locked_positions, current_piece, next_piece, clock, level_time, game_info, fall_time, run):  # *
        
        grid = Game.create_grid(locked_positions)
        
        if Game.check_lost(locked_positions):
            Game.draw_text_middle(win, "YOU LOST!", 80, (255,255,255))
            pygame.display.update()
            #pygame.time.delay(1500)
            run = False
            Game.update_score(game_info.score)
            
        game_info.holes = Game.find_holes(grid)
        game_info.bumpiness, game_info.height = Game.find_bumpiness(grid)
        game_info.score = game_info.score
        game_info.piece_type = current_piece.shape    
        return last_score, locked_positions, current_piece, next_piece, clock, level_time, game_info, fall_time, run

    def move_piece(current_piece, event, grid):
        if event.key == pygame.K_LEFT:
            current_piece.x -= 1
            if not(Game.valid_space(current_piece, grid)):
                current_piece.x += 1
        if event.key == pygame.K_RIGHT:
            current_piece.x += 1
            if not(Game.valid_space(current_piece, grid)):
                current_piece.x -= 1
        if event.key == pygame.K_DOWN:
            current_piece.y += 1
            if not(Game.valid_space(current_piece, grid)):
                current_piece.y -= 1
        if event.key == pygame.K_UP:
            current_piece.rotation += 1
            if not(Game.valid_space(current_piece, grid)):
                current_piece.rotation -= 1


    def main_menu(win):  # *
        run = True
        while run:
            win.fill((0,0,0))
            Game.draw_text_middle(win, 'Press Any Key To Play', 60, (255,255,255))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    Game.main(win)

        pygame.display.quit()

    def automove(decision, piece, grid):
        valid = True
        rotation = decision % 4
        x = decision % 10
        

        save = piece.x
        save2 = piece.rotation

        piece.x = x
        piece.rotation = rotation

        if not Game.valid_space(piece, grid):
            piece.x = save
            piece.rotation = save2
            return False

        Game.drop(piece, grid)
        return True

    def drop(piece, grid):
        while True:
            if Game.valid_space(piece, grid):
                piece.y += 1
            else:
                piece.y -= 1
                break







class Piece(object):  # *
        def __init__(self, x, y, shape_index, shape):
            self.x = x
            self.y = y
            self.shape_index = shape_index
            self.shape = shape
            self.color = Game.shape_colors[Game.shapes.index(shape)]
            self.rotation = 0

#win = pygame.display.set_mode((Game.s_width, Game.s_height))
#pygame.display.set_caption('Tetris')
#Game.main_menu(win)