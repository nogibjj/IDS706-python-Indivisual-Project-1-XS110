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
