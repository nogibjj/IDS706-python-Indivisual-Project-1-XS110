#######################################################################################
### Python Script performing the same descriptive statistics using Polars or Panda ###
#######################################################################################
import polars as pl
import matplotlib.pyplot as plt


WP_data = pl.read_csv('world_population.csv')
WP_data.head()

WP_data.columns
#country's population in 2022, growth rate and area.

df = WP_data[['2022 Population','Growth Rate','Area (km²)']]

# Head 5 rows
print("=== Dataset Overview ===")
print(df.head())
print("\n")

# Summary statistics using the describe method
summary_stats = df.describe()
print("=== Descriptive Statistics Overview ===")
print(summary_stats)
print("\n")

# Mean, Median and Mode
print("=== Mean and Median Overview ===")
mean = df.mean()
median = df.median()
print("Mean:\n", mean)
print("Median:\n", median)
print("\n")

# Variance and standard deviation
variance = df.var()
std_deviation = df.std()
print("=== Variance and standard deviation Overview ===")
print("Variance:\n", variance)
print("Standard Deviation:\n", std_deviation)

# create a histogram
plt.hist(df[['2022 Population']], bins=20, color='blue', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of 2022 Population ')
plt.show()

# Create a boxplot
plt.boxplot(df[['2022 Population']])
# Add labels and title
plt.xlabel('2022')
plt.ylabel('2022 Population')
plt.title('Boxplot of 2022 Population')
# Show the plot
plt.show()