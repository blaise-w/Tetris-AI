import pygame
from tetristry import Game
from tetristry import GameInfo
import neat
import os
import time
import pickle

class TetrisGame:
    def __init__(self, window, width, height):
        self.game = Game(window, width, height)

    def test_ai(self):



        width, height = 800, 700
        window = pygame.display.set_mode((width, height))

        game = Game(window, width, height)


        last_score = Game.max_score()
        locked_positions = {}
        grid = Game.create_grid(locked_positions)
        change_piece = False
        run = True
        current_piece = Game.get_shape()
        next_piece = Game.get_shape()
        clock = pygame.time.Clock()
        fall_time = 0
        fall_speed = 0.27
        level_time = 0
        score = 0
        holes = 0

        game_info = GameInfo(score, current_piece.shape, holes, 0, 0)

        while(run):
            
            grid = Game.create_grid(locked_positions)

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
                if not(Game.valid_space(current_piece, grid)) and current_piece.y > 0:
                    current_piece.y -= 1
                    change_piece = True
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    break

                if event.type == pygame.KEYDOWN:
                    Game.move_piece(current_piece, event, grid)

            shape_pos = Game.convert_shape_format(current_piece)

            for i in range(len(shape_pos)):
                x, y = shape_pos[i]
                if y > -1:
                    grid[y][x] = current_piece.color

            if change_piece:
                for pos in shape_pos:
                    p = (pos[0], pos[1])
                    locked_positions[p] = current_piece.color
                current_piece = next_piece
                next_piece = Game.get_shape()
                change_piece = False
                game_info.score += Game.clear_rows(grid, locked_positions) * 10

            Game.draw_window(window, grid, game_info.score, last_score)
            Game.draw_next_shape(next_piece, window)
            pygame.display.update()    
                
            last_score, locked_positions, current_piece, next_piece, clock, level_time, game_info, fall_time, run = game.main(window, last_score, locked_positions, current_piece, next_piece, clock, level_time, game_info, fall_time, run)


            pygame.quit()

    def train_ai(self, genome1, config):
        
        width, height = 800, 700
        window = pygame.display.set_mode((width, height))

        game = Game(window, width, height)



        last_score = Game.max_score()
        locked_positions = {}
        grid = Game.create_grid(locked_positions)
        change_piece = False
        run = True
        current_piece = Game.get_shape()
        next_piece = Game.get_shape()
        clock = pygame.time.Clock()
        fall_time = 0
        fall_speed = 0.27
        level_time = 0
        score = 0

        start_time = time.time()

        net1 = neat.nn.FeedForwardNetwork.create(genome1, config)
        self.genome1 = genome1

        max_score = 100000

        
        game_info = GameInfo(score, current_piece.shape, 0, 0, 0)
        

        while run:
            grid = Game.create_grid(locked_positions)

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
                if not(Game.valid_space(current_piece, grid)) and current_piece.y > 0:
                    current_piece.y -= 1
                    change_piece = True
            
                    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return True
            

            self.move_ai(net1, grid, current_piece, game_info.holes, game_info.bumpiness, game_info.height)

            shape_pos = Game.convert_shape_format(current_piece)

            for i in range(len(shape_pos)):
                x, y = shape_pos[i]
                if y > -1:
                    grid[y][x] = current_piece.color

            if change_piece:
                for pos in shape_pos:
                    p = (pos[0], pos[1])
                    locked_positions[p] = current_piece.color
                current_piece = next_piece
                next_piece = Game.get_shape()
                change_piece = False
                game_info.score += Game.clear_rows(grid, locked_positions) * 10
                game_info.blocks_placed += 1



            Game.draw_window(window, grid, game_info.score, last_score)
            Game.draw_next_shape(next_piece, window)
            pygame.display.update() 
            

            last_score, locked_positions, current_piece, next_piece, clock, level_time, game_info, fall_time, run = game.main(window, last_score, locked_positions, current_piece, next_piece, clock, level_time, game_info, fall_time, run)
      

            duration = time.time() - start_time
            
            if run == False or game_info.score >= max_score:
                self.calculate_fitness(game_info, duration)
                #print("calculated fitness")
                break

        return False

    def move_ai(self, net, grid, piece, holes, bumpiness, height):
        #print(piece.shape_index)
        output = net.activate((piece.shape_index, holes, bumpiness, height))
        decision = output.index(max(output))
        #print(decision)

        valid = Game.automove(decision, piece, grid)
        if not valid:
            self.genome1.fitness -= 1

        ###



    def calculate_fitness(self, game_info, duration):
        self.genome1.fitness += game_info.score - 0.3*game_info.holes - 0.3*game_info.bumpiness - game_info.height + game_info.blocks_placed + duration

def eval_genomes(genomes, config):
    """
    Run each genome against eachother one time to determine the fitness.
    """
    width, height = 800, 700
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tetris")

    for i, (genome_id1, genome1) in enumerate(genomes):
        print(round(i/len(genomes) * 100), end=" ")
        genome1.fitness = 0

        tetris = TetrisGame(win, width, height)

        force_quit = tetris.train_ai(genome1, config)
        if force_quit:
            quit()

def run_neat(config):
    #p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-85')
    p = neat.Population(config)
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    p.add_reporter(neat.Checkpointer(1))

    winner = p.run(eval_genomes, 2000)
    with open("best.pickle", "wb") as f:
        pickle.dump(winner, f)  

if __name__ == '__main__':
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config.txt')

    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_path)

    run_neat(config)
    #test_best_network(config)