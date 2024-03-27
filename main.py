from window import Window
from maze import Maze


def main():

    win = Window(800, 600)
    Maze(150, 150, 8, 8, 50, 50, win).solve()
    win.wait_for_close()


main()
