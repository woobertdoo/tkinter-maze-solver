import unittest
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1._cells), num_cols)
        self.assertEqual(len(m1._cells[0]), num_rows)
        num_cols = 15
        num_rows = 12
        m2 = Maze(0, 0, num_rows, num_cols, 14, 14)
        self.assertEqual(len(m2._cells), num_cols)
        self.assertEqual(len(m2._cells[0]), num_rows)

    def test_maze_break_entrance_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(m1._cells[0][0].has_top_wall, False)
        self.assertEqual(m1._cells[-1][-1].has_bottom_wall, False)
        num_cols = 15
        num_rows = 12
        m2 = Maze(0, 0, num_rows, num_cols, 14, 14)
        self.assertEqual(m2._cells[0][0].has_top_wall, False)
        self.assertEqual(m2._cells[-1][-1].has_bottom_wall, False)

    def test_maze_reset(self):
        num_rows = 15
        num_cols = 15
        m = Maze(0, 0, num_rows, num_cols, 10, 10)
        for i in range(0, num_cols):
            for j in range(0, num_rows):
                self.assertEqual(m._cells[i][j].visited, False, f"Cell as ({i},{j}) not reset")


if __name__ == "__main__":
    unittest.main()
