def move_right(field, emergence='none', move_value=2):  # todo: add comments
    rownum = len(field)
    colnum = len(field[0])
    for i in range(rownum):
        for j in range(colnum - 2, -1, -1):
            if field[i][j] == move_value and field[i][j + 1] == 0:
                field[i][j + 1] = field[i][j]
                field[i][j] = 0
    return field


def move_down(field, emergence='none', move_value=1):  # todo: add comments, write emergence logic
    rownum = len(field)
    colnum = len(field[0])
    start_row = 2
    if emergence != 'none':
        start_row = 1
        idx_replacable = [el for el, x in enumerate(field[0]) if x == 0]
        idx_to_replace = [el for el, x in enumerate(field[rownum - 1]) if x == 1]
        replacable = list(set(idx_to_replace).intersection(set(idx_replacable)))  # fixme: circular filling
        field[0] = [el if x not in replacable else 1 for el, x in enumerate(field[0])]  # check me
    for i in range(rownum - start_row, -1, -1):
        for j in range(colnum):
            if field[i][j] == move_value and field[i + 1][j] == 0:
                field[i + 1][j] = field[i][j]
                field[i][j] = 0
    return field


def car_moves(field, emerge='none', move_right_value=2, move_down_value=1):  # todo: add comments
    field = move_right(field, emergence=emerge, move_value=move_right_value)
    field = move_down(field, emergence=emerge, move_value=move_down_value)
    return field

# todo: add move_up, move_left
