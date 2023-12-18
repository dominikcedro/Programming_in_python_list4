"""
@author Dominik Cedro
02.12.2023
"""

import matplotlib.pyplot as plt
import pandas as pd


def task1(hd):
    """ This function creates stacked bar chart representing health status among sexes.

    Args:
        hd: Heart disease dataset
    """
    male_sick = hd[(hd['Sex'] == 'male') & (hd['Disease'] == True)].shape[0]
    male_healthy = hd[(hd['Sex'] == 'male') & (hd['Disease'] == False)].shape[0]
    female_sick = hd[(hd['Sex'] == 'female') & (hd['Disease'] == True)].shape[0]
    female_healthy = hd[(hd['Sex'] == 'female') & (hd['Disease'] == False)].shape[0]
    sick = [male_sick, female_sick]
    healthy = [male_healthy, female_healthy]

    total_males = sum(sick[:1] + healthy[:1])
    total_females = sum(sick[1:] + healthy[1:])
    percent_sick_m = (sick[0] / total_males) * 100
    percent_sick_f = (sick[1] / total_females) * 100

    categories = ['Males', 'Females']
    fig, ax = plt.subplots()
    bars1 = ax.bar(categories, sick, color='orange', label='Sick')
    bars2 = ax.bar(categories, healthy, bottom=sick, color='gray', label='Healthy')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Number of Individuals')
    ax.set_title('Health Status by Gender')
    ax.legend()
    ax.text(categories[0], sick[0] / 2, f'{percent_sick_m:.2f}%', ha='center', va='center', color='white',
            fontsize=10)
    ax.text(categories[1], sick[1] / 2, f'{percent_sick_f:.2f}%', ha='center', va='center', color='white',
            fontsize=10)
    plt.savefig('ex2_1.pdf')

    plt.show()



def task2(hd):
    """ Generates bar graph comparing mean value of serum cholesterol in mg/dl among different health groups.

    Args:
        hd: Heart disease dataset
    """
    males_healthy_cholesterol = hd.loc[
        (hd['Sex'] == 'male') & (hd['Disease'] == False), 'Serum cholesterol in mg/dl'].mean()
    males_ill_cholesterol = hd.loc[(hd['Sex'] == 'male') & (hd['Disease'] == True), 'Serum cholesterol in mg/dl'].mean()
    females_healthy_cholesterol = hd.loc[
        (hd['Sex'] == 'female') & (hd['Disease'] == False), 'Serum cholesterol in mg/dl'].mean()
    females_ill_cholesterol = hd.loc[(hd['Sex'] == 'female') & (hd['Disease'] == True),
    'Serum cholesterol in mg/dl'].mean()
    categories = ['Female disease', 'Female healthy', 'Male disease', 'Male healthy']
    fig, ax = plt.subplots()
    bar_width = 0.35
    color1 = 'skyblue'
    color2 = 'dodgerblue'
    color3 = 'lightgreen'
    color4 = 'forestgreen'
    bar1 = ax.bar(categories[0], females_ill_cholesterol, bar_width, color=color1, label='Bar 1')
    bar2 = ax.bar(categories[1], females_healthy_cholesterol, bar_width, color=color2, label='Bar 2')
    bar3 = ax.bar(categories[2], males_ill_cholesterol, bar_width, color=color3, label='Bar 2')
    bar4 = ax.bar(categories[3], males_healthy_cholesterol, bar_width, color=color4, label='Bar 2')
    ax.set_xlabel('Groups')
    ax.set_ylabel('Mean value of serum cholesterol in mg/dl')
    ax.set_title('Comparison of mean value of serum cholesterol in mg/dl')
    plt.savefig('ex2_2.pdf')

    plt.show()


def task3(hd):
    """ Generates histogram of people with heart diseases.
    Args:
        hd: Heart disease dataset
    """
    disease = hd[hd['Disease'] == True]
    plt.hist(disease['Age'])
    plt.title('Histogram of people with heart diseases')
    plt.hist(disease['Age'], color='green')
    plt.xlabel('Age')
    plt.ylabel('Number of people')
    plt.savefig('ex2_3.pdf')

    plt.show()



def task4(hd):
    """ Generates box plot for the maximum achieved heart rate.
    Args:
        hd: Heart disease dataset
    """
    disease_heartrate = hd.loc[hd['Disease'] == True, 'Maximum heart rate achieved'].values
    healthy_heartrate = hd.loc[hd['Disease'] == False, 'Maximum heart rate achieved'].values
    plt.boxplot([disease_heartrate, healthy_heartrate], labels=['Disease', 'Healthy'])
    plt.title('Box plot for the maximum achieved heart rate')
    plt.xlabel('Groups')
    plt.ylabel('Maximum achieved heart rate')
    plt.savefig('ex2_4.pdf')

    plt.show()



def task5(hd):
    """ Generates bar chart representing frequency of heart disease occurrence based on exercise-induced angina.
    Args:
        hd: Heart disease dataset
    """
    freq_matrix = pd.crosstab(index=hd['Disease'], columns=hd['Exercise induced angina'])
    freq_matrix.plot(kind='bar', color=['gray', 'orange'])
    plt.title('Frequency of Heart Disease Occurrence based on Exercise-Induced Angina')
    plt.subplots_adjust(bottom=0.2)
    plt.xlabel('Disease present')
    plt.ylabel('Frequency')
    # plt.savefig('ex2_5extra.pdf')
    plt.show()



def main():
    hd = pd.read_csv("heart_disease_dataset.csv")
    # task1(hd)
    # task2(hd)
    # task3(hd)
    # task4(hd)
    task5(hd)


if __name__ == "__main__":
    main()
