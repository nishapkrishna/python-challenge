import csv
import os

voter = []
voteFor = []

#files to input and output
input_file = os.path.join('election_data.csv')
output_file = os.path.join('election_data_result.txt')
#read the csv and convert it into a list of dictionaries
with open(input_file,'r') as csvfile:
    reader = csv.DictReader(csvfile)
#find the total votes and print result to terminal    
    for row in reader:
        voter.append(row['Voter ID'])
        voteFor.append(row['Candidate'])

print("Election Results")
print("-------------------------")
print(f"Total Votes: {len(voter)}")
print("-------------------------")

# get a list of unique candidates.
cands = list(set(voteFor))
cands.sort()
# get a vote count for each candidate.
candVotes = []
#find total votes for candidate
for cand in cands:
    candVotes.append(voteFor.count(cand))
#find the percentage of votes each candidate got and print the result to terminal
for i in range(len(cands)):
    print(f"{cands[i]}: {'{:.3%}'.format(candVotes[i]/len(voteFor))} ({candVotes[i]})")
     
#Print the winner result to terminal
print("-------------------------")
print(f"Winner: {cands[candVotes.index(max(candVotes))]}")
print("-------------------------\n")
#open and write the result to text file
with open(output_file,'w') as text_write:
    text_write.write("Election Results " +'\n')
    text_write.write("---------------- " +'\n')
    text_write.write("Total Votes :" + str(len(voter)) +'\n')
    text_write.write("----------------------------- " +'\n')
    text_write.write("Vote count for each candidate " +'\n')
    text_write.write("-----------------------------" +'\n')
    for x in range(len(set(cands))):
        #write the percentage of votes each candidate won 
        text_write.write(cands[x] + " : " + str('{:.3%}'.format(candVotes[x]/len(voter)))+ " (" + str(candVotes[x]) + ")" '\n')
    text_write.write("-----------------------------" +'\n')
    text_write.write("Winner : " + str(cands[candVotes.index(max(candVotes))]) +'\n')
    text_write.write("-----------------------------" +'\n')



      
   