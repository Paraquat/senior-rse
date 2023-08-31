# Scenario

A scientist asks you to write a command line tool that analyses some data from an antibody binding experiment. The input is a csv 
with three columns: `index`, `optical_density` and `amino_acid_sequence`. The tool should provide two outputs:  
* a histogram of optical densities as a PNG file
* a csv with the following statistics: min, max and mean optical density for amino acid groups to an accuracy of 1 decimal place.


# Task 

Create a production quality software tool to implement the above user story. 

We have spoken to the user representative and they agreed that the initial task 
should be to focus on core functionality, so we have refined the functional 
requirements to a limited set which should provide them with a minimum viable 
product: 

  * Input is in the form of a comma-separated file (CSV) in which rows are 
    separated by newline characters and the value of each column within a row 
    is separated by a comma.
  * Output plot to be stored as PNG with clear annotations.
    
Our user representative has also provided a tiny example of the input data and output data files
and we have included these in the `example_data` directory.

The tool should be developed with acceptance and unit tests that would aid 
further collaborative development. Considering that the team is most proficient
using Python, the tool should be written in that language as well, to ensure
continued development and maintenance. 

The purpose of this task is for you to showcase your approach to software 
development. We would expect to see a production ready tool, with associated deployment strategy and documentation.
Please do not spend more than three hours on this task.

