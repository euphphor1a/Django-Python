import pygame
import sys


def win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeroes == 0:
        return 'Piece'
    return False


pygame.init()

size_block = 100
margin = 15
width = height = size_block * 3 + margin * 4

size_window = (width, height)
screen = pygame.display.set_mode(size_window)
pygame.display.set_caption("Tic-Tac-Toe")

teal = (0, 128, 128)
purple = (128, 0, 128)

mas = [[0] * 3 for i in range(3)]
query = 0
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            col = x_mouse // (margin + size_block)
            row = y_mouse // (margin + size_block)
            if mas[row][col] == 0:
                if query % 2 == 0:
                    mas[row][col] = 'x'
                else:
                    mas[row][col] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0

    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = teal
                elif mas[row][col] == 'o':
                    color = purple
                else:
                    color = (255, 255, 255)
                x = col * size_block + (col + 1) * margin
                y = row * size_block + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, size_block, size_block))
                if color == teal:
                    pygame.draw.line(screen, (255, 255, 255), (x + 5, y + 5), (size_block + x - 5, size_block + y - 5), 5)
                    pygame.draw.line(screen, (255, 255, 255), (x + size_block - 5, y + 5), (x + 5, size_block + y - 5), 5)
                elif color == purple:
                    pygame.draw.circle(screen, (255, 255, 255), (x + size_block // 2, y + size_block // 2), size_block // 2 - 3, 3)

    if (query - 1) % 2 == 0:
        game_over = win(mas, 'x')
    else:
        game_over = win(mas, 'o')

    if game_over:
        screen.fill((30, 30, 30))
        font = pygame.font.SysFont('stxingkai', 80)
        if game_over == 'x':
            text = font.render("Крестики!", True, (255, 255, 255))
        elif game_over == 'o':
            text = font.render("Нолики!", True, (255, 255, 255))
        else:
            text = font.render("Ничья!", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text, [text_x, text_y])

    pygame.display.update()

