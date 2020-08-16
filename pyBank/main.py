# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv


## This os.path.join function is used to concatenate all of the provided arguments 
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

#Setting Variables 
total_months = 0
net_amount = 0
monthly_change = 0
greatest_increase = 0
greatest_increase_month = 0
greatest_decrease = 0
greastest_decrease_month = 0

# Improved Reading using CSV module

with open(csvpath, 'r') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first 
    csv_header = next(csvreader)

    # row is the next line in the csvreader
    row = (csvreader)

    # Setting the variables for row
    #previous_row = int(row[1]) 
    #total_months += 1
    #net_amount += int(row[1])
    
    for row in csvreader:

    # Read each row of data and calculate the total months, net amount
        total_months += 1

    print(f'Total Months: {total_months}')

