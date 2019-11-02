# Import Dependencies
import os
import csv

# Write a function returning average for candidate votes and total votes
def averageVotes(candidateVotes, totalVotes):
    return (candidateVotes / totalVotes) * 100

# Define path to collect data from the Resources folder using the os module
vote_csv = os.path.join('.', 'Resources', 'election_data.csv')

# Read the CSV file using the CSV module
with open(vote_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)

    # initialize total vote count and the high vote count for winning candidate
    totalVotes = 0 
    vCountMax = 0 


    # set up empty name and vote count lists
    nameList = []
    voteCount = []

    # set list counter for max vote 
    vIndexMax = -1  
    
    # Read each row of data after the header
    for row in csvreader:

        # increment total vote count
        totalVotes = totalVotes + 1

        # assign candidate name from third entry in list "row"
        candidate = row[2]

        # use conditional to identify candidate and assign their votes
        if candidate in nameList:

            # candidates name is already in list add votes to their count
            vIndex = nameList.index(candidate)
            voteCount[vIndex] = voteCount[vIndex] + 1
        else:

            # new candidate: append candidates name to the name list, 
            # and then add a vote to their count
            nameList.append(candidate)
            voteOne = 1
            voteCount.append(voteOne)

# format output to screen - add new line at top to improve readability
print("\nElection Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")

# loop through the candidates list and print percent of vote and total votes received
for candidate in nameList:
    vIndex = nameList.index(candidate)
    vCount = voteCount[vIndex]
    average = averageVotes(vCount, totalVotes)
    # f print format (variable: .3f) produces three decimal point float output
    print(f"{candidate} {average:.3f}% ({vCount})")
    if vCount > vCountMax:
        vIndexMax = vIndex
        vCountMax = vCount
print("-------------------------")
print(f"Winner: {nameList[vIndexMax]}")


# save the output file path
output_file = os.path.join("voteResults.txt")

# open the output file to write a text file
output_file = open("voteResults.txt", "wt") 

# Write formatted output to text file
output_file.write("\nElection Results\n")
output_file.write("-------------------------\n")
output_file.write(f"Total Votes: {totalVotes}\n")
output_file.write("-------------------------\n")

# loop through the candidates list and print percent of vote and total votes received
for candidate in nameList:
    vIndex = nameList.index(candidate)
    vCount = voteCount[vIndex]
    average = averageVotes(vCount, totalVotes)
    # f print format (variable: .3f) produces three decimal point float output
    output_file.write(f"{candidate} {average:.3f}% ({vCount})\n")

# after for loop close out the formatted results with a dashed line and the winner's name
output_file.write("-------------------------\n")
output_file.write(f"Winner: {nameList[vIndexMax]}\n")

# close the output file
output_file.close()