# Import Dependencies
import os
import csv

# Define path to collect data from the Resources folder using the os module
budget_csv = os.path.join('.', 'Resources', 'budget_data.csv')

# Read the CSV file using the CSV module
with open(budget_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
   
    # initialize profit, loss, sum, and set month counter
    profitIncrease = 0
    profitDecrease = 0
    sum = 0
    totalMonths = 0

    # initialize values to calculate monthly change differences
    monthAmt = []
    delta = 0
    deltaTotal = 0

    # Read each row of data after the header
    for row in csvreader:
        totalMonths = totalMonths + 1
        sum = sum + int(row[1])

        # use conditional to find the greatest increase/decrease (loss) of profit
        # also set the month for when the max profit/loss(minimum) occured 

        if int(row[1]) > profitIncrease:
            profitIncrease = int(row[1])
            monthMax = row[0]
        elif int(row[1]) < profitDecrease:
            profitDecrease = int(row[1])
            monthMin = row[0]

        # add the monthly amount for the change calculation to the list
        monthAmt.append(int(row[1]))
        
        # use conditional to check for second month and beyond to calculate monthly difference
        if totalMonths > 1:

            # delta is the monthly difference and deltaTotal is the sum of monthly differences
            delta = monthAmt[totalMonths-1] - monthAmt[totalMonths - 2]
            deltaTotal = deltaTotal + delta

# format output and print to screen 
print("     Financial Analysis     ")
print("----------------------------")
print(f"Total Months: {totalMonths}")

# f print format (variable: .2f) produces two decimal point float output
print(f"Total: ${sum:.2f}")
print(f"Average Change: ${(deltaTotal / (totalMonths - 1)):.2f}")
print(f"Greatest Increase in Profits: {monthMax} (${profitIncrease:.2f})")
print(f"Greatest Decrease in Profits: {monthMin} (${profitDecrease:.2f})")

# save the output file path
output_file = os.path.join("financials.txt")

# open the output file to write a text file
output_file = open("financials.txt", "wt") 

# Write the formatted output to the text file
output_file.write("     Financial Analysis     \n")
output_file.write("----------------------------\n")
output_file.write(f"Total Months: {totalMonths}\n")
output_file.write(f"Total: ${sum:.2f}\n")
output_file.write(f"Average Change: ${(deltaTotal / (totalMonths - 1)):.2f}\n")
output_file.write(f"Greatest Increase in Profits: {monthMax} (${profitIncrease:.2f})\n")
output_file.write(f"Greatest Decrease in Profits: {monthMin} (${profitDecrease:.2f})\n")

# close the output file
output_file.close()