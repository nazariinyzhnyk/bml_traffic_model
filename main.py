import numpy as np
import matplotlib.pyplot as plt
import warnings
import argparse
from matplotlib.colors import ListedColormap
from moves import car_moves, get_field, plot_matrix
warnings.filterwarnings("ignore")
cmap = ListedColormap(['white', '#95d0fc', '#ff474c'])


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Initial conditions: ')
    parser.add_argument("-fcols", "--fieldcols", help="field size cols", default='9')
    parser.add_argument("-frows", "--fieldrows", help="field size rows", default='9')
    parser.add_argument("-d", "--density", help="density", default='0')
    parser.add_argument("-b", "--blues", help="blue cars ratio", default='0.3333')
    parser.add_argument("-r", "--reds", help="red cars ratio", default='0.3333')
    parser.add_argument("-i", "--iterations", help="num of iterations", default='2')
    parser.add_argument("-s", "--sleep", help="sleep time", default='0.1')
    parser.add_argument("-p", "--plot", help="save plot", default='0')
    args = parser.parse_args()

    if float(args.density) != 0:  # able to pass only density arg
        args.blues = '0.' + args.density
        args.reds = '0.' + args.density

    plt.ion()
    plt.figure()
    field = get_field(int(args.fieldcols), int(args.fieldrows), [float(args.blues), float(args.reds)])
    plot_matrix(field, 'Initial matrix', save_plots=int(args.plot))
    prev_iter_field = field.copy()
    for i in range(int(args.iterations)):
        title_iter_num = str(i + 1)
        field = car_moves(field)  # move right then down
        if np.array_equal(np.array(field), np.array(prev_iter_field)):  # check if matrix changed
            print('System stucked after ' + title_iter_num + ' iterations.')
            plot_matrix(field, 'Final iteration = ' + title_iter_num,
                        pause_time=5.0, save_plots=int(args.plot))
            break  # if matrix didn't changed: stop - system stucked
        elif i == int(args.iterations) - 1:  # check for the last iteration
            print('All iterations passed.')
            plot_matrix(field, 'Final iteration = ' + title_iter_num,
                        pause_time=5.0, save_plots=int(args.plot))  # if yes: save plot
        else:
            plot_matrix(field, 'Iteration = ' + title_iter_num, pause_time=float(args.sleep))
            prev_iter_field = field.copy()
