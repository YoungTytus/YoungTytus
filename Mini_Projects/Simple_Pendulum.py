import pygame, math

def main():
    width, height = 400, 400
    clock = pygame.time.Clock()
    angle = math.pi / 4
    angleV, angleA = 0.001, 0
    gravity = 2
    origin = pygame.math.Vector2(width / 2, 0)
    circle = pygame.math.Vector2()
    lenth = 300

    success = pygame.init()
    if success[1] > 0:
        print(f'Error: {success[1]}')
    else:
        print('Success')

    pygame.init()
    window = pygame.display.set_mode([width, height])
    pygame.display.set_caption('Simple Pendulum')
    while True:
        window.fill(pygame.Color('Gray'))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
        force = gravity * math.sin(angle)
        angleA = -1 * force / lenth

        angleV += angleA
        angle += angleV

        angleV *= .999

        circle.x = lenth * math.sin(angle) + origin.x
        circle.y = lenth * math.cos(angle) + origin.y

        x = pygame.draw.line(window, pygame.Color('Black'), [origin.x, origin.y], [circle.x, circle.y], 3)
        pygame.draw.circle(window, pygame.Color('DarkRed'), [circle.x, circle.y], 25)
        pygame.display.update()
        clock.tick(60)


if __name__ == '__main__':
    main()
