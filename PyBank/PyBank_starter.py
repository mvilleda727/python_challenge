# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_months = 0
total_net = 0
# Add more variables to track other necessary financial data
net_change_list = []
previous_month_value = None
greatest_increase = float('-inf')
greatest_decrease = float('inf')
greatest_increase_month = ""
greatest_decrease_month = ""

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract first row to avoid appending to net_change_list
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])
    previous_month_value = int(first_row[1])

    # Process each row of data
    for row in reader: 
        total_months += 1
        current_value = int(row[1])

        # Track the total
        total_net += current_value

        # Net change (current month - previous month)
        net_change = current_value - previous_month_value
        # Append to the list of net changes
        net_change_list.append(net_change)
        previous_month_value = current_value
        
        # Calculate the greatest increase in profits (month and amount)
        if net_change > greatest_increase:
            greatest_increase = net_change
            greatest_increase_month = row[0]

        # Calculate the greatest decrease in losses (month and amount)
        if net_change < greatest_decrease:
            greatest_decrease = net_change
            greatest_decrease_month = row[0]

# Calculate the average net change across the months
if len(net_change_list) > 0:
    average_change = sum(net_change_list) / len(net_change_list)
else:
    average_change = 0

# Generate the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n"
    f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n"
)
#Print the output
print(output)
# Write the results to a text file
with open(file_to_output, "w") as txt_file:
     txt_file.write(output)
