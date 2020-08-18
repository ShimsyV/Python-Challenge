# First we will import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


## This os.path.join function is used to concatenate all of the provided arguments 
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

#Setting Variables 
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# Improved Reading using CSV module

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # Read each Row of data 
    for row in csvreader:

        # Calculate total number of votes casted
        total_votes += 1
    
    # Print Results
    print(f"Total_Votes: {total_votes}")