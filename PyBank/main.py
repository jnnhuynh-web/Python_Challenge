#BANK
#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#print the analysis to the terminal and export a text file with the results.

#import library
import csv
import os

#import file
csvpath = os.path.join("budget_data.csv")
file=open('budget_data.csv', newline='')

filehandle = csv.reader(file, delimiter=',')

#PART 1
#total months and net total amount of "Profit/Losses" 
total_month = 0
total_sum = 0
next(filehandle, None) #for excluding header row
for eachrow in filehandle:
    total_month += 1
    total_sum += int(eachrow[1])

#print summary header
print("Financial Analysis")
print("----------------------------")
#print results
print("Total Months: " + str(total_month))
print("Total: $" + str(total_sum))

#PART 2
#variables for calculating change
revenue = []
date = []
rev_change = []

#loop through the file for list of revenue per month
for row in filehandle:
    revenue.append(int(row[1]))
    date.append(row[0])

#loop through the file for change
for i in range(len(revenue)):
    rev_change.append(revenue[i-1] - revenue[i])
    #average change
    avg_rev_change = sum(rev_change)/len(rev_change)
    #max and min change
    max_rev_change = max(rev_change)
    min_rev_change = min(rev_change)
    #date of max and min change
    max_rev_change_date = str(date[rev_change.index(max(rev_change))])
    min_rev_change_date = str(date[rev_change.index(min(rev_change))])


#print the average change, the max and min change
print("Average Revenue Change: $" + str(avg_rev_change))
print("Greatest Increase in Revenue:" + max_rev_change_date +"($" + max_rev_change,")")
print("Greatest Decrease in Revenue:" + min_rev_change_date +"($" + min_rev_change,")")

#export the text file with the results
csvwriter = csv.writer(csvfile, delimiter=',')
# Write the first row (column headers)
output_path = os.path.join("results.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:
    csvwriter.writerow(["Total Votes:" + ])
writeFile.close()