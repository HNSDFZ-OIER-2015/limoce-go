from sfml import *

INVALID_X = -1000
INVALID_Y = -1000

OFFEST_X = 200
OFFEST_Y = 0

WINDOW_WIDTH = 760 + OFFEST_X
WINDOW_HEIGHT = 760 + OFFEST_Y
WINDOW_TITLE = "Go Game"
WINDOW_STYLE = window.Style.TITLEBAR | window.Style.CLOSE
WINDOW_ANTIALIAS = 0
WINDOW_BACKGROUND_COLOR = Color(205, 154, 61)

BLOCK_RADIUS = 20
CHESS_RADIUS = 18
POINT_RADIUS = 4

CURRENT_SELECT_COLOR = Color(125, 125, 125, 150)

CURRENT_CHESS_X = 30
CURRENT_CHESS_Y = 30
CURRENT_CHESS_RADIUS = 75

CIRCLE_POINTS_NUMBER = 64

FONT = "consolas.ttf"

HISTORY_TEXT_SIZE = 20
HISTORY_TEXT_X = 30
HISTORY_TEXT_Y = 230
HISTORY_TEXT_COLOR = Color.BLACK
HISTORY_TEXT_MAX_LINES = 22
