import pygame, sys, time, random

# Initialize Pygame
pygame.init()

difficulty = 15
frame_size_x = 720
frame_size_y = 480

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

# Initialize game window
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((frame_size_x, frame_size_y))
fps_controller = pygame.time.Clock()

# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(3, (frame_size_y//10)) * 10]
food_spawn = True
direction = 'RIGHT'
change_to = direction
score = 0
high_score = 0

# Game Over function
def game_over():
    global score, high_score, snake_pos, snake_body, food_pos, food_spawn
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (frame_size_x/2, frame_size_y/4)
    game_window.fill(black)
    game_window.blit(game_over_surface, game_over_rect)

    play_again_surface = my_font.render('Play Again', True, green)
    play_again_rect = play_again_surface.get_rect()
    play_again_rect.midtop = (frame_size_x/2, frame_size_y/2)
    game_window.blit(play_again_surface, play_again_rect)

    show_score(0, red, 'times', 20)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if play_again_rect.collidepoint(mouse_pos):
                    reset_game()

def reset_game():
    global score, snake_pos, snake_body, food_pos, food_spawn, direction, change_to
    score = 0
    snake_pos = [100, 50]
    snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]
    food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(3, (frame_size_y//10)) * 10]
    food_spawn = True
    direction = 'RIGHT'
    change_to = direction
    main()

# Score display function
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score) + ' High Score: ' + str(high_score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (frame_size_x / 2, 15)
    else:
        score_rect.midtop = (frame_size_x / 2, frame_size_y / 1.25)
    game_window.blit(score_surface, score_rect)

def main():
    global change_to, direction, food_pos, food_spawn, score, high_score, snake_body, snake_pos
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_UP, ord('w')]:
                    change_to = 'UP'
                if event.key in [pygame.K_DOWN, ord('s')]:
                    change_to = 'DOWN'
                if event.key in [pygame.K_LEFT, ord('a')]:
                    change_to = 'LEFT'
                if event.key in [pygame.K_RIGHT, ord('d')]:
                    change_to = 'RIGHT'

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            score += 1
            if score > high_score:
                high_score = score
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (frame_size_x//10)) * 10, random.randrange(3, (frame_size_y//10)) * 10]
        food_spawn = True

        game_window.fill(black)
        for pos in snake_body:
            pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(game_window, white, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        if snake_pos[0] < 0 or snake_pos[0] > frame_size_x-10 or snake_pos[1] < 30 or snake_pos[1] > frame_size_y-10:
            game_over()
        for block in snake_body[1:]:
            if block[0] == snake_pos[0] and block[1] == snake_pos[1]:
                game_over()

        show_score(1, white, 'consolas', 20)
        pygame.display.update()
        fps_controller.tick(difficulty)

main()

