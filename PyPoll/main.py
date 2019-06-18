import os
import csv
csvpath = os.path.join('..', 'Resources', 'election_data.csv')
from collections import Counter


votescount = Counter()
candidate_list = [] 
percentage = [] 
final_result = [] 



with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    if csv.Sniffer().has_header:
        next(csvreader)
    for row in csvreader: 
        candidate_list.append(row[2])

    totalVotes = len(candidate_list)

    for name in candidate_list: 
        votescount[name] += 1

    winner = max(zip(votescount.values(), votescount.keys())) 
    names = tuple(votescount.keys())
    votes = tuple(votescount.values())

    for x in votes:
        percentage.append((int(x)/totalVotes)*100) 
    
    print('Election Results')
    print('-----------------------')
    print('Total Votes: ' + str(totalVotes))
    print('-----------------------')
    for x in range(len(names)):
        message = names[x] + ': ' + str(round(percentage[x],1)) + '% ' + '(' + str(votes[x]) + ')'
        print(message)
    print('-----------------------')
    print('Winner: ' + winner[1])
    print('-----------------------')

    f = open("output.txt", "a")
    print(f'Election Results', file=f)
    print(f"-------------------------------", file=f)
    print(f'Total Votes: ' + str(totalVotes), file=f)
    print(f'-----------------------', file=f)
    for x in range(len(names)):
        message = names[x] + ': ' + str(round(percentage[x],1)) + '% ' + '(' + str(votes[x]) + ')'
        print(message, file=f)
    print(f'-----------------------', file=f)
    print(f'Winner: ' + winner[1], file=f)
    print(f'-----------------------', file=f)
    f.close()