from draw import Point
from cell import Cell
from time import sleep
import random


class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_width, cell_height, win=None, seed=None):
        if seed is not None:
            random.seed(seed)
        self._x1 = x1
        self._y1 = y1
        self._rows = num_rows
        self._cols = num_cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._win = win
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = []
        for i in range(0, self._cols):
            row = []
            for j in range(0, self._rows):
                cell_p1 = Point(self._cell_width * i + self._x1, self._cell_height * j + self._y1)
                cell_p2 = Point(cell_p1.x + self._cell_width, cell_p1.y + self._cell_height)
                row.append(Cell(cell_p1, cell_p2, self._win))
            self._cells.append(row)
        for i in range(0, self._cols):
            for j in range(0, self._rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if self._win is not None:
            self._cells[i][j].draw()
            self._animate(0.05)

    def _animate(self, speed):
        self._win.redraw()
        sleep(speed)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()
        self._cells[-1][-1].has_bottom_wall = False
        self._cells[-1][-1].draw()

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        i_to_visit = i
        j_to_visit = j
        while True:
            to_visit = [None, None, None, None]
            if i > 0:
                to_visit[0] = self._cells[i-1][j]
            if i < self._cols - 1:
                to_visit[2] = self._cells[i+1][j]
            if j > 0:
                to_visit[1] = self._cells[i][j-1]
            if j < self._rows - 1:
                to_visit[3] = self._cells[i][j+1]
            for n in range(0, 4):
                if to_visit[n] is not None and to_visit[n].visited:
                    to_visit[n] = None
            if to_visit == [None, None, None, None]:
                self._cells[i][j].draw()
                return
            dir = random.randrange(0, 4)
            while to_visit[dir] is None:
                dir = random.randrange(0, 4)

            i_to_visit, j_to_visit = self._remove_walls_and_move(dir, i, j, to_visit)
            self._break_walls_r(i_to_visit, j_to_visit)

    def _remove_walls_and_move(self, dir, i, j, to_visit):
        i_to_visit, j_to_visit = i, j
        if dir == 0:
            self._cells[i][j].has_left_wall = False
            to_visit[dir].has_right_wall = False
            i_to_visit = i-1
        elif dir == 1:
            self._cells[i][j].has_top_wall = False
            to_visit[dir].has_bottom_wall = False
            j_to_visit = j-1
        elif dir == 2:
            self._cells[i][j].has_right_wall = False
            to_visit[dir].has_left_wall = False
            i_to_visit = i+1
        elif dir == 3:
            self._cells[i][j].has_bottom_wall = False
            to_visit[dir].has_top_wall = False
            j_to_visit = j+1
        return i_to_visit, j_to_visit

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)

    def _solve_r(self, i, j):
        self._animate(0.05)
        self._cells[i][j].visited = True
        cur_cell = self._cells[i][j]
        if cur_cell == self._cells[-1][-1]:
            return True
        if i > 0:
            if not cur_cell.has_left_wall and not self._cells[i-1][j].visited:
                cur_cell.draw_move(self._cells[i-1][j])
                if self._solve_r(i-1, j):
                    return True
                self._cells[i-1][j].draw_move(cur_cell, undo=True)
                self._animate(0.1)
        if i < self._cols:
            if not cur_cell.has_right_wall and not self._cells[i+1][j].visited:
                cur_cell.draw_move(self._cells[i+1][j])
                if self._solve_r(i+1, j):
                    return True
                self._cells[i+1][j].draw_move(cur_cell, undo=True)
                self._animate(0.1)
        if j > 0:
            if not cur_cell.has_top_wall and not self._cells[i][j-1].visited:
                cur_cell.draw_move(self._cells[i][j-1])
                if self._solve_r(i, j-1):
                    return True
                self._cells[i][j-1].draw_move(cur_cell, undo=True)
                self._animate(0.1)
        if j < self._rows:
            if not cur_cell.has_bottom_wall and not self._cells[i][j+1].visited:
                cur_cell.draw_move(self._cells[i][j+1])
                if self._solve_r(i, j+1):
                    return True
                self._cells[i][j+1].draw_move(cur_cell, undo=True)
                self._animate(0.1)
        return False
