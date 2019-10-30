import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')
# print(budget_csv) # shows path to data file

# Read the CSV file using the CSV module
with open(budget_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader) # provides file info

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}") # prints header info to screen

    # initialize profit / loss and sum
    profitIncrease = 0
    profitDecrease = 0
    sum = 0
    totalMonths = 0

    # Read each row of data after the header
    for row in csvreader:
        totalMonths = totalMonths + 1
        sum = sum + int(row[1])

        if int(row[1]) > profitIncrease:
            profitIncrease = int(row[1])
            monthMax = row[0]
        elif int(row[1]) < profitDecrease:
            profitDecrease = int(row[1])
            monthMin = row[0]

print("     Financial Analysis     ")
print("----------------------------")
print(f"Total Months: {totalMonths}")
print(f"Total: ${sum:.2f}")
print(f"Average Change: ${(sum / totalMonths):.2f}")
print(f"Greatest Increase in Profits: {monthMax} (${profitIncrease:.2f})")
print(f"Greatest Decrease in Profits: {monthMin} (${profitDecrease:.2f})")

# save the output file path
output_file = os.path.join("financials.txt")

# open the output file, create a header row, and then write the zipped object to the csv
output_file = open("financials.txt", "wt") 
output_file.write("     Financial Analysis     \n")
output_file.write("----------------------------\n")
output_file.write(f"Total Months: {totalMonths}\n")
output_file.write(f"Total: ${sum:.2f}\n")
output_file.write(f"Average Change: ${(sum / totalMonths):.2f}\n")
output_file.write(f"Greatest Increase in Profits: {monthMax} (${profitIncrease:.2f})\n")
output_file.write(f"Greatest Decrease in Profits: {monthMin} (${profitDecrease:.2f})\n")

# close the file
output_file.close()