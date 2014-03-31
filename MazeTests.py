import unittest
from Maze import ChillMazeTile, ChillMaze


class TileTests(unittest.TestCase):
    def test_tile_instantiates(self):
        tile = ChillMazeTile()

    def test_all_walls_are_up_after_creation(self):
        tile = ChillMazeTile()
        self.assertTrue(tile.are_all_walls_up())

    def test_knocking_a_wall_causes_all_walls_check_to_be_false(self):
        tile = ChillMazeTile()
        tile.knock_wall("Bottom")
        self.assertFalse(tile.are_all_walls_up())

    def test_raising_a_wall_after_knocked_makes_all_walls_check_true(self):
        tile = ChillMazeTile()
        tile.knock_wall("Top")
        tile.raise_wall("Top")
        self.assertTrue(tile.are_all_walls_up())

    def test_knocking_non_existent_wall_raises_value_error(self):
        tile = ChillMazeTile()
        with self.assertRaises(ValueError):
            tile.knock_wall("Inexistent")


class MazeTests(unittest.TestCase):
    def test_maze_instantiates(self):
        maze = ChillMaze(3, 3)

    def test_error_for_non_numeric_initialization(self):
        with self.assertRaises(ValueError):
            ChillMaze("pizza", "is awesome")

    def test_error_for_negative_values_initialization(self):
        with self.assertRaises(ValueError):
            ChillMaze(-1, -3)
        with self.assertRaises(ValueError):
            ChillMaze(1, -3)
        with self.assertRaises(ValueError):
            ChillMaze(-1, 5)

    def test_maze_initializes_not_generated(self):
        maze = ChillMaze(3, 4)
        self.assertFalse(maze.has_been_generated())

    def test_maze_returns_correct_dimensions(self):
        intended_width = 3
        intended_height = 5
        maze = ChillMaze(3, 5)
        self.assertTrue(maze.getWidth() == intended_width)
        self.assertTrue(maze.getHeight() == intended_height)



def main():
    unittest.main()

if __name__ == '__main__':
    main()