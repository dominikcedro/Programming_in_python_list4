"""
@author: Dominik Cedro
Consider a scenario where you have a dataset representing the heights of a population.
You are interested in analysing this dataset, which follows a normal distribution.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp


def generate_height_data(size=1000, mean=170, st_dev=10):
    """
    Generates a dataset of heights.
    :param size: size of the dataset
    :param mean: mean of the dataset
    :param st_dev: standard deviation of the dataset
    :return: dataset of heights
    """
    return np.random.normal(mean, st_dev, size)

def descriptive_statistics(height_data):
    """
    Calculates descriptive statistics of the dataset.
    :param height_data: dataset of heights
    :return: mean, median, standard deviation, variance, min, max
    """
    print(f"mean: {np.mean(height_data)}")
    print(f"median: {np.median(height_data)}")
    print(f"standard deviation: {np.std(height_data)}")

def visualise_histogram(height_data):
    """
    Visualises the dataset as a histogram.
    :param height_data: dataset of heights
    """

    plt.hist(height_data)
    plt.show()



def calculate_percentiles(height_data):
    """
    Calculates percentiles of the dataset.
    :param height_data: dataset of heights
    :return: 25th, 50th, 75th percentiles
    """
    p25 = np.percentile(height_data, 25)
    p50 = np.percentile(height_data, 50)
    p75 = np.percentile(height_data, 75)

    print(f"percentiles are: {p25}, {p50}, {p75}")
    return p25, p50, p75

def identify_outliers(height_data):
    """
    Identifies outliers in the dataset.
    :param height_data: dataset of heights
    :return: outliers
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
    :param height_data: dataset of heights
    :return: random sample
    """
    return np.random.choice(height_data, 50)

def hypothesis_testing(data, null_hypothesis_mean=165):
    """
    Performs hypothesis testing on the dataset.
    :param height_data: dataset of heights
    :return: p-value
    """

    return ttest_1samp(data, null_hypothesis_mean)

def calculate_probability(data, threshold_height=180):
    """
    Calculates the probability of a person being taller than a threshold height.
    :param height_data: dataset of heights
    :return: probability
    """
    return np.sum(data > threshold_height) / len(data)

def main():
    """
    Main function. to change it late
    """
    height_data = generate_height_data()
    descriptive_statistics(height_data)
    visualise_histogram(height_data)
    calculate_percentiles(height_data)
    identify_outliers(height_data)
    random_sample = random_sampling(height_data)
    # print(f"random sample: {random_sample}")
    print(f"p-value: {hypothesis_testing(height_data)}")
    print(f"probability: {calculate_probability(height_data)}")

if __name__ == "__main__":
    main()
