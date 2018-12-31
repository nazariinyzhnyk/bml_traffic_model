import numpy as np
import matplotlib.pyplot as plt
import warnings
import argparse
from matplotlib.colors import ListedColormap
from moves import car_moves, get_field, plot_matrix
warnings.filterwarnings("ignore")
cmap = ListedColormap(['white', '#95d0fc', '#ff474c'])

parser = argparse.ArgumentParser(description='Initial conditions: ')
parser.add_argument("-fcols", "--fieldcols", help="field size cols", default='9')
parser.add_argument("-frows", "--fieldrows", help="field size rows", default='9')
parser.add_argument("-d", "--density", help="density", default='0')
parser.add_argument("-b", "--blues", help="blue cars ratio", default='0.3333')
parser.add_argument("-r", "--reds",  help="red cars ratio", default='0.3333')
parser.add_argument("-i", "--iterations",  help="num of iterations", default='2')
parser.add_argument("-s", "--sleep",  help="sleep time", default='0.1')
args = parser.parse_args()

if float(args.density) != 0:
    args.blues = '0.' + args.density
    args.reds = '0.' + args.density


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
