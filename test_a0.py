"""CSC148 Assignment 0

=== CSC148 Winter 2024 ===
Department of Computer Science,
University of Toronto

This code is provided solely for the personal and private use of
students taking the CSC148 course at the University of Toronto.
Copying for purposes other than this use is expressly prohibited.
All forms of distribution of this code, whether as given or with
any changes, are expressly prohibited.

Author: Jonathan Calver and Sophia Huynh

All of the files in this directory and all subdirectories are:
Copyright (c) Jonathan Calver, Diane Horton, and Sophia Huynh.

=== Module Description ===

This file contains some provided tests for the assignment and is where
you will write additional tests.

To run the tests in this file, right-click here and select the option
that says "Run 'Python tests in test...'"

Note: We will not run pyTA on this file when grading your assignment.

"""
from __future__ import annotations

from four_in_a_row import *
from a0 import *


# TODO add tests for each method and function as indicated in the assignment
#      Note: we have scaffolded some code below for you to add your tests into.
#      Make sure each test has a unique name and that each test starts
#      with test_
#      The tests below are organized into classes to help keep related tests
#      grouped together. In PyCharm you can choose to run all tests in a single
#      class by using the run button beside the class name (just like how you
#      can choose to run a single test). Alternatively, you can run all tests
#      in the file by right-clicking the file name and choosing to run tests.


class TestHelpers:
    """
    These are provided tests related to Task 1, which are meant to remind you
    of the structure of a pytest for later tasks. For Task 1, you are asked
    to write doctests instead.

    While not required, you are welcome to add other pytests here as you
    develop your code.
    """

    def test_within_grid_in_grid(self):
        """Test that (0, 0) is inside a 4-by-4 grid."""
        assert within_grid((0, 0), 4)

    def test_within_grid_outside_grid(self):
        """Test that (4, 4) is outside a 4-by-4 grid."""
        assert not within_grid((4, 4), 4)

    def test_all_within_grid_all_in_grid(self):
        """Test when the four coordinates are all within a 4-by-4 grid."""
        assert all_within_grid([(0, 0), (1, 1), (2, 2), (3, 3)], 4)

    def test_reflect_vertically_above(self):
        """Test reflecting vertically for a coordinate above the middle."""
        assert reflect_vertically((0, 1), 5) == (4, 1)

    def test_reflect_vertically_middle(self):
        """Test reflecting vertically for a coordinate on the middle row."""
        assert reflect_vertically((2, 1), 5) == (2, 1)

    def test_reflect_points(self):
        """Test reflecting a very short line"""
        assert reflect_points([(0, 1), (1, 2)], 5) == [(4, 1), (3, 2)]


class TestLine:
    """
    TODO Task 2: add tests for the Line methods and related functions
                 You must write two tests for each of:
                   - is_row, is_column, and is_diagonal
                   - Line.drop, Line.is_full, and Line.has_fiar
    """

    def test_is_a_row(self) -> None:
        l = [Square((0, 2)), Square((0, 3)), Square((0, 4)), Square((0, 5))]
        assert is_row(l) == True

    def test_is_not_a_row(self) -> None:
        not_l = [Square((0, 1)), Square((0, 2)), Square((0, 4)), Square((0, 3))]
        assert is_row(not_l) is False

    def test_is_a_column(self) -> None:
        l = [Square((0, 1)), Square((1, 1)), Square((2, 1)), Square((3, 1))]
        assert is_column(l) is True

    def test_not_a_column(self) -> None:
        not_l = [Square((0, 1)), Square((1, 1)), Square((3, 1)), Square((2, 1))]
        assert is_column(not_l) is False

    def test_is_diagonal(self) -> None:
        l = [Square((0, 0)), Square((1, 1)), Square((2, 2)), Square((3, 3))]
        assert is_diagonal(l) is True

    def test_is_diagonal(self) -> None:
        l2 = [Square((1, 1)), Square((2, 2)), Square((3, 3)), Square((4, 4))]
        assert is_diagonal(l2) is True

    def test_is_not_diagonal(self) -> None:
        l3 = [Square((5, 4)), Square((3, 3)), Square((2, 2)), Square((1, 1))]
        assert is_diagonal(l3) is False

    def test_is_not_diagonal(self) -> None:
        not_l = [Square((0, 0)), Square((1, 1)), Square((3, 3)), Square((2, 2))]
        assert is_diagonal(not_l) is False

    def test_drop_return_row_coord(self) -> None:
        l = Line([Square((0, 0)), Square((1, 0)), Square((2, 0)), Square((3, 0))])
        assert l.drop('X') == 3

    def test_drop_replace_symbol(self) -> None:
        l = Line([Square((0, 0)), Square((1, 0)), Square((2, 0)), Square((3, 0))])
        row_coord = l.drop('X')
        assert l[row_coord].symbol is 'X'

    def test_empty_is_full(self) -> None:
        empty_line = Line([Square((0, 1)), Square((1, 1)), Square((2, 1)), Square((3, 1))])
        assert empty_line.is_full() is False

    def test_full_is_full(self) -> None:
        full_line = Line(
            [Square((0, 1), 'X'), Square((1, 1), 'X'), Square((2, 1), 'X'), Square((3, 1), 'X')]
        )
        assert full_line.is_full() is True

    def test_has_fiar_no_symbol(self) -> None:
        line = Line([Square((0, 1)), Square((0, 2)), Square((0, 3)), Square((0, 4))])
        assert line.has_fiar((0, 2)) is False

    def test_has_fiar_contain_coord(self) -> None:
        line = Line(
            [
                Square((0, 1), 'X'),
                Square((0, 2), 'X'),
                Square((0, 3), 'X'),
                Square((0, 4), 'X'),
                Square((0, 5), 'X'),
            ]
        )
        assert line.has_fiar((0, 2)) is True

    def test_drop_first(self) -> None:
        l = Line([Square((0, 0)), Square((1, 0)),
                  Square((2, 0)), Square((3, 0))])
        row_coord = l.drop('X')
        assert row_coord == 3

    def test_drop_last(self) -> None:
        l = Line([Square((0, 0)), Square((1, 0),'O'),
                  Square((2, 0),'X'), Square((3, 0),'O')])
        row_coord = l.drop('X')
        assert row_coord is 0

class TestGrid:
    """
    TODO Task 3.1: add tests for the Grid methods and related functions
                 You must write two tests for each of:
                   - Grid.drop, Grid.is_full
                   - create_rows_and_columns

    TODO Task 3.2: add tests for the Grid methods and related functions
                 You must write two tests for each of:
                   - Grid.has_fiar
                   - create_mapping
    """
    def test_grid_drop(self) -> None:
        g = Grid(4)
        assert g.drop(1, 'X')  == 3

    def test_grid_drop_multiple(self) -> None:
        g = Grid(5)
        assert g.drop(3, 'X') == 4
        assert g.drop(3, 'X')  == 3
        assert g.drop(1, 'O')  == 4
        assert g.drop(1, 'X')  == 3

    def test_grid_no_fiar(self) -> None:
        g = Grid(4)
        assert g.has_fiar((0, 0)) is False

    def test_grid_has_fiar(self) -> None:
        g = Grid(4)
        for _ in range(4):  # make a four-in-a-row
            _ = g.drop(0, 'X')
        assert g.has_fiar((0, 0)) is True

    def test_create_rows_and_columns_alias(self):
        squares = create_squares(4)
        rows, columns = create_rows_and_columns(squares)
        assert rows[0][2] is columns[2][0]

    def test_create_rows_and_columns_alias2(self):
        squares = create_squares(4)
        rows, columns = create_rows_and_columns(squares)
        assert rows[0][2] is squares[0][2]

    def test_is_not_full(self) -> None:
        g = Grid(4)
        assert g.is_full() is False

    def test_is_full(self) -> None:
        g = Grid(4)
        for c in range(4):  # fill the grid and check again
            for r in range(4):
                g.drop(c, 'X')
        assert g.is_full() is True

    def test_create_mapping_length(self) -> None:
        squares = create_squares(6)
        mapping = create_mapping(squares)
        lines = mapping[(2,0)]
        assert len(lines) == 3

    def test_create_mapping_diagonal(self) -> None:
        squares = create_squares(6)
        mapping = create_mapping(squares)
        lines = mapping[(2,0)]
        assert is_diagonal(lines[2].cells) is True



class TestFourInARow:
    """
    TODO TASK 4:
     - run check_coverage.py to get the code coverage report.
     - Using the code coverage report, identify which branches of the code
       are not currently being tested.
     - add tests below in order to achieve 100% code coverage when you run
       check_coverage.py. Your tests should follow a similar structure
       to the test_x_wins test defined below.
    """

    def test_x_wins(self) -> None:
        """
        Provided test demonstrating how you can test FourInARow.play using
        a StringIO object to "script" the input.

        See both the handout and the Task 4 section of the supplemental slides
        for a detailed explanation of this example.
        """
        fiar = play_game(GAME_SCRIPT_X_WINS)

        assert fiar.result == WIN

    # TODO Add your tests for Task 4 here. Make sure each test has a unique name
    #      and that each test starts with test_


if __name__ == '__main__':
    import pytest

    pytest.main(['test_a0.py'])

