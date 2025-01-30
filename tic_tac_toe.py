import pygame
import sys
import random

SW, SH = 600, 600
BLOCK_SIZE = 200

pygame.init()
screen = pygame.display.set_mode((SW, SH))
screen.fill('white')
pygame.display.set_caption("O_and_X")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 50)

board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False
winner_text = ""

def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "black", rect, 1)

def draw_symbol(x, y, player):
    center_x = x * BLOCK_SIZE + BLOCK_SIZE // 2
    center_y = y * BLOCK_SIZE + BLOCK_SIZE // 2

    if player == "X":
        offset = 50
        pygame.draw.line(screen, "black", (center_x - offset, center_y - offset), 
                         (center_x + offset, center_y + offset), 5)
        pygame.draw.line(screen, "black", (center_x + offset, center_y - offset), 
                         (center_x - offset, center_y + offset), 5)
    else:
        pygame.draw.circle(screen, "black", (center_x, center_y), 50, 5)

def check_winner():
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != "":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]

    if all(board[row][col] != "" for row in range(3) for col in range(3)):
        return "Remis"
    
    return None

def minimax(board, depth, is_maximizing):
    result = check_winner()
    if result == "X":
        return -1
    elif result == "O":
        return 1
    elif result == "Remis":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = "O"
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ""
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    board[row][col] = "X"
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ""
                    best_score = min(score, best_score)
        return best_score



def best_move():
    if random.random() < 0.2:  # 20% szans na błąd
        return random.choice([(r, c) for r in range(3) for c in range(3) if board[r][c] == ""])
    
    best_score = -float("inf")
    move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == "":
                board[row][col] = "O"
                score = minimax(board, 0, False)
                board[row][col] = ""
                if score > best_score:
                    best_score = score
                    move = (row, col)
    return move


def show_winner_screen(text):
    screen.fill("white")
    text_surface = font.render(text, True, "black")
    text_rect = text_surface.get_rect(center=(SW // 2, SH // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.update()

drawGrid()
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over and current_player == "X":
            mx, my = event.pos
            grid_x, grid_y = mx // BLOCK_SIZE, my // BLOCK_SIZE

            if board[grid_y][grid_x] == "":
                board[grid_y][grid_x] = "X"
                draw_symbol(grid_x, grid_y, "X")
                pygame.display.update()

                winner = check_winner()
                if winner:
                    winner_text = f"Wygrał: {winner}!" if winner != "Remis" else "Remis!"
                    game_over = True
                else:
                    current_player = "O"

    if current_player == "O" and not game_over:
        pygame.time.delay(500)
        move = best_move()
        if move:
            board[move[0]][move[1]] = "O"
            draw_symbol(move[1], move[0], "O")
            pygame.display.update()

            winner = check_winner()
            if winner:
                winner_text = f"Wygrał: {winner}!" if winner != "Remis" else "Remis!"
                game_over = True
            else:
                current_player = "X"

    if game_over:
        show_winner_screen(winner_text)
        pygame.time.delay(2000)
        board = [["" for _ in range(3)] for _ in range(3)]
        screen.fill("white")
        drawGrid()
        pygame.display.update()
        game_over = False
        current_player = "X"

    clock.tick(25)
