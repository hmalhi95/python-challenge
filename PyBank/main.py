#importing modules
import os
import csv

#setting path for CSV file
csvpath = os.path.join('Resources', 'budget_data.csv')

#defining variables
total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#opening and reading CSV file and setting delimiter
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    #reading header row
    csv_header = next(csvreader)

    #reading first row for initial data
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])

    #reading all rows after header and first row
    for row in csvreader:
        
        #tracking the dates
        dates.append(row[0])

        #calculating the changes and adding them to a list
        change = int(row[1]) - value
        profits.append(change)
        value = int(row[1])

        #calculating total months
        total_months += 1

        #calculating total profit and loss over the entire time period
        total_pl = total_pl + int(row[1])

    #calculating greatest increase in profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #calculating greatest decrease in profits
    greatest_decrease = min(profits)
    lowest_index = profits.index(greatest_decrease)
    lowest_date = dates[lowest_index]

    #calculating average monthly change in profit and loss over the entire time period
    avg_change = sum(profits)/len(profits)

#printing analysis to terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {lowest_date} (${str(greatest_decrease)})")

#exporting analysis as a .txt file
with open("analysis/pybank_analysis.txt", "w") as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {str(total_months)}\n")
    f.write(f"Total: ${str(total_pl)}\n")
    f.write(f"Average Change: ${str(round(avg_change,2))}\n")
    f.write(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})\n")
    f.write(f"Greatest Decrease in Profits: {lowest_date} (${str(greatest_decrease)})\n")