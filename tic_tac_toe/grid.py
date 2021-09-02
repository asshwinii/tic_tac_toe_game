import pygame
import os

letterx = pygame.image.load(os.path.join('IMG', 'letterx.png'))
lettero = pygame.image.load(os.path.join('IMG', 'lettero.png'))
class Grid:
    def __init__(self):
        self.grid_lines = [((0, 200), (600, 200)),   #first horizontal line
                           ((0, 400), (600, 400)),   #second horizontal line
                           ((200, 0), (200, 600)),   #first vertical line
                           ((400, 0), (400, 600))]   #second vertical line

        self.grid= [[0 for x in range(3)] for y in range(3)]
        self.game_over = False
        # search in direction N    NW        W         SW      S       SE      E      NE
        self.search_dir =[(0,-1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1,0), (1, -1)]
    def draw(self,surface):
        for line in self.grid_lines:
            pygame.draw.line(surface, (200, 200, 200), line[0], line[1], 2 )

        for y in range(len(self.grid)):
            for x in range(len(self.grid[y])):
                if self.get_cell_value(x, y) == 'X':
                    surface.blit(letterx, (x*200, y*200))
                elif self.get_cell_value(x,y)== 'O':
                    surface.blit(lettero, (x*200, y*200))


    def get_cell_value(self, x, y):
        return self.grid[y][x]

    def set_cell_value(self, x, y, value):
        self.grid[y][x]= value

    def get_mouse(self,x,y,player):

        if self.get_cell_value(x,y)== 0:
            if player == 'X':
                self.set_cell_value(x, y, 'X')
            elif player == 'O':
                self.set_cell_value(x, y, 'O')
            self.check_grid(x,y,player)

    def is_within_bound(self,x,y):
        return x>=0 and x<3 and y>=0 and y<3

    def check_grid(self,x,y,player):
        count = 1
        for index, (dirx , diry) in enumerate(self.search_dir):
            if self.is_within_bound(x+dirx, y+diry) and self.get_cell_value(x+dirx, y+diry) == player:
                count += 1
                xx = x+dirx
                yy = y+diry
                if self.is_within_bound(xx+dirx, yy+diry) and self.get_cell_value(xx+dirx, yy+diry) == player:
                    count += 1
                    if count == 3:
                        break
                if count < 3:
                    new_dir=0
                    # mapping the indices to opposite direction  : 0-4 ,1-5 ,2-6, 3-7, 4-0 , 5-1 , 6-2 , 7-3

                    if index == 0:
                        new_dir = self.search_dir[4]  # N to S
                    elif index == 1:
                        new_dir = self.search_dir[5]  # NW to SE
                    elif index == 2:
                        new_dir = self.search_dir[6]  # W to E
                    elif index == 3:
                        new_dir = self.search_dir[7]  # SW to NE
                    elif index == 4:
                        new_dir = self.search_dir[0]  # S to N
                    elif index == 5:
                        new_dir = self.search_dir[1]  # SE TO NW
                    elif index == 6:
                        new_dir = self.search_dir[2]  # W to E
                    elif index == 7:
                        new_dir = self.search_dir[3]  # NE to SW
                    if self.is_within_bound(x + new_dir[0], y + new_dir[1]) \
                            and self.get_cell_value(x + new_dir[0], y + new_dir[1]) == player:
                        count += 1
                        if count == 3:
                            break
                    else:
                        count = 1
        if count == 3:
            print(player,'wins')
            self.game_over = True
        else:
            self.game_over = self.full_grid()

    def clear_grid(self):
        for y in range(len(self.grid)):
            for x in range(len(self.grid)):
                if self.grid[y][x] != 0:
                    self.grid[y][x]=0
        self.game_over= False

    def full_grid(self):
        for row in self.grid:
            for value in row:
                if value ==0 :
                    return False
        return True

    def print_grid(self):
        for y in self.grid:
            print(y)