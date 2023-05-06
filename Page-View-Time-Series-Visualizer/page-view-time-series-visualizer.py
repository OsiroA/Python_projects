import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)

# Clean data
low_bound = df["value"].quantile(0.025)
high_bound = df["value"].quantile(0.975)
df = df[(df["value"] >= low_bound) & (df["value"] <= high_bound)]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(16, 6))
    ax.plot(df.index, df["value"], color="tab:blue")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Add new column with month extracted from date
    df["month"] = df.index.month_name()

    # Group data by month and calculate mean
    df_bar = df.groupby("month")["value"].mean()

    # Set order of months
    Months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    df_bar = df_bar.reindex(Months)

    # Create bar chart
    fig, ax = plt.subplots(figsize=(12, 6))
    ax = df_bar.plot(kind="bar", legend=False)
    ax.set_xlabel("Months")
    ax.set_ylabel("Average Page Views")
    ax.set_title("Average Page Views per Month (2016-2019)")

    # Add horizontal line at y=mean
    ax.axhline(df_bar.mean(), color="r", linestyle="--")

    # Add legend
    ax.legend(["Monthly Average"])

    # Save figure and return
    fig.savefig("bar_plot.png")
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    print(df_box.index)
    df_box["year"] = pd.DatetimeIndex(df_box["date"]).year
    df_box["month"] = [d.strftime("%b") for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axs = plt.subplots(1, 2, figsize=(16, 7))
    axs[0] = sns.boxplot(x="year", y="value", data=df_box, ax=axs[0])
    axs[1] = sns.boxplot(x="month", y="value", data=df_box, ax=axs[1], order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    axs[0].set_xlabel("Year")
    axs[0].set_ylabel("Page Views")
    axs[0].set_title("Year-wise Box Plot (Trend)")
    axs[1].set_xlabel("Month")
    axs[1].set_ylabel("Page Views")
    axs[1].set_title("Month-wise Box Plot (Seasonality)")

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig