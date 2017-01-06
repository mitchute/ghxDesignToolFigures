import matplotlib.pyplot as plt
import numpy as np


def plot(args):

	# split in to separate files
	args = args.split(",")
	
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

	# plot percent diff. vs. approach temp
	i = 1
	for data in percent_error:
		axarr[1].plot(data[0], data[1], color=colors[i], ls=lines[i], lw=2.0)
		i += 1

	# set labels
	axarr[0].set_ylabel("m/kW")
	axarr[1].set_xlabel(r"Approach Temp. Difference $(^\circ C)$ [Coil Exit Temp. - Lake Temp.]")
	axarr[1].set_ylabel("% Difference from \"Typical\"")

	# set axis limits
	axarr[0].set_xlim([1, 6])
	
	# grid lines
	axarr[0].grid(b=True, which='major', color='b')
	axarr[1].grid(b=True, which='major', color='b')

	# twin axes
	axarr[0].twinx()
	axarr[0].twiny()

	# save figure
	# plt.savefig("NumIter.pdf", bbox_inches='tight')
	plt.show()


