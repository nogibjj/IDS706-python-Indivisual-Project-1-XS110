#######################################################################################
### Python Script performing the same descriptive statistics using Polars or Panda ###
#######################################################################################
import lib

# read in data
WP_data = lib.readfile("world_population.csv")
# country's population in 2022, growth rate and area.
data = WP_data[["2022 Population", "Growth Rate", "Area (km²)"]]

# descriptive statistics
lib.descript_stat(data)

# histogram
lib.histogram(data)

# boxplot
lib.boxplot(data)

# generate report
input_file_path = "world_population.csv"  # Update with your dataset file path
summary_report = "report.md"
histogram_image = "image/population_histogram.png"
boxplot_image = "image/population_boxplot.png"

WP_data = lib.readfile(input_file_path)

# country's population in 2022, growth rate and area.
data = WP_data[["2022 Population", "Growth Rate", "Area (km²)"]]

lib.descript_stat(data)
lib.save_report(data, summary_report, histogram_image, boxplot_image)


