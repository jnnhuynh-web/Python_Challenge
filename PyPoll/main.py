#POLL
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.
#print the analysis to the terminal and export a text file with the results.

#import library
import csv
import os

from collections import Counter

#import file
csvpath = os.path.join("election_data.csv")
file=open('election_data.csv', 'r', newline='')

filehandle = csv.reader(file, delimiter=',')

#total months and net total amount of "Profit/Losses" 
total_votes = 0
next(filehandle, None) #for excluding header row
for eachrow in filehandle:
    total_votes += 1
#print summary header
print("Election Results")
print("----------------------------")
#print results
print("Total Votes: " + str(total_votes))

#total for each candidate "Khan", "Correy", "Li", "O'Tooley" 
Khan = 0
next(filehandle, None) #for excluding header row
for eachrow in filehandle:
    if i == "Khan"
        print(count.Khan())
# percentages = total votes for each candiate / total *100


#winner = max
#print(winner)

#export a text