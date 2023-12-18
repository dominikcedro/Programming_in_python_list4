"""
@author Dominik Cedro
02.12.2023
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def task1(hd):
    how_many_males = hd[(hd['Sex'] == 'male')].shape[0]
    disease_group_male = hd[(hd['Sex'] == 'male') & (hd['Disease'] == True)].shape[0]
    # percentage_males = (disease_group_male/how_many_males)*100
    how_many_females = hd[(hd['Sex'] == 'female')].shape[0]
    disease_group_female = hd[(hd['Sex'] == 'female') & (hd['Disease'] == True)].shape[0]
    # percentage_females = (disease_group_female/how_many_females)*100
    # print(f"among males {round(percentage_males,2)}% are sick, among females {round(percentage_females,2)}% are sick")

    females_values = [(how_many_females-disease_group_female), disease_group_female]
    females_labels = ['Healthy', 'Sick']
    males_values = [how_many_males-disease_group_female, disease_group_male]
    males_labels = ['Healthy', 'Sick']
    categories = ['Men', 'Women']
    bar_width = 0.30
    index = np.arange(len(categories))
    fig, ax = plt.subplots()
    ax.bar(categories, [females_values[0], males_values[0]],color='darkgrey', label='Healthy')
    ax.bar(categories, [females_values[1], males_values[1]],bottom=[females_values[0], males_values[0]], color= 'orange',label='Sick')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Number of People')
    ax.set_title('Distribution of Health Status by Gender')
    # change the colors to green and grey


    ax.legend()
    plt.show()

def task2(hd):
    males_healthy_cholesterol = hd.loc[
        (hd['Sex'] == 'male') & (hd['Disease'] == False), 'Serum cholesterol in mg/dl'].mean()
    males_ill_cholesterol = hd.loc[(hd['Sex'] == 'male') & (hd['Disease'] == True), 'Serum cholesterol in mg/dl'].mean()
    females_healthy_cholesterol = hd.loc[
        (hd['Sex'] == 'female') & (hd['Disease'] == False), 'Serum cholesterol in mg/dl'].mean()
    females_ill_cholesterol = hd.loc[(hd['Sex'] == 'female') & (hd['Disease'] == True), 'Serum cholesterol in mg/dl'].mean()
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
    # Display
    plt.show()

def task3(hd):
    disease = hd[hd['Disease'] == True]
    plt.hist(disease['Age'])
    plt.title('Histogram of people with heart diseases')
    plt.xlabel('Age')
    plt.ylabel('Number of people')
    plt.show()


def task4(hd):
    disease_heartrate = hd.loc[hd['Disease'] == True, 'Maximum heart rate achieved'].values
    healthy_heartrate = hd.loc[hd['Disease'] == False, 'Maximum heart rate achieved'].values
    plt.boxplot([disease_heartrate, healthy_heartrate], labels=['Disease', 'Healthy'])
    plt.title('Box plot for the maximum achieved heart rate')
    plt.xlabel('Groups')
    plt.ylabel('Maximum achieved heart rate')
    plt.show()

def task5(hd):
    freq_matrix = pd.crosstab(index=hd['Disease'], columns=hd['Exercise induced angina'])
    freq_matrix.plot(kind='bar', color=['blue', 'red'])
    plt.title('Frequency of Heart Disease Occurrence based on Exercise-Induced Angina')
    plt.xlabel('Disease')
    plt.ylabel('Frequency')
    plt.show()


def main():
    hd = pd.read_csv("heart_disease_dataset.csv")
    task1(hd)
    # task2(hd)
    # task3(hd)
    # task4(hd)
    # task5(hd)

if __name__ == "__main__":
    main()