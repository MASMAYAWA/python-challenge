import os
import csv
budget_csv = os.path.join('/Users/phuonglinh/Downloads/Bootcamp/Module-03/Challenge/python-challenge/PyBank/Resources/budget_data.csv')

selected_column_index = 1 
data = []

with open(budget_csv, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        header = next(csvreader)
        header.append('Change') 
    
        for row in csvreader:
                current_value = float(row[selected_column_index])
                previous_value = float(data[-1][selected_column_index]) if data else current_value
                change = current_value - previous_value

                row.append(change)
                data.append(row)

with open(budget_csv, 'w', newline='') as csvfile_new:
    writer = csv.writer(csvfile_new)
    writer.writerow(header)
    writer.writerows(data)

def budget(numbers):
    with open(budget_csv, 'r') as csvfile_new:

    
        csvreader = csv.reader(csvfile_new, delimiter=',')
        header = next(csvreader)  

    
        Total_Months = 0
        Total_Amount = 0
        Total_Change = 0
        Greatest_Increase = 0
        Greatest_Decrease = 0
       
                
        for row in csvreader:
                value = float(row[1])
                change = float(row[2])
        
                Total_Months += 1
                Total_Amount += value
                Total_Change += change
                Greatest_Increase = max(Greatest_Increase, change)

                Greatest_Decrease = min(Greatest_Decrease, change)
        Average_Amount = Total_Change / (Total_Months - 1)
    return Total_Months, Total_Amount, Greatest_Increase, Greatest_Decrease, Average_Amount 

Total_Months, Total_Amount, Greatest_Increase, Greatest_Decrease, Average_Amount = budget(budget_csv)
Average_Amount_rounded = round(Average_Amount, 2)


print(f'Financial Analysis')
print('----------------------------')
print(f'Total Months: {Total_Months}')
print(f'Total: ${Total_Amount}')
print(f'Average Change: ${Average_Amount_rounded}')
print(f'Greatest Increase in Profits: ${Greatest_Increase}')
print(f'Greatest Decrease in Profits: ${Greatest_Decrease}')