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
total_monthly_change = []
month_count = []
average_monthly_change = 0
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
    row = next(csvreader)

    # Setting the variables for row
    previous_profit_loss = int(row[1]) 
    total_months += 1
    net_amount += int(row[1])
    
    # Read each Row of data 
    for row in csvreader:

    # Calculate the total months
        total_months += 1
    # Calculate the net amount
        net_amount += int(row[1])
    
    # Calculate average change in profit/loss 
        monthly_change = int(row[1]) - previous_profit_loss
        total_monthly_change.append(monthly_change)
        previous_profit_loss = int(row[1])
        month_count.append(row[0])

    # Calculate the greatest increase profit
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

    # Calculate the greatest decrease loss
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greastest_decrease_month = row[0]    

    # Calculate the average change between months
    average_monthly_change = sum(total_monthly_change) / len(total_monthly_change)

print(f'Financial Analysis')
print(f'-------------------------------------------------------')
print(f'Total Months: {total_months}')
print(f'Total: ${net_amount}')
print(f'Average Change: $ {average_monthly_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase_month} (${max(total_monthly_change)}) ')
print(f'Greatest Decrease in Loss: {greastest_decrease_month} (${min(total_monthly_change)}) ')

# Specify the file to write to
output_path = os.path.join('.', 'analysis', 'analysis.txt')

# Open file and write
with open(output_path, 'w') as analysis_file:

    # Write the report
    analysis_file.write(f'Financial Analysis\n')
    analysis_file.write(f'-------------------------------------------------------\n')
    analysis_file.write(f'Total Months: {total_months}\n')
    analysis_file.write(f'Total: ${net_amount}\n')
    analysis_file.write(f'Average Change: $ {average_monthly_change:.2f}\n')
    analysis_file.write(f'Greatest Increase in Profits: {greatest_increase_month} (${max(total_monthly_change)})\n')
    analysis_file.write(f'Greatest Decrease in Loss: {greastest_decrease_month} (${min(total_monthly_change)})\n')