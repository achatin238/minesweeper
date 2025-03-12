import pytest

import src.minesweeper.minesweeper as minesweeper


def test_module_exists():
    assert minesweeper


def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    assert len(game.mines) == 2
    mine_count = sum(row.count("💣") for row in game.get_board())
    assert mine_count == 2


def test_reveal():
    import random

    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    result = game.reveal(2, 2)
    assert result == "Continue"
    assert (2, 2) in game.revealed


def test_reveal_mine():
    import random

    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    for mine in game.mines:
        result = game.reveal(*mine)
        assert result == "Game Over"


def test_is_winner():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.revealed = set(
        (r, c) for r in range(3) for c in range(3) if (r, c) not in game.mines
    )
    assert game.is_winner()


def test_restart():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.reveal(0, 0)
    game.restart()
    assert len(game.revealed) == 0
    assert len(game.mines) == 2
