Sure! Here is a possible README file for your code:

# README

## Introduction

This code is designed to analyze demographic data from the U.S. census, contained in the `adult.data.csv` file. The code provides various statistics on different aspects of the data, such as race, age, education level, income, and occupation.

## Dependencies

The following dependencies are required to run the code:
- pandas: a Python library for data manipulation and analysis

You can install the dependencies using pip with the following command:

```
pip install pandas
```

## Usage

To run the code, simply run the `calculate_demographic_data()` function. This function takes one optional argument, `print_data`, which defaults to `True`. If `print_data` is set to `True`, the function will print out the various statistics on the data. Otherwise, it will simply return the statistics as a Python dictionary.

## Output

The `calculate_demographic_data()` function calculates the following statistics on the data:

- The number of individuals in each race.
- The average age of men.
- The percentage of individuals with a Bachelor's degree.
- The percentage of individuals with advanced education (i.e., Bachelors, Masters, or Doctorate) who earn more than 50K, and the percentage of individuals without advanced education who earn more than 50K.
- The minimum number of hours a person works per week.
- The percentage of individuals who work the minimum number of hours per week and earn more than 50K.
- The country with the highest percentage of individuals who earn more than 50K.
- The most popular occupation for individuals who earn more than 50K in India.

The statistics are returned as a Python dictionary or printed to the console, depending on the `print_data` argument.