# Tensorboard-custom-scalar-plots

The bash script do_plot_html takes one argument, which is the path to the log directory, that you wish to plot.

get_scalars.py is a helper python script, that takes the --logdir argument. It will create data_*.csv files depending on the scalar fields, that are supplied in your event files (you can manually check these with e.g. tensorboard --inspect --logdir=xyz).

The output of do_plot_html is a html file with a plot to every scalar field.

Requirements
===
The script requires gnuplot and python to be installed
