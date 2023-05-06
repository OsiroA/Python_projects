## README

This code reads sea level data from a CSV file, creates a scatter plot of the data and fits two lines of best fit to show the trend in sea level rise over the years.

### Required Libraries

- pandas
- matplotlib.pyplot
- scipy.stats.linregress

### Function

#### draw_plot()

This function reads the sea level data from "epa-sea-level.csv" file, creates a scatter plot of the data, and then fits two lines of best fit. The first line is fit using all the available data, while the second line is fit using only the data from 2000 onwards. The function then adds labels to the x and y axes, a title to the plot and a legend for the lines of best fit. Finally, it saves the plot as "sea_level_plot.png" and returns the plot.

### Usage

Call the `draw_plot()` function.