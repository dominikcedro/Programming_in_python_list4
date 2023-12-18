"""
@author: Dominik Cedro
Consider a scenario where you have a dataset representing the heights of a population.
You are interested in analysing this dataset, which follows a normal distribution.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp


def generate_height_data(size=1000, mean=170, st_dev=10):
    """ Generates a dataset of heights.
    Args:
        size: int, size of the dataset
        mean: int, mean of the dataset
        st_dev: int, standard deviation of the dataset
    Returns:
         dataset of heights
    """
    return np.random.normal(mean, st_dev, size)


def descriptive_statistics(height_data):
    """ Calculates descriptive statistics of the dataset.
    Args:
        height_data: dataset of heights
    Returns:
         printed (mean, median, standard deviation, variance, min, max)
    """
    print(f"mean: {np.mean(height_data)}")
    print(f"median: {np.median(height_data)}")
    print(f"standard deviation: {np.std(height_data)}")


def visualise_histogram(height_data):
    """Visualises the dataset as a histogram.
    Args:
         height_data: dataset of heights
    """
    plt.hist(height_data)
    plt.title("Histogram of heights")
    plt.xlabel("Height")
    plt.ylabel("Frequency")
    plt.hist(height_data, color="green")
    plt.show()


def calculate_percentiles(height_data):
    """ Calculates percentiles of the dataset.
    Args:
        height_data: dataset of heights
    Returns:
         p25: float, 25th percentile
         p50: float, 50th percentile
         p75: float, 75th percentile
    """
    p25 = np.percentile(height_data, 25)
    p50 = np.percentile(height_data, 50)
    p75 = np.percentile(height_data, 75)

    print(f"percentiles are: {p25}, {p50}, {p75}")
    return p25, p50, p75


def identify_outliers(height_data):
    """ Identifies outliers in the dataset.
    Args:
        height_data: dataset of heights
    Returns:
         outliers: list of outliers
    """
    percentiles = calculate_percentiles(height_data)
    iqr = percentiles[2] - percentiles[0]
    lower = percentiles[0] - 1.5 * iqr
    upper = percentiles[2] + 1.5 * iqr
    print(f"outliers are: {height_data[(height_data < lower) | (height_data > upper)]}")
    return height_data[(height_data < lower) | (height_data > upper)]


def random_sampling(height_data):
    """
    Performs random sampling on the dataset.
    Args:
        height_data: dataset of heights
    Returns:
        random sample: np array of 50 random samples
    """
    return np.random.choice(height_data, 50)


def hypothesis_testing(data, null_hypothesis_mean=165):
    """
    Performs hypothesis testing on the dataset.
    Args:
        data: dataset of heights
        null_hypothesis_mean: int, mean of the null hypothesis
    Returns:
        p-value: float, p-value of the test
    """
    test = ttest_1samp(data, null_hypothesis_mean)
    print(f"p-value: {test[1]}")


def calculate_probability(data, threshold_height=180):
    """
    Calculates the probability of a person being taller than a threshold height.
    Args:
        data: dataset of heights
        threshold_height: int, threshold height
    Returns:
        probability: np float, probability of a person being taller than a threshold height
    """
    result = np.sum(data > threshold_height) / len(data)
    print(f"probability: {result}")


