import os
import os.path as op
from argparse import ArgumentParser
import pandas as pd
import numpy as np
import matplotlib.pyplot as plot

# Create Parser to load file passed as argument
parser = ArgumentParser(description='A CSV reader + stats maker')
parser.add_argument('csvfile',
                    type=str,
                    help='Path to the input csv file.')

parsed_args = parser.parse_args()
my_csv_file = parsed_args.csvfile

# Check if file exists
assert op.isfile(my_csv_file), "This file doesnt not exists"

# Read data into the dataframe
data = pd.read_csv(my_csv_file, sep='\s+|,')

# Remove the ID column, as its not real data but just index
del data['ID']

# Verify data shape i.e. its rows and columns
print(data.shape)

# Use numpy to calculate mean and standard deviation on data
print("MEAN: ")
print(np.mean(data))
print("SD: ")
print(np.std(data))

# Visualize the data
for d in data:
    n, bins, patches = plot.hist(data[d], 50, facecolor='green')
    plot.xlabel("frequency")
    plot.ylabel("Number of " + d)
    plot.title(r'Histogram for ' + d)
    #plot.axis([40, 160, 0, 0.03])
    plot.grid(True)
    plot.savefig(d + '.png')
    
    for e in data:
        if(d == e):
            continue
        area = np.pi*3
        colors = "red"
        # Reference: https://pythonspot.com/matplotlib-scatterplot/
        plot.scatter(data[d], data[e], s=area, c=colors, alpha=0.5)
        plot.title('Scatter plot pythonspot.com')
        plot.xlabel('x')
        plot.ylabel('y')
        plot.savefig(d + "_" + e + '.png')
    
print("The End")
