import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv("medical_examination.csv")

# Add 'overweight' column
df['overweight'] = (df['weight'] / ((df['height'] / 100)**2) > 25).astype(int)

# Normalize data
df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)

# Filter data
df = df[(df['ap_lo'] <= df['ap_hi'])
        & (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))]


# Draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt`
  df_cat = pd.melt(df,
                   id_vars=['cardio'],
                   value_vars=[
                     'active', 'alco', 'cholesterol', 'gluc', 'overweight',
                     'smoke'
                   ])

  # Group and reformat the data to split it by 'cardio'
  df_cat = df_cat.groupby(['cardio', 'variable', 'value'],
                          as_index=False).size().reset_index()
  df_cat = df_cat.rename(columns={
    'size': 'total',
    'variable': 'variable',
    'value': 'value'
  })
  df_cat['value'] = df_cat['value'].replace({0: 'No', 1: 'Yes'})

  # Draw the catplot with 'sns.catplot()'
  g = sns.catplot(x='variable',
                  y='total',
                  hue='value',
                  col='cardio',
                  kind='bar',
                  data=df_cat)

  # Get the figure for the output
  fig = g.fig

  # Return the figure
  return fig


def draw_heat_map():
  # Clean the data
  df_heat = df.copy()
  df_heat['BMI'] = df_heat['weight'] / (df_heat['height'] / 100)**2
  df_heat = df_heat.drop('BMI', axis=1)
  df_heat = df_heat[(df_heat['ap_lo'] <= df_heat['ap_hi'])
                    & (df_heat['height'] >= df_heat['height'].quantile(0.025))
                    & (df_heat['height'] <= df_heat['height'].quantile(0.975))
                    & (df_heat['weight'] >= df_heat['weight'].quantile(0.025))
                    & (df_heat['weight'] <= df_heat['weight'].quantile(0.975))]

  # Calculate the correlation matrix
  corr = None
  corr = df_heat.corr()

  # Generate a mask for the upper triangle
  #mask = None
  mask = np.triu(np.ones_like(corr, dtype=bool))

  # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(11, 9))

  # Draw the heatmap with 'sns.heatmap()'
  sns.heatmap(corr,
              mask=mask,
              annot=True,
              fmt='.1f',
              center=0,
              vmin=-0.1,
              vmax=0.25,
              square=True,
              linewidths=.5,
              cbar_kws={
                "shrink": .45,
                "format": "%.1f"
              })

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig
