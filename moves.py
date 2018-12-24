def move_right(field, move_value=2):
    rownum = len(field)
    colnum = len(field[1])
    for i in range(rownum):
        for j in range(colnum - 2, -1, -1):
            if field[i][j] == move_value and field[i][j + 1] == 0:
                field[i][j + 1] = field[i][j]
                field[i][j] = 0
    return field


def move_down(field, move_value=1):
    rownum = len(field)
    colnum = len(field[1])
    for i in range(rownum - 2, -1, -1):
        for j in range(colnum):
            if field[i][j] == move_value and field[i + 1][j] == 0:
                field[i + 1][j] = field[i][j]
                field[i][j] = 0
    return field


def car_moves(field, move_right_value=2, move_down_value=1):
    field = move_right(field, move_value=move_right_value)
    field = move_down(field, move_value=move_down_value)
    return field

# todo: add move_up, move_left
