# README

This code contains three functions that generate different types of visualizations using the data from the `fcc-forum-pageviews.csv` file. 

## Required libraries
The following libraries are required to run this code:
- pandas
- matplotlib
- seaborn

## Data
The data is read from a csv file named `fcc-forum-pageviews.csv` that contains daily page views of the freeCodeCamp forum from May 2016 to December 2019.

## Functions

### `draw_line_plot()`
This function generates a line plot that shows the daily page views over the entire period of the dataset.

### `draw_bar_plot()`
This function generates a bar chart that shows the average page views for each month of the year.

### `draw_box_plot()`
This function generates two box plots, one that shows the yearly trend in page views and the other that shows the seasonality of the page views by month.

## Outputs
Each function generates a plot and saves it to a file with the following names:
- `line_plot.png`
- `bar_plot.png`
- `box_plot.png` 

The plot objects are also returned by each function and can be used for further analysis or customization.