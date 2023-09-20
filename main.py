#######################################################################################
### Python Script performing the same descriptive statistics using Polars or Panda ###
#######################################################################################
from lib import descript_stat
from lib import histogram
from lib import boxplot
from lib import readfile



if __name__ == "__main__":
    data = readfile('world_population.csv')
    descript_stat(data)
    histogram(data)
    boxplot(data)
