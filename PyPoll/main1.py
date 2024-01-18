#this creates a file path across operating systems
import os

# Reads CSV files
import csv

csvpath = os.path.join('election_data.csv')
text_path = "output.txt"


#variables
total_votes = 0
candidates = []
candidate_votes = {}
winner_count = 0
winner = ""



#Opening the csv file
with open(csvpath) as csvfile:

    csvreader = csv.DictReader(csvfile)

    #Looping for total votes
    for row in csvreader:
       
    #total votes  
        total_votes += 1

        candidate = row["Candidate"]
    
    #candidate name
        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes [candidate] = 1

        candidate_votes[candidate] = candidate_votes[candidate] + 1
    
    for candidate in candidate_votes:
        votes = candidate_votes [candidate]
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winner_count):
            winner_count = votes
            winner = candidate

    voter_output = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

    

            









#winning candidate
with open(text_path, 'w') as file:
    file.write("Election Results\n")
    file.write("--------------------\n")
    file.write("Total Votes: %d\n" % total_votes)
    file.write("--------------------\n")
    file.write(voter_output)
    file.write("--------------------\n")
    file.write("Winner : ")
    file.write(winner)
    file.write("--------------------\n")
    









    




    




print(total_votes)
print(candidate_votes)

print(winner)
print(voter_output)












