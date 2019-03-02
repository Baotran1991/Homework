# Homework
Question 5 and 6
Pseudocode
&nbsp;&nbsp;&nbsp;&nbsp;

1)	Setup Argument Parser
&nbsp;&nbsp;&nbsp;&nbsp;a.	Accept csv file as argument
&nbsp;&nbsp;&nbsp;&nbsp;b.	Check if file exists, and raise error if it doesn’t.
&nbsp;&nbsp;&nbsp;&nbsp;c.	Read data from the csv file and store in Pandas Data frame
&nbsp;&nbsp;&nbsp;&nbsp;d.	If the csv file contains header, then the header flag should be true in “read_csv”
2)	Organize Data
&nbsp;&nbsp;&nbsp;&nbsp;a.	Use functions from Pandas library to remove unwanted columns from Data Frame
&nbsp;&nbsp;&nbsp;&nbsp;b.	Clean data if needed from unknown character sets.
3)	Check Data Shape
4)	Compute Summary Statistics
&nbsp;&nbsp;&nbsp;&nbsp;a.	Use Numpy to calculate the mean and standard deviation on Data.
5)	Visualize the Data
&nbsp;&nbsp;&nbsp;&nbsp;a.	Iterate over the columns in data
&nbsp;&nbsp;&nbsp;&nbsp;b.	For each column, create a histogram using Matplot.Pyplot
&nbsp;&nbsp;&nbsp;&nbsp;c.	Save the histograms in files.
&nbsp;&nbsp;&nbsp;&nbsp;d.	Nested Iteration.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i.	Iterate over the columns in data.
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ii.	If current column matches the column in parent loop, then skip
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;iii.	Create Scatter plot using Matplot Lib for the columns in child and parent loops
