import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

# Read the CSV file using the CSV module
with open(budget_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # initialize profit / loss and sum
    profitIncrease = 0
    profitDecrease = 0
    sum = 0

    # Read each row of data after the header
    for row in csvreader:
        totalMonths += row
        sum = sum + row[1]

        if row[1] > profitIncrease:
            profitIncrease = row[1]
            monthMax = row[0]
        elif row[1] < profitDecrease:
            profitDecrease = row[1]
            monthMin = row[0]

print("     Financial Analysis     ")
print("----------------------------")
print("Total Months: " + totalMonths)
print("Total: $" + sum)
print("Average Change: $" + sum / totalMonths)
print("Greatest Increase in Profits: "+ monthMax + " " + profitIncrease)
print("Greatest Decrease in Profits: "+ monthMin + " " + profitDecrease)
