from maze_abstract_base import MazeAbstractBase
from chill_tile import ChillTile


class ChillMaze(MazeAbstractBase):

    def __init__(self, width, height, tile_class=ChillTile):
        """Initialization logic for the maze
            Params:
                width: numeric value for the grid width of the maze
                height: numeric value for the gird height of the maze
            Raises:
                ValueError: If width or height cannot be numerically
                            interpreted and are not greater than zero
        """
        super().__init__(width, height, tile_class)
        try:
            width = int(width)
            height = int(height)

            if width < 1 or height < 1:
                raise ValueError

        except (TypeError, ValueError):
            raise ValueError("Width and Height must be greater than zero:"
                             "{},{} provided".format(width, height))

        # Initialize data
        self._width = width
        self._height = height
        self._maze = []
        self._tile_class = tile_class

        # Time to actually initialize the tiles
        # Lets go through each row
        for row_number in range(height):
            # Then create all columns
            column = []
            for column_number in range(width):
                tile = self._tile_class()
                column.append(tile)
            self._maze.append(column)

        # Sanity check
        if (len(self._maze) != self.get_height() or
                len(self._maze[0]) != self.get_width()):
                    raise AssertionError("Dimensions are not matching up!\n"
                                         "Actual Width: {actual_width}\n"
                                         "Actual Height: {actual_height}\n"
                                         "Intended Width: {intended_width}\n"
                                         "Intended Height: {intended_height}\n"
                                         .format(
                                         actual_width=len(self._maze[0]),
                                         actual_height=len(self._maze),
                                         intended_width=width,
                                         intended_height=height
                                         ))

    def has_been_generated(self):
        """Determine whether or not this maze has been generated and has tiles
            Returns: bool
        """
        if len(self._maze) > 0 and len(self._maze[0]) > 0:
            return True
        else:
            return False

    def get_width(self):
        """Get the width of this maze
            Return: Numeric value of the width
        """
        return self._width

    def get_height(self):
        """Get the height of this maze
            Return: Numeric value of the height
        """
        return self._height

    def get_tiles_in_row(self, index):
        """Return all tiles on a specific row (horizontal dimension)
            Params:
                index: integer
            Returns:
                List of tiles
            Raises:
                IndexError: If supplied index is invalid
        """
        try:
            tiles = self._maze[index]
            return tiles
        except IndexError:
            raise IndexError("Invalid value, {} not a valid index for a row"
                             .format(index))

    def get_tiles_in_column(self, index):
        """Return all tiles from a specific column (vertical dimension)
            Params:
                index integer
            Returns:
                List of tiles
            Raises:
                IndexError: If supplied index is invalid
        """
        try:
            tiles = []
            for row in self._maze:
                tiles.append(row[index])
            return tiles
        except IndexError:
            raise IndexError("Invalid value, {} not a valid index for a column"
                             .format(index))

    def get_tile_at(self, horizontal_index, vertical_index):
        """Return the tile at a specific location
            Params:
                horizontal_index numeric index for the horizontal axis
                vertical_index numeric index for the vertical axis
            Returns:
                A tile
            Raises:
                Index error if any of the provided indexes is not valid
        """
        row = self.get_tiles_in_row(vertical_index)
        try:
            row[horizontal_index]
        except IndexError:
            raise IndexError("Invalid position: {horizontal},{vertical}"
                             .format(horizontal=horizontal_index,
                                     vertical=vertical_index))