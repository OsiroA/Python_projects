# Mean, Variance, and Standard Deviation Calculator

This is a Python module that provides a `calculate()` function for calculating various statistical measures, including mean, variance, and standard deviation, from a list of numbers.

## Usage

### Installation

You can install this module using `pip`:

pip install mean-variance-std-dev


### Example Usage

After installing the module, you can use it in your Python code as follows:

```python
import mean_variance_std_dev as mv

# Example list of numbers
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]

# Call the calculate() function
result = mv.calculate(my_list)

# Print the calculated statistics
print("Mean: ", result["mean"])
print("Variance: ", result["variance"])
print("Standard Deviation: ", result["standard deviation"])
print("Max: ", result["max"])
print("Min: ", result["min"])
print("Sum: ", result["sum"])

Function Signature
The calculate() function takes a list of numbers as input and returns a dictionary containing the calculated statistics. The dictionary has the following keys:

"mean": A dictionary containing the mean calculated along the columns ("axis1"), along the rows ("axis2"), and for the flattened list ("flattened").
"variance": A dictionary containing the variance calculated along the columns ("axis1"), along the rows ("axis2"), and for the flattened list ("flattened").
"standard deviation": A dictionary containing the standard deviation calculated along the columns ("axis1"), along the rows ("axis2"), and for the flattened list ("flattened").
"max": A dictionary containing the maximum value calculated along the columns ("axis1"), along the rows ("axis2"), and for the flattened list ("flattened").
"min": A dictionary containing the minimum value calculated along the columns ("axis1"), along the rows ("axis2"), and for the flattened list ("flattened").
"sum": A dictionary containing the sum calculated along the columns ("axis1"), along the rows ("axis2"), and for the flattened list ("flattened").


Error Handling
The calculate() function performs basic error checking and raises a ValueError if the input list does not contain exactly nine numbers.

Contributing
If you would like to contribute to this project, please submit a pull request with your changes. Contributions are welcome!