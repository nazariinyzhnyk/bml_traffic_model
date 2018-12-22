import time
import numpy as np
import matplotlib.pyplot as plt
import warnings
import argparse
from matplotlib.colors import ListedColormap
warnings.filterwarnings("ignore")
cmap = ListedColormap(['white', '#95d0fc', '#ff474c'])

parser = argparse.ArgumentParser(description='Initial conditions: ')
parser.add_argument("-f", "--field", help="field size", default='7')
parser.add_argument("-b", "--blues", help="blue cars ratio", default='0.3333')
parser.add_argument("-r", "--reds",  help="red cars ratio", default='0.3333')
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


if __name__ == '__main__':
    plt.ion()
    plt.figure()
    for i in range(2):
        plt.clf()
        print('iteration = ' + str(i))
        field = get_field(int(args.field), [float(args.blues), float(args.reds)])
        plt.matshow(field, fignum=1, cmap=cmap)
        plt.show()
        plt.pause(1)
