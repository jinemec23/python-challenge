# Import file
import os
import csv

# Set path
budget_data = os.path.join('Resources','election_data.csv')

#Set variable lists
voter_id = []
candidates = []
candidate_votes = {}
win = 0


# Use with open to read the file
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader,None)
    for row in csvreader:
        candidate = row[2]
        voter_id.append(row[0])
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 1
        else:
            candidate_votes[candidate] +=1

# Set loops to get data
vote_total = len(voter_id)
vote_percent = {candidate : candidate_votes[candidate]/vote_total \
    for candidate in candidates}
for x in vote_percent.items():
    if x[1] > win:
        win = x[1]
        winner = x[0]


#Set Results to List
Election_Results = []
Election_Results.append('Election Results')
Election_Results.append("------------------------")
Election_Results.append(f'Total Votes: {int(vote_total)}')
Election_Results.append("------------------------")
for candidate in candidates:
    Election_Results.append("{}:".format(candidate) + \
        "{:.1%}".format(vote_percent[candidate]) + \
            "({})".format(candidate_votes[candidate])) 
Election_Results.append("------------------------")   
Election_Results.append(f'Winner: {winner}')
Election_Results.append("------------------------")   

#Print and Export Results to txt file
for line in Election_Results:
    print(line)

output_file = os.path.join('Analysis','pypoll_analysis.txt')
with open(output_file,"w", newline="") as textfile:
    for line in Election_Results:
        textfile.write(line + '\n')