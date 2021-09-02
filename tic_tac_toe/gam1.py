import pygame

from grid import Grid
surface = pygame.display.set_mode((600,600))
pygame.display.set_caption('Tic-Tac-Toe')

grid = Grid()
#grid.set_cell_value(0,0,'X')
#grid.print_grid()

running = True
player ='X'
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not grid.game_over:
            if pygame.mouse.get_pressed()[0]:
                pos= pygame.mouse.get_pos()
                print(pos[0]//200, pos[1]//200)
                if grid.get_cell_value(pos[0]//200,pos[1]//200) ==0:
                    grid.get_mouse(pos[0] // 200, pos[1] // 200, player)
                    if player == 'X':
                        player = 'O'
                    elif player == 'O':
                        player = 'X'

                grid.print_grid()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and grid.game_over:
                grid.clear_grid()
            elif event.key == pygame.K_ESCAPE:
                running = False

    surface.fill((0, 0, 0))
    grid.draw(surface)
    pygame.display.flip()