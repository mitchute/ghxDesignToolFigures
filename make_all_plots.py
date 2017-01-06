import sys
import os
import make_plot as mkplt


# nice usage function
def usage():
    print("""Call this script with the path to the plot list:
    $ make_all_plots.py <path to plot list>""")

# check the command line arguments
if not len(sys.argv) == 2:
    print("Invalid command line arguments")
    usage()
    sys.exit(1)

if __name__ == "__main__":

    plot_list_path = os.path.abspath(sys.argv[1])

    if not os.path.exists(plot_list_path):
        print("Plot list file not found")
        sys.exit(1)
    else:
        plot_list_file = open(plot_list_path,'r')

        for line in plot_list_file:
            try:
                line = line.replace(" ", "")
                mkplt.plot(line.rstrip())
            except:
                print("Plot failed on: %s" % line)
