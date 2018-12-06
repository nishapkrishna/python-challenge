import os
import csv
#files to input and output
input_file = os.path.join('budget_data.csv')
output_file = os.path.join('budget_data_Output.txt')

month = []
profit_loss = []
#read the csv and convert it into a list of dictionaries
with open(input_file,'r') as csvfile:
    reader = csv.DictReader(csvfile)
#Find all the months and all the "Profit/Losses"
    for row in reader:
        month.append(row['Date'])
        profit_loss.append(int(row['Profit/Losses']))
#Find the total months and total net amount of "Profit/Losses"
total_months = len(month)
increase_profit = profit_loss[0]
decrease_loss = profit_loss[0]
total_proloss = 0
difference = 0
#Find the greatest increase/decrease in profits (date and amount) over the entire period
for i in range(len(profit_loss)):
    if profit_loss[i] >= increase_profit: 
        increase_profit = profit_loss[i]
        increase_month = month[i]
        increase_value = increase_profit - profit_loss[i-1] 
    if profit_loss[i] <= decrease_loss: 
        decrease_loss = profit_loss[i]
        decrease_month = month[i]
        decrease_value = decrease_loss - profit_loss[i-1] 
    total_proloss = total_proloss + profit_loss[i]  
#Find the average change in "Profit/Losses" between months over the entire period
    if i > 0:
        difference = difference + (profit_loss[i] - profit_loss[i-1])
average_change = difference / (total_months-1)

#open output and write to text file
with open(output_file,'w') as txt_write:
    txt_write.write("Financial Analysis" + '\n')
    txt_write.write("------------------" + '\n')
    txt_write.write("Total months : " + str(total_months) + '\n')
    txt_write.write("Total net amount of Profit/Losses : " +"$" + str(total_proloss) + '\n')
    txt_write.write("Average  Change : " + "$" +str(average_change) + '\n')
    txt_write.write("Greatest Increase in Profits : " + increase_month + " ($"+(str(increase_value))+")" + '\n')
    txt_write.write("Greatest Decrease in Profits : " + decrease_month + " ($"+(str(decrease_value))+")" +'\n')    
#open output and write to terminal
with open (output_file, 'r') as outfile:
    print(outfile.read())


