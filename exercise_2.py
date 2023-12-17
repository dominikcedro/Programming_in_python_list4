"""
@author Dominik Cedro
02.12.2023
"""

import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
def task1(hd):
    # Answer the question of whether, according to the analysed dataset, more women or
    # men suffer from heart diseases. By what percentage?
    how_many_males =  hd[(hd['Sex'] == 'male')].shape[0]
    disease_group_male = hd[(hd['Sex'] == 'male') & (hd['Disease'] == True)].shape[0]
    percentage_males = (disease_group_male/how_many_males)*100
    how_many_females = hd[(hd['Sex'] == 'female')].shape[0]
    disease_group_female = hd[(hd['Sex'] == 'female') & (hd['Disease'] == True)].shape[0]
    percentage_females = (disease_group_female/how_many_females)*100
    print(f"among males {round(percentage_males,2)}% are sick, among females {round(percentage_females,2)}% are sick")


def task2(hd):
    # 2. Compare the average value of serum cholesterol separately for the group of women
    # and the group of men depending on the presence of heart disease.
    general_view_cholesterol = hd.groupby(['Sex', 'Disease'])['Serum cholesterol in mg/dl'].mean()
    # males
    males_healthy_cholesterol = hd.loc[
        (hd['Sex'] == 'male') & (hd['Disease'] == False), 'Serum cholesterol in mg/dl'].mean()
    males_ill_cholesterol = hd.loc[(hd['Sex'] == 'male') & (hd['Disease'] == True), 'Serum cholesterol in mg/dl'].mean()
    # females
    females_healthy_cholesterol = hd.loc[
        (hd['Sex'] == 'female') & (hd['Disease'] == False), 'Serum cholesterol in mg/dl'].mean()
    females_ill_cholesterol = hd.loc[(hd['Sex'] == 'female') & (hd['Disease'] == True), 'Serum cholesterol in mg/dl'].mean()
    categories = ['Female disease', 'Female healthy', 'Male disease', 'Male healthy']
    # plot
    fig, ax = plt.subplots()
    bar_width = 0.35
    color1 = 'skyblue'
    color2 = 'dodgerblue'
    color3 = 'lightgreen'
    color4 = 'forestgreen'
    # plot bars
    bar1 = ax.bar(categories[0], females_ill_cholesterol, bar_width, color=color1, label='Bar 1')
    bar2 = ax.bar(categories[1], females_healthy_cholesterol, bar_width, color=color2, label='Bar 2')
    bar3 = ax.bar(categories[2], males_ill_cholesterol, bar_width, color=color3, label='Bar 2')
    bar4 = ax.bar(categories[3], males_healthy_cholesterol, bar_width, color=color4, label='Bar 2')
    # Add labels
    ax.set_xlabel('Groups')
    ax.set_ylabel('Mean value of serum cholesterol in mg/dl')
    ax.set_title('Comparison of mean value of serum cholesterol in mg/dl')
    # Display
    plt.show()

def task3(hd):
    # 3. Draw a histogram of people with heart diseases. In which age range are the most
    # affected individuals?
    disease = hd[hd['Disease'] == True]
    plt.hist(disease['Age'])
    plt.title('Histogram of people with heart diseases')
    plt.xlabel('Age')
    plt.ylabel('Number of people')
    plt.show()


def task4(hd):
    # 4. Draw a box plot for the maximum achieved heart rate during the exercise test
    # depending on the presence of heart disease. What observations can be made based
    # on this plot?
    group_by_max = hd['Maximum heart rate achieved'].groupby(hd['Disease']).mean()
    # print(group_by_max)
    plt.boxplot(group_by_max)
    plt.title('Box plot of maximum achieved heart rate')
    plt.xlabel('Disease')
    plt.ylabel('Maximum achieved heart rate')
    plt.show()

# 5. Draw a bar chart for the frequency of heart disease occurrence depending on whether
# the patient has angina during the exercise test. What observations can be made
# based on the chart?

# group_by_angina = hd.groupby(['Exercise induced angina', 'Disease']).size()
# print(group_by_angina)
#
# plt.bar(group_by_angina.index, group_by_angina.values)
# plt.title('Bar chart of frequency of heart disease occurrence')
# plt.xlabel('Angina')
# plt.ylabel('Number of people')
# plt.show()

def main():
    hd = pd.read_csv("heart_disease_dataset.csv")
    # task1(hd)
    # task2(hd)
    # task3(hd)
    task4(hd)
    # task5(hd)

if __name__ == "__main__":
    main()