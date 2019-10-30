import os
import csv

# Write a function returning average for candidate votes and total votes
def averageVotes(candidateVotes, totalVotes):
    return (candidateVotes / totalVotes) * 100

# Path to collect data from the Resources folder
vote_csv = os.path.join('.', 'Resources', 'election_data.csv')
# print(vote_csv) # shows path to data file

# Read the CSV file using the CSV module
with open(vote_csv, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader) # provides file info

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}") # prints header info to screen

    # initialize total vote count
    totalVotes = 0 
    vCountMax = 0 
    vIndexMax = -1  
    
    # set up empty name and vote count lists
    nameList = []
    voteCount = []
    
    # Read each row of data after the header
    for row in csvreader:
        totalVotes = totalVotes + 1
        candidate = row[2]
        if candidate in nameList:
            # candidates name is already in list add votes to their count
            vIndex = nameList.index(candidate)
            voteCount[vIndex] = voteCount[vIndex] + 1
        else:
            # append candidates name to the name list, and then add a vote to their count
            nameList.append(candidate)
            voteOne = 1
            voteCount.append(voteOne)

print("\r\nElection Results")
print("-------------------------")
print(f"Total Votes: {totalVotes}")
print("-------------------------")
for candidate in nameList:
    vIndex = nameList.index(candidate)
    vCount = voteCount[vIndex]
    average = averageVotes(vCount, totalVotes)
    print(f"{candidate} {average:.3f}% ({vCount})")
    if vCount > vCountMax:
        vIndexMax = vIndex
        vCountMax = vCount
print("-------------------------")
print(f"Winner: {nameList[vIndexMax]}")


# save the output file path
output_file = os.path.join("voteResults.txt")

# open the output file, create a header row, and then write the zipped object to the csv
output_file = open("voteResults.txt", "wt") 
output_file.write("\nElection Results\n")
output_file.write("-------------------------\n")
output_file.write(f"Total Votes: {totalVotes}\n")
output_file.write("-------------------------\n")
for candidate in nameList:
    vIndex = nameList.index(candidate)
    vCount = voteCount[vIndex]
    average = averageVotes(vCount, totalVotes)
    output_file.write(f"{candidate} {average:.3f}% ({vCount})\n")
output_file.write("-------------------------\n")
output_file.write(f"Winner: {nameList[vIndexMax]}\n")

# close the file
output_file.close()