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
khan_percent = 0
correy_percent = 0
li_percent = 0
otooley_percent = 0


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

        # Calculate the total number of votes each candidate received
        if (row[2] == "Khan"):
            khan_votes += 1
        elif (row[2] == "Correy"):
            correy_votes += 1
        elif (row[2] == "Li"):
            li_votes += 1
        else:
            otooley_votes += 1

        # Calculate the percentage of votes of each candidate 
        khan_percent = (khan_votes/total_votes)*100
        correy_percent = (correy_votes/total_votes)*100
        li_percent = (li_votes/total_votes)*100
        otooley_percent = (otooley_votes/total_votes)*100

        # Find winner of the election based on popular vote
        winner = max(khan_votes, correy_votes, li_votes, otooley_votes)

        if winner == khan_votes:
            winner_name = "Khan"
        elif winner == correy_votes:
            winner_name = "Correy"
        elif winner == li_votes:
            winner_name = "Li"
        else:
            winner_name = "O'Tooley"
        
    
    # Print Results
    print(f"Election Results")
    print(f"------------------------------")
    print(f"Total_Votes: {total_votes}")
    print(f"------------------------------")
    print(f"Khan: {round(khan_percent, 3)}% ({khan_votes})")
    print(f"Correy: {round(correy_percent, 3)}% ({correy_votes})")
    print(f"Li: {round(li_percent, 3)}% ({li_votes})")
    print(f"O'Tooley: {round(otooley_percent, 3)}% ({otooley_votes})")
    print(f"------------------------------")
    print(f"Winner: {winner_name}")
    print(f"------------------------------")

# Specify the file to write to
output_path = os.path.join('.', 'analysis', 'analysis.txt')

# Open file and write
with open(output_path, 'w') as analysis_file:

    # Write the report
    analysis_file.write(f"Election Results\n")
    analysis_file.write(f"------------------------------\n")
    analysis_file.write(f"Total_Votes: {total_votes}\n")
    analysis_file.write(f"------------------------------\n")
    analysis_file.write(f"Khan: {round(khan_percent, 3)}% ({khan_votes})\n")
    analysis_file.write(f"Correy: {round(correy_percent, 3)}% ({correy_votes})\n")
    analysis_file.write(f"Li: {round(li_percent, 3)}% ({li_votes})\n")
    analysis_file.write(f"O'Tooley: {round(otooley_percent, 3)}% ({otooley_votes})\n")
    analysis_file.write(f"------------------------------\n")
    analysis_file.write(f"Winner: {winner_name}\n")
    analysis_file.write(f"------------------------------\n")
    
