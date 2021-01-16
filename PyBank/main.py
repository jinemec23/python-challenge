#The total number of months included in the dataset

#The net total amount of "Profit/Losses" over the entire period

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes

#The greatest increase in profits (date and amount) over the entire period

#The greatest decrease in losses (date and amount) over the entire period

# Import file
import os
import csv

# Set path
budget_data = os.path.join('Resources','budget_data.csv')

#Set variable lists
Date = []
Profit_Losses = []
net_total = 0
net_change = 0
max_profit_inc = ['',0]
max_loss_dec = ['',0]

# Use with open to read the file
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader,None)
    for row in csvreader:
        Date.append(row[0])
        pl_total = float(row[1])
        Profit_Losses.append(pl_total)
        net_total += pl_total

# Set loops to get data
total_months = len(Date)
for x in range(1,len(Date)):
    pl_change = Profit_Losses[x] - Profit_Losses[x-1]
    net_change += pl_change
    if pl_change > max_profit_inc[1]:
        max_profit_inc = [Date[x], pl_change]
    if pl_change < max_loss_dec[1]:
        max_loss_dec = [Date[x], pl_change]
average_change = net_change / total_months
greatest_increase = max_profit_inc

#Print PyBank Analysis
print('Financial Analysis')
print("------------------------")
print(f'Total Months: {int(total_months)}')
print(f'Total: ${int(net_total)}')
print(f'Average Change: ${str(round(average_change,2))}')
print(f'Greatest Increase in Profits: {(max_profit_inc[0])} (${int(max_profit_inc[1])})')
print(f'Greatest Decrease in Profits: {(max_loss_dec[0])} (${int(max_loss_dec[1])})')

#Export Results to txt file


Line1 ='Financial Analysis'
Line2 ="------------------------"
Line3 =str(f'Total Months: {int(total_months)}')
Line4 =str(f'Total: ${int(net_total)}')
Line5 =str(f'Average Change: ${str(round(average_change,2))}')
Line6 =str(f'Greatest Increase in Profits: {(max_profit_inc[0])} (${int(max_profit_inc[1])})')
Line7 =str(f'Greatest Decrease in Profits: {(max_loss_dec[0])} (${int(max_loss_dec[1])})')
line_summary = []
line_summary.extend([Line1,Line2,Line3,Line4,Line5,Line6,Line7])

output_file = os.path.join('Analysis','pybank_analysis.txt')
with open(output_file,"w", newline="") as textfile:
    for line in line_summary:
        textfile.write(line + '\n')
#textfile.writelines([Line1,Line2,Line3,Line4,Line5,Line6,Line7])