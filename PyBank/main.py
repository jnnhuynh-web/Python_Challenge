#BANK
#import library
import csv
import os

#import filepath
csvpath = os.path.join("budget_data.csv")

#open the file
with open(csvpath) as file:
    #use filehandle as the name for the file
    filehandle = csv.reader(file,delimiter=',')
    #exclude the header row
    next(filehandle, None)

    #PART 1
    #total months and net total amount of "Profit/Losses"
    #zero out the month and sum as the starting point
    total_month = 0
    total_sum = 0
    #loop through the rows for the sum and month
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
    #list the revenue, dates, and list for revenue storage
    revenue = []
    date = []
    rev_change = []
    #loop through each rows
    for row in filehandle:
        revenue.append(row[1])
        date.append(row[0])
        rev_change.append(revenue[row-1] - revenue[row])

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
output_path = os.path.join("results.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:
    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')
    # Write the rows
    csvwriter.writerow(['Financial Analysis'])
    csvwriter.writerow(['----------------------------'])
    csvwriter.writerow(['Total Months: ' + str(total_month)])
    csvwriter.writerow(['Total: $' + str(total_sum)])
    csvwriter.writerow(["Average Revenue Change: $" + str(avg_rev_change)])
    csvwriter.writerow(["Greatest Increase in Revenue:" + max_rev_change_date +"($" + max_rev_change,")"])
    csvwriter.writerow(["Greatest Decrease in Revenue:" + min_rev_change_date +"($" + min_rev_change,")"])