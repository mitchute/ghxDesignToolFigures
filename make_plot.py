import matplotlib.pyplot as plt
import numpy as np


def plot(args):

    #unit conversion
    c = [9./5., 11.53808]

    # split in to separate files
    args = args.split(",")

    save_name = args[0]

    args.pop(0)

    # names
    names = []
    for name in args:
        temp = name.split("_")
        string = ""
        for t in temp:
            string += t + " "
        names.append(string.strip())

    # get data from files
    all_data = []
    for arg in args:
        file_name = arg.strip() + ".csv"
        data = np.genfromtxt(file_name, delimiter=",", unpack=True, dtype=float)
        all_data.append([data[0], data[1]])

    # calculate percent error
    percent_error = []
    for data in all_data[1:]:
        interp_data = np.interp(data[0], all_data[0][0], all_data[0][1])
        error = ((data[1] - interp_data) / interp_data) * 100.0
        percent_error.append([data[0], error])

    # make plot
    f, axarr = plt.subplots(2, sharex=True, gridspec_kw={'height_ratios':[2,1]})

    # line style
    lines = ['-', '--', '-.', ':']

    # colors
    colors = ['k', 'b', 'r', 'g']

    # plot m/kW vs. approach temp
    i = 0
    for data in all_data:
        axarr[0].plot(data[0], data[1], color=colors[i], ls=lines[i], lw=2.0)
        i += 1

    # add legend to plot
    axarr[0].legend(names)

    # set axis limits
    axarr[0].set_xlim([1, 6])

    # add secondary axes
    ax3 = axarr[0].twinx()
    ax4 = axarr[0].twiny()

    ax3.set_ylabel("ft/ton")
    ax4.set_xlabel(r"Approach Temp. $(^\circ F)$ [Coil Exit Temp. - Lake Temp.]")

    new_x_limits = [axarr[0].get_xlim()[0], axarr[0].get_xlim()[1]]
    new_x_limits = [x * c[0] for x in new_x_limits]
    ax4.set_xlim(new_x_limits)

    new_x_ticks = axarr[0].xaxis.get_ticklocs()
    new_x_ticks = [x * c[0] for x in new_x_ticks]
    ax4.set_xticks(new_x_ticks)

    new_y_limits = [axarr[0].get_ylim()[0], axarr[0].get_ylim()[1]]
    new_y_limits = [x * c[1] for x in new_y_limits]
    ax3.set_ylim(new_y_limits)

    new_y_ticks = axarr[0].yaxis.get_ticklocs()
    new_y_ticks = [x * c[1] for x in new_y_ticks]
    ax3.set_yticks(new_y_ticks)

    # plot percent diff. vs. approach temp
    i = 1
    for data in percent_error:
        axarr[1].plot(data[0], data[1], color=colors[i], ls=lines[i], lw=2.0)
        i += 1

    # set labels
    axarr[0].set_ylabel("m/kW")
    axarr[1].set_xlabel(r"Approach Temp. Difference $(^\circ C)$ [Coil Exit Temp. - Lake Temp.]")
    axarr[1].set_ylabel("% Difference from \"Typical\"")

    # grid lines
    axarr[0].grid(b=True, which='major', color='b')
    axarr[1].grid(b=True, which='major', color='b')

    plt.subplots_adjust(hspace=0.1)

    # save figure
    plt.savefig(save_name + ".pdf", bbox_inches='tight')
    #plt.show()


