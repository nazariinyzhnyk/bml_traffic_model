

# def move_right(field, move_value=2):  # todo: add comments
#     rownum = len(field)
#     colnum = len(field[0])
#     for i in range(rownum):
#         for j in range(colnum - 2, -1, -1):
#             if field[i][j] == move_value and field[i][j + 1] == 0:
#                 field[i][j + 1] = field[i][j]
#                 field[i][j] = 0
#     return field
#
#
# def move_down(field, move_value=1):  # todo: add comments, write emergence logic
#     rownum = len(field)
#     colnum = len(field[0])
#     start_row = 2
#     idx_replacable = [el for el, x in enumerate(field[0]) if x == 0]
#     idx_to_replace = [el for el, x in enumerate(field[rownum - 1]) if x == 1]
#     replacable = list(set(idx_to_replace).intersection(set(idx_replacable)))  # fixme: circular filling
#     field[0] = [el if x not in replacable else 1 for x, el in enumerate(field[0])]  # check me
#     field[rownum - 1] = [el if x not in replacable else 0 for x, el in enumerate(field[rownum-1])]
#     for i in range(rownum - 2, -1, -1):
#         for j in range(colnum):
#             if field[i][j] == move_value and field[i + 1][j] == 0:
#                 field[i + 1][j] = field[i][j]
#                 field[i][j] = 0
#     return field

def move_loop(arr, range_from, range_to, move_value=2):
    for i in range(range_from, range_to, -1):
        if arr[i] == move_value and arr[i + 1] == 0:
            arr[i + 1] = arr[i]
            arr[i] = 0
    return arr


def circular_filling(vect, move_value=2):
    vect_len = len(vect)
    if vect[vect_len - 1] == move_value:
        if vect[0] == 0:
            vect[0] = move_value
            vect[vect_len - 1] = 0
            vect = move_loop(vect, vect_len - 2, 0, move_value=move_value)
        else:
            temp_vect = vect.copy()
            temp_vect[vect_len - 1] = 0
            temp_vect = move_loop(temp_vect, vect_len - 2, -1, move_value=move_value)
            if temp_vect[0] == 0:
                temp_vect[0] = move_value
                vect = temp_vect.copy()
            else:
                vect = move_loop(vect, vect_len - 2, -1, move_value=move_value)
    else:
        vect = move_loop(vect, vect_len - 2, -1, move_value=move_value)
    return vect


def move_right(field, move_value=2):
    for i in range(len(field)):
        field[i] = circular_filling(field[i], move_value=move_value)
    return field


def move_down(field, move_value=1):
    for i in range(len(field[0])):
        field[:, i] = circular_filling(field[:, i], move_value=move_value)
    return field


def car_moves(field, move_right_value=2, move_down_value=1):  # todo: add comments
    field = move_right(field, move_value=move_right_value)
    field = move_down(field, move_value=move_down_value)
    return field

# todo: add move_up, move_left
