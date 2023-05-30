#importing modules
import os
import csv

#setting path for CSV file
csvpath = os.path.join('Resources', 'election_data.csv')

#define lists and counter
candidates = []
num_votes = []
percent_votes = []
total_votes = 0

#opening and reading CSV file and setting delimiter
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #reading header row
    csv_header = next(csvreader)

    #reading all rows after header
    for row in csvreader:

        #add to our vote-counter 
        total_votes += 1 

        #checking if the candidate is in the list of candidates, if it is in the list, adding to the list counting the votes
        #if the candidate is not in the list, we add it to the list of candidates, then we add a 1 to the list counting the votes to start a count for that candidate
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    
    #creating vote percentage list
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)
    
    #calculating winner based on votes
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

#printing analysis to terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

#exporting analysis as a .txt file
with open('analysis/pypoll_analysis.txt', 'w') as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {str(total_votes)}\n" )
    f.write("-------------------------\n")
    for i in range(len(candidates)):
        f.write(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    f.write("-------------------------\n")
    f.write(f"Winner: {winning_candidate}\n")
    f.write("-------------------------")