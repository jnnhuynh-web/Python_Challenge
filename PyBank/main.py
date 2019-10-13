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

#Average Change: $-2315.12
#Greatest Increase in Profits: Feb-2012 ($1926159)
#Greatest Decrease in Profits
average_change = 0
greatest_increase = 0
greatest_decrease = 0
next(filehandle, None) #for excluding header row
for eachrow in filehandle:
    previous=int(eachrow[1])
    average_change=int(eachrow[1])-previous

#print
print("Average Change: $" + str(average_change))
print("Greatest Increase in Profits: " + "month " + str(greatest_increase))
print("Dreatest Decrease in Profits: " + "month " + str(greatest_decrease))



#export the text file with the results