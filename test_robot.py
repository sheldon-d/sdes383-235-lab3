import pytest

from robot import Robot, Direction, IllegalMoveException


@pytest.fixture
def robot():
    return Robot()


def test_constructor(robot):
    state = robot.state()

    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_east_turn(robot):
    robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.EAST


def test_south_turn(robot):
    for i in range(2):
        robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.SOUTH


def test_west_turn(robot):
    for i in range(3):
        robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.WEST


def test_north_turn(robot):
    for i in range(4):
        robot.turn()

    state = robot.state()
    assert state['direction'] == Direction.NORTH


def test_illegal_move(robot):
    robot.turn()
    robot.turn()

    with pytest.raises(IllegalMoveException):
        robot.move()


def test_illegal_move_west(robot):
    for i in range(3):
        robot.turn()

    with pytest.raises(IllegalMoveException):
        robot.move()


def test_illegal_move_north(robot):
    for i in range(9):
        robot.move()

    with pytest.raises(IllegalMoveException):
        robot.move()


def test_illegal_move_east(robot):
    robot.turn()

    for i in range(9):
        robot.move()

    with pytest.raises(IllegalMoveException):
        robot.move()


def test_move_north(robot):
    robot.move()
    state = robot.state()
    assert state['row'] == 9
    assert state['col'] == 1


def test_move_east(robot):
    robot.turn()
    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 2


def test_move_south(robot):
    robot.move()

    for i in range(2):
        robot.turn()

    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 1


def test_move_west(robot):
    robot.turn()
    robot.move()

    for i in range(2):
        robot.turn()

    robot.move()
    state = robot.state()
    assert state['row'] == 10
    assert state['col'] == 1


def test_back_track_without_history(robot):
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_back_track_after_move(robot):
    robot.move()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_back_track_after_turn(robot):
    robot.turn()
    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1


def test_back_track_after_multiple(robot):
    for i in range(9):
        robot.move()

    robot.turn()

    for i in range(9):
        robot.move()

    robot.back_track()
    state = robot.state()
    assert state['direction'] == Direction.EAST
    assert state['row'] == 1
    assert state['col'] == 9


def test_back_track_all_moves(robot):
    for i in range(9):
        robot.move()

    robot.turn()

    for i in range(9):
        robot.move()

    for i in range(19):
        robot.back_track()

    state = robot.state()
    assert state['direction'] == Direction.NORTH
    assert state['row'] == 10
    assert state['col'] == 1
