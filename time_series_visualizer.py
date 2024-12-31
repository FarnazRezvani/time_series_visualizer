'''import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv("C:/Users/SAM-Tech/Desktop/freecode camp/time_series_visualizer/fcc-forum-pageviews.csv")
print(df.head())


df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)


lower_bound = df["value"].quantile(0.025)
upper_bound = df["value"].quantile(0.975)
df = df[(df["value"] >= lower_bound) & (df["value"] <= upper_bound)]
print("Filtered DataFrame:")
print(df.head())



def draw_line_plot ():
    fig, ax = plt.subplots(figsize = (12, 6))
    ax.plot(df.index, df["value"], color = "red" , linewidth = 1)
    ax.set_title(" Daily freeCodeCamp Forum Page Views 5/2016-12/2019 ")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    fig.savefig("line_plot.png")
    return fig
fig = draw_line_plot()
plt.show()



def draw_bar_plot():
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()
    df_bar["month_number"] = df_bar.index.month

    df_bar = df_bar.groupby(["year", "month", "month_number"])["value"].mean().reset_index()
    df_bar = df_bar.sort_values("month_number")
    df_bar_pivot = df_bar.pivot(index="year", columns="month", values="value")
    
    print("Pivoted DataFrame:")
    print(df_bar_pivot.head())
    

    fig = df_bar_pivot.plot(kind= "bar", figsize= (10, 10), legend= True).figure
    plt.title("Average Daily Page Views per Month")
    plt.xlabel("years")
    plt.ylabel("Average Page Views")
    plt.legend(title="month")

    fig.savefig("bar_plot.png")
    return fig
fig =draw_bar_plot()
plt.show()



def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")
    df_box["month_number"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_number")

    fig, axes = plt.subplots(1, 2, figsize = (14, 6), dpi = 100)
    sns.boxplot(x = "year", y = "value", data = df_box, ax = axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x = "month", y = "value", data = df_box, ax = axes[1], order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig
fig =draw_box_plot()
plt.show()'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Import the data
df = pd.read_csv("C:/Users/SAM-Tech/Desktop/freecode camp/time_series_visualizer/fcc-forum-pageviews.csv")
print(df.head())

# Convert date column to datetime and set it as the index
df["date"] = pd.to_datetime(df["date"])
df.set_index("date", inplace=True)

# Clean data by removing top and bottom 2.5% of the data
lower_bound = df["value"].quantile(0.025)
upper_bound = df["value"].quantile(0.975)
df = df[(df["value"] >= lower_bound) & (df["value"] <= upper_bound)]
print("Filtered DataFrame:")
print(df.head())

# Function to draw line plot
def draw_line_plot():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df.index, df["value"], color="red", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    fig.savefig("line_plot.png")
    return fig

fig = draw_line_plot()
plt.show()

def draw_bar_plot():
    df_bar = df.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()  # Ensure full month names
    df_bar["month_number"] = df_bar.index.month

    # Group data by year and month
    df_bar = df_bar.groupby(["year", "month", "month_number"])["value"].mean().reset_index()

    # Sort by month number to get the correct order
    df_bar = df_bar.sort_values("month_number")

    # Create pivot table to have months as columns
    df_bar_pivot = df_bar.pivot(index="year", columns="month", values="value")

    # Ensure months are ordered correctly in the legend
    month_order = ["January", "February", "March", "April", "May", "June", "July", 
                   "August", "September", "October", "November", "December"]
    df_bar_pivot = df_bar_pivot[month_order]

    print("Pivoted DataFrame:")
    print(df_bar_pivot.head())

    fig = df_bar_pivot.plot(kind="bar", figsize=(10, 10), legend=True).figure
    plt.title("Average Daily Page Views per Month")
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Month", labels=month_order)  # Ensure legend labels are in the correct order

    fig.savefig("bar_plot.png")
    return fig

fig = draw_bar_plot()
plt.show()

# Function to draw box plot
def draw_box_plot():
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")
    df_box["month_number"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_number")

    fig, axes = plt.subplots(1, 2, figsize=(14, 6), dpi=100)
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x="month", y="value", data=df_box, ax=axes[1], order=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig

fig = draw_box_plot()
plt.show()
