from defs import *

from sfml import *

NONE = Color.TRANSPARENT
WHITE = Color.WHITE
BLACK = Color.BLACK

board_grid = None
circles = None
chesses = {}

offest_x = 0
offest_y = 0

def prepare_board(_offest_x = 0, _offest_y = 0):
    global board_grid
    global circles

    global offest_x
    global offest_y
    offest_x = _offest_x
    offest_y = _offest_y

    board_grid = VertexArray(PrimitiveType.LINES)
    for i in range(0, 19):
        board_grid.append(
            Vertex(Vector2(
                    offest_x + BLOCK_RADIUS + i * 2 * BLOCK_RADIUS, 
                    offest_y + BLOCK_RADIUS
                ), Color.BLACK
            )
        )

        board_grid.append(
            Vertex(Vector2(
                    offest_x + BLOCK_RADIUS + i * 2 * BLOCK_RADIUS,
                    offest_y + BLOCK_RADIUS + 36 * BLOCK_RADIUS
                ), Color.BLACK
            )
        )

        board_grid.append(
            Vertex(Vector2(
                    offest_x + BLOCK_RADIUS,
                    offest_y + BLOCK_RADIUS + i * 2 * BLOCK_RADIUS
                ), Color.BLACK
            )
        )

        board_grid.append(
            Vertex(Vector2(
                    offest_x + BLOCK_RADIUS + 36 * BLOCK_RADIUS,
                    offest_y + BLOCK_RADIUS + i * 2 * BLOCK_RADIUS
                ), Color.BLACK
            )
        )

    circles = []

    POSITIONS = [
        (3, 3), (3, 9), (3, 15),
        (9, 3), (9, 9), (9, 15),
        (15, 3), (15, 9), (15, 15)
    ]

    for point in POSITIONS:
        x, y = point

        circle = CircleShape()
        circle.radius = POINT_RADIUS
        circle.fill_color = Color.BLACK
        circle.position = (
            offest_x + BLOCK_RADIUS * 2 * x + BLOCK_RADIUS - POINT_RADIUS,
            offest_y + BLOCK_RADIUS * 2 * y + BLOCK_RADIUS - POINT_RADIUS
        )

        circles.append(circle)

def set_chess(x, y, color):
    global chesses
    global offest_x
    global offest_y

    chess = CircleShape()
    chess.radius = CHESS_RADIUS
    chess.position = (
        offest_x + (2 * x - 1) * BLOCK_RADIUS - CHESS_RADIUS,
        offest_y + (2 * y - 1) * BLOCK_RADIUS - CHESS_RADIUS
    )
    chess.fill_color = color

    chesses[(x, y)] = chess

def to_index(px, py):
    return (int(px / (2 * BLOCK_RADIUS)) + 1, int(py / (2 * BLOCK_RADIUS)) + 1)

def render_board(window):
    global board_grid
    global circles

    window.draw(board_grid)

    for circle in circles:
        window.draw(circle)

    for chess in chesses.values():
        window.draw(chess)
