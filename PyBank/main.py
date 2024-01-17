#this creates a file path across operating systems
import os

# Reads CSV files
import csv

csvpath = os.path.join('budget_data.csv')
text_path = "output.txt"

total_months = 0
total_revenue = 0
revenue = []
previous_revenue = 0
greatest_decrease = ["", 9999999]
greatest_increase = ["",0]
revenue_change_list = []
revenue_average = 0
revenue_change = 0
month_of_change = []





#Opening the csv file
with open(csvpath) as csvfile:

    csvreader = csv.DictReader(csvfile)

    #Looping for total months
    for row in csvreader:
       
    #total months   
        total_months += 1
    #calculate total revenue
        total_revenue = total_revenue + int(row["Profit/Losses"])
    #average change
        revenue_change = float(row["Profit/Losses"]) - previous_revenue
        previous_revenue = float(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = [month_of_change] + [row["Date"]]

    #increase in revenue
        if revenue_change> greatest_increase[1]:
            greatest_increase[1] = revenue_change
            greatest_increase[0] = row['Date']

    #greatest decrease
        if revenue_change<greatest_decrease[1]:
            greatest_decrease[1] = revenue_change
            greatest_decrease[0] = row['Date']
    revenue_average = sum(revenue_change_list)/len(revenue_change_list)

with open(text_path, 'w') as file:
        file.write("Financial Analysis\n")
        file.write("--------------------\n")
        file.write("Total Months: %d\n" % total_months)
        file.write("Total $%d\n" % total_revenue)
        file.write("Average Change $%d\n" % revenue_average)
        file.write("Greatest Increase in Profits: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
        file.write("Greatest Decrease in Profits: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))






    
    
    
    






