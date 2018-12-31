import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import os
import datetime
cmap = ListedColormap(['white', '#95d0fc', '#ff474c'])


def get_field(field_size_cols, field_size_rows, class_relation):

    """
    Function to create field of given shape with randomly filled values of classes.
    :param field_size_cols: # of matrix columns
    :param field_size_rows: # of matrix rows
    :param class_relation: relation of reds and blues (0:1)
    :return: field filled with random values white:0, blue:1, red:2
    """

    field_to_return = np.random.rand(field_size_cols, field_size_rows)
    field_to_return = np.where(field_to_return <= class_relation[0], 1,
                        np.where(field_to_return > sum(class_relation), 0, 2))
    return field_to_return


def plot_matrix(matrix, title_text, pause_time=1.0, save_plots=0):
    """
    Function to plot matrix with colorizing different classes.
    :param matrix: matrix to plot
    :param title_text: plot title text
    :param pause_time: time (in secs) to sleep after each plot
    :param save_plots: whether or not save plot results to results folder
    """
    plt.clf()
    plt.matshow(matrix, fignum=1, cmap=cmap)
    plt.title(title_text)
    if save_plots:
        if not os.path.exists('results'):
            os.makedirs('results')
        plt.savefig('results/' + str(datetime.datetime.now())[:-7] + '.png')
    plt.show()
    plt.pause(pause_time)


def move_loop(arr, range_from, range_to, move_value=2):
    """
    Perform array moving
    :param arr: array to move
    :param range_from: range() from param
    :param range_to: range() to param
    :param move_value: class to move
    :return: moved array
    """
    for i in range(range_from, range_to, -1):
        if arr[i] == move_value and arr[i + 1] == 0:
            arr[i + 1] = arr[i]
            arr[i] = 0
    return arr


def circular_filling(vect, move_value=2):
    """
    :param vect: array to  move
    :param move_value: class to move
    :return: moved vect
    """
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
    """
    Function that calls move function to each row
    :param field: field to shift right
    :param move_value: class to move
    :return: moved right field
    """
    for i in range(len(field)):
        field[i] = circular_filling(field[i], move_value=move_value)
    return field


def move_down(field, move_value=1):
    """
    Function that calls move function to each col
    :param field: field to shift down
    :param move_value: class to move
    :return: moved down field
    """
    for i in range(len(field[0])):
        field[:, i] = circular_filling(field[:, i], move_value=move_value)
    return field


def car_moves(field, move_right_value=2, move_down_value=1):
    """
    Function that moves field right then down
    :param field: field to move
    :param move_right_value: class to move right
    :param move_down_value: class to move down
    :return: moved field
    """
    field = move_right(field, move_value=move_right_value)
    field = move_down(field, move_value=move_down_value)
    return field
