#!/usr/bin/python3.11

from snake import SnakeGame

def test_1():
    game = SnakeGame(2,2,[[0,1]])
    assert game.move('R') == 1
    assert game.move('D') == 1

def test_2():
    game = SnakeGame(3,2,[[1,2],[0,1]])
    # ["R"],["D"],["R"],["U"],["L"],["U"]
    # 0,0,1,1,2,-1
    assert game.move('R') == 0
    assert game.move('D') == 0
    assert game.move('R') == 1
    assert game.move('U') == 1
    assert game.move('L') == 2
    assert game.move('U') == -1