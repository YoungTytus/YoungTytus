import pygame, random


def main():
    success = pygame.init()
    if success[1] > 0:
        print(f'Error: {success[1]}')
    else:
        print('Success')
    pygame.init()
    window = pygame.display.set_mode([width, height])
    pygame.display.set_caption('Bubble Sort')
    arr = random.sample(range(width), width)
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quit()
        pygame.time.delay(10)
        start = False
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            start = True
        if start:
            show(window, arr)
            pygame.display.update()
            arr_lenth = len(arr)
            for i in range(arr_lenth):
                for j in range(arr_lenth - i - 1):
                    window.fill('black')
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    show(window, arr)
                    pygame.display.update()
        else:
            window.fill('black')
            show(window, arr)
            pygame.display.update()


def show(window, arr):
    for i in range(len(arr)):
        pygame.draw.line(window, 'white', [i, height], [i, height - arr[i]])


if __name__ == '__main__':
    width = height = 400
    main()
