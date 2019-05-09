# Imports
import os
import csv

# Read in CSV file
csvpath = os.path.join("election_data.csv")

# Create object "csvfile" from csvpath and open the object
with open (csvpath, newline="") as csvfile: 
    # take the csvfile object and add the interpreter (.reader()) function, then pass it to a variable
    csvreader = csv.reader(csvfile, delimiter=",")
    # take the first line out of the csvreader and assign it to a variable "csv_header"
    csv_header = next(csvreader)
    # check for first line in the file
    print(csv_header)

    # create counter for total_votes
    total_votes = 0

    # make a list of candidates
    gross_candidate_list = []
    unique_candidates = []
    li = []
    otooley = []
    correy = []
    khan = []
    
    garbage = []

    # list of candidate names as a variable
    l = "Li"
    o = "O'Tooley"
    c = "Correy"
    k = "Khan"

    # loop through each row and grab candidate's name and add names to gross candidate list
    for row in csvreader:
        candidate_name = str(row[2])
        gross_candidate_list.append(candidate_name)
    
    # pull out the unique values from gross candidate list and add unique values to unique candidate list
    unique_candidate_list = set(gross_candidate_list)
    unique_candidate_list = list(unique_candidate_list) 
    unique_candidates.append(unique_candidate_list)
   
    li_votes = gross_candidate_list.count("Li")
    otooley_votes = gross_candidate_list.count("O'Tooley")
    correy_votes = gross_candidate_list.count("Correy")
    khan_votes = gross_candidate_list.count("Khan")
    total_votes = li_votes + otooley_votes + correy_votes + khan_votes 

    # calculate percentages
    li_percent = li_votes / total_votes
    otooley_percent = otooley_votes / total_votes
    correy_percent = correy_votes / total_votes
    khan_percent = khan_votes / total_votes

    # find winner
    winner = max([(gross_candidate_list.count(chr),chr) for chr in set(gross_candidate_list)])
    

    # print(otooley_percent) 

    # print(li_votes)
    # print(otooley_votes)
    # print(correy_votes)
    # print(khan_votes)

    print(f"Election Results")
    print(f"----------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"----------------------------------")
    print(f"{k}: {khan_percent:.3%} ({khan_votes})")
    print(f"{c}: {correy_percent:.3%} ({correy_votes})")
    print(f"{l}: {li_percent:.3%} ({li_votes})")
    print(f"{o}: {otooley_percent:.3%} ({otooley_votes})")
    print(f"----------------------------------")
    print(f"Winner: {winner}")
    print(f"----------------------------------")



   




    



