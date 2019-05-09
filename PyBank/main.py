# Imports
import os
import csv

# Read in CSV file
csvpath = os.path.join("budget_data22.csv")

# Create object "csvfile" from csvpath and open the object
with open (csvpath, newline="") as csvfile: 
    # take the csvfile object and add the interpreter (.reader()) function, then pass it to a variable
    csvreader = csv.reader(csvfile, delimiter=",")
    # take the first line out of the csvreader and assign it to a variable "csv_header"
    csv_header = next(csvreader)
    # check for first line in the file
    print(csv_header)

    # create a counter for month
    month = 0
    # make an empty list and assign values to variable "pl_list"
    pl_list = []
    # create a date list
    date_list = []
    # create a counter for profit & loss total and assign it to variable "pl_total" 
    pl_total = 0

    # loop through each row in csvreader
    for row in csvreader:
        # take the integer of the second column in each row of csvreader and assign it to variable "pl"
        pl = int(row[1])
        # immediately take the value from pl and append it to pl_list
        pl_list.append(pl)
        # increment the varible "month" by one (1)
        month +=1
        # increment the pl_total list by the current row and second column's integer value
        pl_total += pl
        # take the string of the first column in each row of csvreader and assign it to variable "date"
        date = str(row[0]) 
        # immediately take the value from date and append it to date_list
        date_list.append(date)
        
    # calculate the statistics 
    # create container for total change in P&L
    change_total = 0
    # create list to contain change values
    deltas = []
    # find the length of pl_list, loop through pl_list to count up the values
    for i in range(len(pl_list)-1):
        # find the difference between next value and current value
        change = pl_list[i+1] - pl_list[i]
        # take the value of change and append it to the deltas list
        deltas.append(change)
        # increment change_total counter by current change value
        change_total += change
        
    # test = len(deltas)
    # print(f"test: {test}") 

    # calculate greatest profit in/decrease
    # find the max value in the deltas
    greatest_gain_delta = max(deltas)
    # find location of max value (greatest gain delta location) in deltas list
    ggd_location = deltas.index(greatest_gain_delta)
    
    # find the min value in the deltas
    greatest_loss_delta = min(deltas)
    # # find location of min value (greatest loss delta location) in deltas list
    gld_location = deltas.index(greatest_loss_delta)

    # use the ggd_location index to cross reference the original csv file and return corresponding date
    ggd_date = date_list[ggd_location + 1]

    # use the gld_location index to cross reference the original csv file and return corresponding date
    gld_date = date_list[gld_location + 1]
    
    
    
    
    print(f"Financial Analysis")
    print(f"------------------------------------------")
    print(f"Total Months: {month}")
    print(f"Total P&L: ${pl_total}")
    print(f"Average Change: ${round((change_total/month), 2)}")
    print(f"Greatest Increase in Profits: {ggd_date} (${greatest_gain_delta})")
    print(f"Greatest Decrease in Profits: {gld_date} (${greatest_loss_delta})")
   