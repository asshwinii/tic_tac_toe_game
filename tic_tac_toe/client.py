import pygame

from grid import Grid
surface = pygame.display.set_mode((600, 600))
pygame.display.set_caption('Tic-Tac-Toe-client')

import threading


def create_thread(target):
    thread = threading.Thread(target= target)
    thread.demon = True
    thread.start()


import socket

HOST = '127.0.0.1'
PORT = 65432

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))


def receive_data():
    global turn
    while True:
        data = sock.recv(1024).decode()    # recv function is a blocking function that is why we created a new thread
        data = data.split('-')
        x, y = int(data[0]), int(data[1])

        if data[2] == 'yourturn':
            turn = True
        if data[3] == 'False':
            grid.game_over = True
        if grid.get_cell_value(x, y) == 0:
            grid.set_cell_value(x, y, 'X')
        print(data)


create_thread(receive_data)
grid = Grid()

running = True
player = 'O'
turn = False
playing = 'True'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:
            if pygame.mouse.get_pressed()[0]:
                if turn and not grid.game_over:
                    pos = pygame.mouse.get_pos()
                    cellx, celly = pos[0] // 200, pos[1] // 200
                    if grid.get_cell_value(pos[0] // 200, pos[1] // 200) == 0:
                        grid.get_mouse(cellx, celly, player)
                        if grid.game_over:
                            playing ='False'
                        send_data = '{}-{}-{}-{}'.format(cellx, celly, 'yourturn', playing).encode()
                        sock.send(send_data)
                        turn = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
                playing = 'True'
            elif event.key == pygame.K_ESCAPE:
                running = False

    surface.fill((0, 0, 0))
    grid.draw(surface)
    pygame.display.flip()