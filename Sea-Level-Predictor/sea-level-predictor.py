import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv("epa-sea-level.csv")

  # Create scatter plot
  year = df["Year"]
  sea_level = df["CSIRO Adjusted Sea Level"]
  plt.scatter(year, sea_level)

  # Set the axis labels and titles
  plt.xlabel("Year")
  plt.ylabel("Sea Level (inches)")
  plt.title("Rise in Sea Level")

  # Create first line of best fit
  slope, intercept, r_value, p_value, std_err = linregress(
    df['Year'], df['CSIRO Adjusted Sea Level'])
  x = range(1880, 2051)
  y = slope * x + intercept
  ax = plt.gca()
  ax.plot(x, y, 'r', label='All data')

  # Create second line of best fit
  recent_years = df[df['Year'] >= 2000]
  slope2, intercept2, r_value2, p_value2, std_err2 = linregress(
    recent_years['Year'], recent_years['CSIRO Adjusted Sea Level'])
  x2 = range(2000, 2051)
  y2 = slope2 * x2 + intercept2
  ax.plot(x2, y2, 'g', label='2000 onwards')

  # Add labels and title
  ax.set_xlabel('Year')
  ax.set_ylabel('Sea Level (inches)')
  ax.set_title('Rise in Sea Level')
  ax.legend()

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
