'''get_statistics.py'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=W0621
print(" ")

'''

Type of Question:
- math concept

Question:
Write a function 
that takes in a list of numbers 
and returns a dictionary
containing the following statistics about the numbers: 
the 
mean, 
median, 
mode, 
sample variance, 
sample standard deviation, 
and 95% confidence interval for the mean.

Clarifying Questions / Insights:
- large-enough sample size to use a z-score of 1.96
- If multiple modes exist, any can be returned.
- You shouldn't use any libraries.
- automatically round output values to the fourth decimal.

Edge cases:
-

Base case:
-

Input:
- Intuitive
- Primitive Types
		- Numbers
			- Zero (0)
			- NULL or nil
			- Negative Numbers
			- Floats or Doubles (clarifies if Ints only?)
			- Min/Max Int
		- Arrays
			- Empty array
			- Nested or not nested
		- Dictionaries (Hashmaps)
			- Collisions
	
- If I knew / had this....
	-

Output:
-
'''


# Time: O() | # Space: O()
def get_statistics(input_list):
    if len(input_list) == 0:
        return None

    # mean
    mean = sum(input_list) / len(input_list)

    # median
    sorted_list = sorted(input_list)
    
    middle_idx = (len(sorted_list) - 1) // 2

    if len(sorted_list) % 2 == 1:  # Odd-length list
        median = sorted_list[middle_idx]
    else:  # Even-length list
        mid_num_1 = sorted_list[middle_idx]
        mid_num_2 = sorted_list[middle_idx + 1]
        median = (mid_num_1 + mid_num_2) / 2

    # mode
    num_frequency = {x: input_list.count(x) for x in set(input_list)}
    mode = max(num_frequency.keys(), key=lambda num: num_frequency[num])

    # sample_variance
    sample_variance = sum([(num - mean) ** 2 / (len(input_list) - 1) for num in input_list])

    # sample_standard_deviation
    sample_standard_deviation = sample_variance ** 0.5

    # mean_confidence_interval
    mean_standard_deviation = sample_standard_deviation / (len(input_list) ** 0.5)

    z_score_standard_error = 1.96 * mean_standard_deviation

    lower_bound = mean - z_score_standard_error
    upper_bound = mean + z_score_standard_error

    mean_confidence_interval = [lower_bound, upper_bound]

    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "sample_variance": sample_variance,
        "sample_standard_deviation": sample_standard_deviation,
        "mean_confidence_interval": mean_confidence_interval
    }

input_list = [2, 1, 3, 4, 4, 5, 6, 7]
print("input_list:", input_list)
print("get_statistics:", get_statistics(input_list))
print(" ")

input_list = [3, 12, 18, 12, 20, 8, 18, 6, 4, 8, 4, 4, 11, 1, 20, 15, 11, 17, 19, 10, 7, 18, 14, 9, 20, 11, 14, 12, 9, 3, 4, 7, 5, 9, 20, 4, 0, 13, 1, 17, 15, 5]
print("input_list:", input_list)
print("get_statistics:", get_statistics(input_list))
print(" ")

input_list = [7, 20]
print("input_list:", input_list)
print("get_statistics:", get_statistics(input_list))
print(" ")

# _recursion
# _iteration
print(" ")
