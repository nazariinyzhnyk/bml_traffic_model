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
parser.add_argument("-f", "--field", help="field size", default='7')
parser.add_argument("-b", "--blues", help="blue cars ratio", default='0.3333')
parser.add_argument("-r", "--reds",  help="red cars ratio", default='0.3333')
parser.add_argument("-i", "--iterations",  help="num of iterations", default='2')
args = parser.parse_args()


def get_field(field_size, class_relation):

    """
    :param field_size: square matrix nrows/ncols
    :param class_relation: relation of reds and blues (0:1)
    :return: field filled with random values white:0, blue:1, red:2
    """

    field_to_return = np.random.rand(field_size, field_size)
    field_to_return = np.where(field_to_return <= class_relation[0], 1,
                      np.where(field_to_return > sum(class_relation), 0, 2))
    return field_to_return


def plot_matrix(matrix, title_text, pause_time=1):
    plt.clf()
    plt.matshow(matrix, fignum=1, cmap=cmap)
    plt.title(title_text)
    plt.show()
    plt.pause(pause_time)


if __name__ == '__main__':
    plt.ion()
    plt.figure()
    field = get_field(int(args.field), [float(args.blues), float(args.reds)])
    plot_matrix(field, 'Initial matrix')
    prev_iter_field = field.copy()
    for i in range(int(args.iterations)):
        title_iter_num = str(i + 1)
        field = car_moves(field)
        if np.array_equal(np.array(field), np.array(prev_iter_field)):
            print('System stucked after ' + title_iter_num + ' iterations.')
            plot_matrix(field, 'Final iteration = ' + title_iter_num, pause_time=5)
            break
        else:
            plot_matrix(field, 'Iteration = ' + title_iter_num)
            prev_iter_field = field.copy()
