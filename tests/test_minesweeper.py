import pytest

import src.minesweeper.minesweeper as minesweeper


def test_module_exists():
    assert minesweeper


def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    # TODO : Add assertions
    assert len(game.mines) == 2
