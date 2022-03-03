import pygame, random

frame_size_x = 640
frame_size_y = 480

check_error = pygame.init()
if check_error[1] > 0:
    print('Error' + str(check_error[1]))
else:
    print('Succes initialized')

pygame.display.set_caption('Snake')
game = pygame.display.set_mode([frame_size_x, frame_size_y])

black = pygame.Color('black')
white = pygame.Color('white')
red = pygame.Color('red')

fps_controler = pygame.time.Clock()

square_size = 20


def init_vars():
    global head_pos, snake_body, food_pos, food_spawn, score, direction, speed
    direction = "RIGHT"
    head_pos = [frame_size_x / 2, frame_size_x / 2]
    snake_body = [[head_pos]]
    food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size,
                random.randrange(1, (frame_size_y // square_size)) * square_size]
    food_spawn = True
    score = 0
    speed = 15


init_vars()

def show_score_speed(color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render(f'Score: {score}', True, color)
    speed_surface = score_font.render(f'Speed: {speed}', True, color)
    score_rect = score_surface.get_rect()
    speed_rect = speed_surface.get_rect()
    score_rect.midtop = (frame_size_x / 10, 15)
    speed_rect.midtop = (frame_size_x / 10, 35)

    game.blit(score_surface, score_rect)
    game.blit(speed_surface, speed_rect)


while True:
    game.fill(pygame.Color('DarkGreen'))
    last_len_body = len(snake_body)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_UP or event.key == ord('w')) and direction != 'DOWN':
                direction = 'UP'
            elif (event.key == pygame.K_DOWN or event.key == ord('s')) and direction != 'UP':
                direction = 'DOWN'
            elif (event.key == pygame.K_LEFT or event.key == ord('a')) and direction != 'RIGHT':
                direction = 'LEFT'
            elif (event.key == pygame.K_RIGHT or event.key == ord('d')) and direction != 'LEFT':
                direction = 'RIGHT'

    if direction == 'UP':
        head_pos[1] -= square_size
    elif direction == 'DOWN':
        head_pos[1] += square_size
    elif direction == 'LEFT':
        head_pos[0] -= square_size
    elif direction == 'RIGHT':
        head_pos[0] += square_size

    if head_pos[0] < 0:
        head_pos[0] = frame_size_x - square_size
    elif head_pos[0] > frame_size_x - square_size:
        head_pos[0] = 0
    elif head_pos[1] < 0:
        head_pos[1] = frame_size_y - square_size
    elif head_pos[1] > frame_size_y - square_size:
        head_pos[1] = 0
    # game.fill(black)

    snake_body.insert(0, list(head_pos))
    if head_pos[0] == food_pos[0] and head_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    if not food_spawn:
        food_pos = [random.randrange(1, (frame_size_x // square_size)) * square_size,
                    random.randrange(1, (frame_size_y // square_size)) * square_size]
        food_spawn = True

    for index, pos in enumerate(snake_body):
        if head_pos[0] == pos[0] and head_pos[1] == pos[1]:
            pygame.draw.rect(game, pygame.Color('Green'), pygame.Rect([pos[0], pos[1], square_size, square_size]))
        else:
            if index % 2 == 0:
                color = pygame.Color('Yellow')
            else:
                color = black
            pygame.draw.rect(game, color, pygame.Rect([pos[0], pos[1], square_size, square_size]), 2)
    pygame.draw.rect(game, white, pygame.Rect([food_pos[0], food_pos[1], square_size, square_size]), 2,
                     border_radius=20)

    for block in snake_body[1:]:
        if head_pos[0] == block[0] and head_pos[1] == block[1]:
            init_vars()
    if last_len_body != len(snake_body):
        speed = speed / 25 + speed
        speed = round(speed)

    show_score_speed(white, 'consolas', 20)
    pygame.display.update()
    fps_controler.tick(speed)
