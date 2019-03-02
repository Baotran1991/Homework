# Homework
Question 5 and 6
Pseudocode

1)	Setup Argument Parser

  1.1).	Accept csv file as argument
  
  1.2).	Check if file exists, and raise error if it doesn’t.
  
  1.3).	Read data from the csv file and store in Pandas Data frame
  
  d.	If the csv file contains header, then the header flag should be true in “read_csv”
  
2)	Organize Data
  a.	Use functions from Pandas library to remove unwanted columns from Data Frame
  b.	Clean data if needed from unknown character sets.
3)	Check Data Shape
4)	Compute Summary Statistics
  a.	Use Numpy to calculate the mean and standard deviation on Data.
5)	Visualize the Data
  a.	Iterate over the columns in data
  b.	For each column, create a histogram using Matplot.Pyplot
  c.	Save the histograms in files.
  d.	Nested Iteration.
    i.	Iterate over the columns in data.
    ii.	If current column matches the column in parent loop, then skip
    iii.	Create Scatter plot using Matplot Lib for the columns in child and parent loops
    
