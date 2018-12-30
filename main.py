import time
import numpy as np
import matplotlib.pyplot as plt
import warnings
import argparse
from matplotlib.colors import ListedColormap
from moves import car_moves
warnings.filterwarnings("ignore")
cmap = ListedColormap(['white', '#95d0fc', '#ff474c'])

parser = argparse.ArgumentParser(description='Initial conditions: ')
parser.add_argument("-fcols", "--fieldcols", help="field size cols", default='9')
parser.add_argument("-frows", "--fieldrows", help="field size rows", default='9')
parser.add_argument("-b", "--blues", help="blue cars ratio", default='0.3333')  # todo: add param to pass only density
parser.add_argument("-r", "--reds",  help="red cars ratio", default='0.3333')
parser.add_argument("-i", "--iterations",  help="num of iterations", default='2')
parser.add_argument("-s", "--sleep",  help="sleep time", default='0.1')
args = parser.parse_args()


def get_field(field_size_cols, field_size_rows, class_relation):

    """ # todo write the function destination
    :param field_size_cols: # of matrix columns
    :param field_size_rows: # of matrix rows
    :param class_relation: relation of reds and blues (0:1)
    :return: field filled with random values white:0, blue:1, red:2
    """

    field_to_return = np.random.rand(field_size_cols, field_size_rows)
    field_to_return = np.where(field_to_return <= class_relation[0], 1,
                        np.where(field_to_return > sum(class_relation), 0, 2))
    return field_to_return


def plot_matrix(matrix, title_text, pause_time=1.0):  # todo: add comments
    plt.clf()
    plt.matshow(matrix, fignum=1, cmap=cmap)
    plt.title(title_text)
    plt.show()
    plt.pause(pause_time)


if __name__ == '__main__':  # todo: add comments
    plt.ion()
    plt.figure()
    field = get_field(int(args.fieldcols), int(args.fieldrows), [float(args.blues), float(args.reds)])
    plot_matrix(field, 'Initial matrix')
    prev_iter_field = field.copy()
    for i in range(int(args.iterations)):
        title_iter_num = str(i + 1)
        field = car_moves(field)
        if np.array_equal(np.array(field), np.array(prev_iter_field)):
            print('System stucked after ' + title_iter_num + ' iterations.')
            plot_matrix(field, 'Final iteration = ' + title_iter_num, pause_time=5.0)
            break
        elif i == int(args.iterations) - 1:
            print('All iterations passed.')
            plot_matrix(field, 'Final iteration = ' + title_iter_num, pause_time=5.0)
        else:
            plot_matrix(field, 'Iteration = ' + title_iter_num, pause_time=float(args.sleep))
            prev_iter_field = field.copy()
