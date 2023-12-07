import os
import csv
election_csv = os.path.join('/Users/phuonglinh/Downloads/Bootcamp/Module-03/Challenge/python-challenge/PyPoll/Resources/election_data.csv')

votes = {}

def election(votes):
    total_votes = sum(votes.values())
    percentages = {name: (count / total_votes * 100, count) for name, count in votes.items()}
    return total_votes, percentages

with open(election_csv, 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)  

    for row in reader:
            vote_id = row[0]  
            name = row[2]  
            votes[vote_id] = name

vote_counts = {}
for name in votes.values():
    vote_counts[name] = vote_counts.get(name, 0) + 1

total_votes, percentage_and_count = election(vote_counts)

winner_name = max(vote_counts, key=vote_counts.get)

print(f'Election Results')
print('----------------------------')
print(f'Total Votes: {total_votes}')
print('----------------------------')
for name, (percentage, count) in percentage_and_count.items():
    print(f"{name}: {percentage:.2f}% ({count})")
print('----------------------------')
print(f"Winner: {winner_name}")
print('----------------------------')