#POLL
#import library
import csv
import os

#import file
csvpath = os.path.join("election_data.csv")

#open and read the CSV
with open(csvpath) as file:

    #save file as variable and skip header
    filehandle = csv.reader(file, delimiter=',') 
    next(filehandle, None) #for excluding header row

    #PART 1
    #set variables
    total_votes = 0
    Votes = 0
    percent_votes = 0
    Most_Votes = 0
    Most_Voted = ""
    Candidates = {}
    
    #loop through the rows in the CSV to count the votes
    for row in filehandle:
        #candidates are in the 3rd column
        candidate = row[2]
        total_votes += 1
        #if statement to add one for every time the candidate shows up in the dictionary
        if candidate in Candidates.keys():
            Candidates[candidate] += 1
        else:
            Candidates[candidate] = 1

#print summary header
print("Election Results")
print("----------------------------")
#print total votes
print("Total Votes: " + str(total_votes))
print("----------------------------")

#PART 2
#percentage = (total votes for each candiate / total) *100
#total number of votes for each candidate
for candidate in Candidates:
    Votes += Candidates[candidate]
    #formula for percent of votes for each candidate
    percent_votes = (Candidates[candidate])/(total_votes) * 100

    #print the percentages and votes for every candidate
    print(f"{candidate}: {int(round(percent_votes))}% {Votes}")
    
    #If statement to determine the winner
    #"if the candidate in the dictionary of candidates has that most votes, then..."
    if Candidates[candidate] > Most_Votes:
        Most_Votes = Candidates[candidate]
        Most_Voted = candidate
        
# Print the Winner
print("-------------------------------")
print(f"Winner: {Most_Voted}")
print("-------------------------------")

#export a text file for the results
output_path = os.path.join("results.txt")
#open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the rows
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(["Total Votes: " + str(total_votes)])
    csvwriter.writerow(['----------------------------'])
    for candidate in Candidates:
        Votes += Candidates[candidate]
        percent_votes = (Candidates[candidate])/(total_votes) * 100
        csvwriter.writerow([f"{candidate}: {int(percent_votes)}% {Votes}"])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow([f"Winner: {Most_Voted}"])
    csvwriter.writerow(['----------------------------'])