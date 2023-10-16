# Example
Estimate standard error of correlated data

# Author
- Dr. Aristotelis P. Sgouros (arissgouros@gmail.com)

# Organization
The directory includes the following files:
 - README           -> current file
 - sample_data.xlsx -> excel file used for the generation of sample data and for testing the implementation
 - sample_data.dat  -> sample correlated data
 - run.sh           -> executable file for processing the sample data
 - o.log            -> output file

# Description
The excel file can be used for generating sample data subject to a prescribed correlation length (cell B19) and noise factor (cell B20). Furthermore, the generated data is subjected to the block averaging algorithm; see cells D19-T24. A side-by-side comparison between the excel and python implementation is shown in the second graph.
