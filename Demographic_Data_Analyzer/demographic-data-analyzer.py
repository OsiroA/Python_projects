import pandas as pd


def calculate_demographic_data(print_data=True):
  # Read data from file
  df = None
  df = pd.read_csv("adult.data.csv")

  # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
  race_count = None
  race_count = df['race'].value_counts()

  # What is the average age of men?
  average_age_men = None
  average_age_men = df[df['sex'] == 'Male']['age'].mean().round(1)

  # What is the percentage of people who have a Bachelor's degree?
  percentage_bachelors = None
  bachelors_count = df['education'].value_counts()['Bachelors']
  total_number = df['education'].count()

  percentage_bachelors = ((bachelors_count / total_number) * 100).round(1)

  # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
  # What percentage of people without advanced education make more than 50K?

  # with and without `Bachelors`, `Masters`, or `Doctorate`
  higher_education = None
  advanced_degree_count = df['education'].value_counts()[[
    'Bachelors', 'Masters', 'Doctorate'
  ]]
  total_number = df['education'].count()
  advanced_degree_sum = advanced_degree_count.sum()
  higher_education = (advanced_degree_sum / total_number) * 100

  lower_education = None
  non_advanced_degree = total_number - advanced_degree_sum
  lower_education = 100 - higher_education

  # percentage with salary >50K
  higher_education_rich = None
  advanced_education = df[df['education'].isin(
    ['Bachelors', 'Masters', 'Doctorate'])]
  ae_high_salary_count = len(
    advanced_education[advanced_education['salary'] == '>50K'])
  ae_above_50k_count = df['education'].value_counts()[[
    'Bachelors', 'Masters', 'Doctorate'
  ]]
  sum_of_ae_above50k = advanced_degree_count.sum()
  higher_education_rich = ((ae_high_salary_count / sum_of_ae_above50k) *
                           100).round(1)

  lower_education_rich = None
  lower_education = df[~df['education'].
                       isin(['Bachelors', 'Masters', 'Doctorate'])]
  le_high_salary_count = len(
    lower_education[lower_education['salary'] == '>50K'])
  le_count = len(lower_education)
  lower_education_rich = round((le_high_salary_count / le_count) * 100, 1)

  # What is the minimum number of hours a person works per week (hours-per-week feature)?
  min_work_hours = None
  min_work_hours = df['hours-per-week'].min()

  # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
  num_min_workers = None
  mnohpwa50k = df[(df['hours-per-week'] == min_work_hours)
                  & (df['salary'] == '>50K')]
  num_min_workers = len(mnohpwa50k)

  rich_percentage = None
  rich_percentage = (num_min_workers /
                     len(df[df['hours-per-week'] == min_work_hours])) * 100

  # What country has the highest percentage of people that earn >50K?

  highest_earning_country = None
  over50kbycountry = df[df['salary'] ==
                        '>50K']['native-country'].value_counts()
  total_of_each_country = df['native-country'].value_counts()
  over_50k_percentage_per_country = (over50kbycountry /
                                     total_of_each_country) * 100
  country_list_sorted = over_50k_percentage_per_country.sort_values(
    ascending=False)
  highest_earning_country = country_list_sorted.index[0]

  highest_earning_country_percentage = None
  highest_earning_country_percentage = (
    over_50k_percentage_per_country.loc[highest_earning_country]).round(1)

  # Identify the most popular occupation for those who earn >50K in India.
  top_IN_occupation = None
  sortthesalary = df[(df['native-country'] == 'India')
                     & (df['salary'] == '>50K')]
  top_IN_occupation = sortthesalary['occupation'].value_counts().idxmax()
  # DO NOT MODIFY BELOW THIS LINE

  if print_data:
    print("Number of each race:\n", race_count)
    print("Average age of men:", average_age_men)
    print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
    print(
      f"Percentage with higher education that earn >50K: {higher_education_rich}%"
    )
    print(
      f"Percentage without higher education that earn >50K: {lower_education_rich}%"
    )
    print(f"Min work time: {min_work_hours} hours/week")
    print(
      f"Percentage of rich among those who work fewest hours: {rich_percentage}%"
    )
    print("Country with highest percentage of rich:", highest_earning_country)
    print(
      f"Highest percentage of rich people in country: {highest_earning_country_percentage}%"
    )
    print("Top occupations in India:", top_IN_occupation)

  return {
    'race_count': race_count,
    'average_age_men': average_age_men,
    'percentage_bachelors': percentage_bachelors,
    'higher_education_rich': higher_education_rich,
    'lower_education_rich': lower_education_rich,
    'min_work_hours': min_work_hours,
    'rich_percentage': rich_percentage,
    'highest_earning_country': highest_earning_country,
    'highest_earning_country_percentage': highest_earning_country_percentage,
    'top_IN_occupation': top_IN_occupation
  }
