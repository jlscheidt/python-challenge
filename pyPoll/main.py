import os
import csv

rawVotes = []
candidates = []
votes = []

poll1_csv = os.path.join('..', 'PyPoll', 'election_data_1.csv')
poll2_csv = os.path.join('..', 'PyPoll', 'election_data_2.csv')

with open(poll1_csv, newline="") as csvfile:
    csvreader1 = csv.DictReader(csvfile)
    for row in csvreader1:

        rawVotes.append(row["Candidate"])

with open(poll2_csv, newline="") as csvfile:
    csvreader2 = csv.DictReader(csvfile)
    for row in csvreader2:

        rawVotes.append(row["Candidate"])


totalVotes = (len(rawVotes))
inList = False


candidates[0] = rawVotes[0]
for x in range(0, (totalVotes - 1)):
    for person in candidates:
        if rawVotes[x] == person:
            inList = True
            break
    if(!inList):
        candidates.append(rawVotes)

print("The total votes is: ")
print(totalVotes)
