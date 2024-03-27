from window import Window
from draw import Point, Line


class Cell:
    '''
        Takes two points and a window.
        `p1` represents the top left corner of the cell.
        `p2` represents the bottom right corner of the cell
        `window` is the window to draw the cell on
    '''

    def __init__(self, p1, p2, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = p1.x
        self._y1 = p1.y
        self._x2 = p2.x
        self._y2 = p2.y
        self.midpoint = Point((self._x1 + self._x2)//2, (self._y1+self._y2)//2)
        self._win: Window = window
        self.visited = False

    def draw(self):
        top_left = Point(self._x1, self._y1)
        top_right = Point(self._x2, self._y1)
        bottom_left = Point(self._x1, self._y2)
        bottom_right = Point(self._x2, self._y2)
        if self._win is not None:
            if self.has_left_wall:
                self._win.draw_line(Line(top_left, bottom_left), "black")
            else:
                self._win.draw_line(Line(top_left, bottom_left), "white")
            if self.has_right_wall:
                self._win.draw_line(Line(top_right, bottom_right), "black")
            else:
                self._win.draw_line(Line(top_right, bottom_right), "white")
            if self.has_top_wall:
                self._win.draw_line(Line(top_left, top_right), "black")
            else:
                self._win.draw_line(Line(top_left, top_right), "white")
            if self.has_bottom_wall:
                self._win.draw_line(Line(bottom_left, bottom_right), "black")
            else:
                self._win.draw_line(Line(bottom_left, bottom_right), "white")

    def draw_move(self, other, undo=False):
        line = None

        if self.midpoint.x != other.midpoint.x:
            line = Line(self.midpoint, Point(other.midpoint.x, self.midpoint.y))
        if self.midpoint.y != other.midpoint.y:
            line = Line(self.midpoint, Point(self.midpoint.x, other.midpoint.y))

        if line is None:
            return
        if self._win is not None:
            if not undo:
                self._win.draw_line(line, "red")
            else:
                self._win.draw_line(line, "gray")
