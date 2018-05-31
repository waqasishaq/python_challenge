import csv


pypollfile1 = "election_data_1.csv"


Vote_count = 0
total_candidates = 0
candidate_options = []
candidate_votes = {}

with open(pypollfile1) as file_data:
    reader = csv.DictReader(file_data)
# loop through the rows of CSV file  and count the votes
    for row in reader:

        Vote_count = Vote_count + 1

        total_candidates = row["Candidate"]

        if row["Candidate"] not in candidate_options:
            candidate_options.append(row["Candidate"])
            candidate_votes[row["Candidate"]] = 1

        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

    print()

    print("Election Results")
    print("--------------------------------------")
    print("Total Votes " + str(Vote_count))
    print("--------------------------------------")
   
    
    for candidate in candidate_votes:

        print(candidate + " " + str(round(((candidate_votes[candidate]/Vote_count)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
        
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/Vote_count)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 

# finding winner_votes

winner = max(candidate_votes.items(),key=lambda x: len(x))

print("--------------------------------------")
print ("Winner : " + str(winner[0]))
print("--------------------------------------")


# Output Files

file_to_output = "election_analysis_1.txt"

with open(file_to_output, "w") as txt_file:
        txt_file.write("Election Results")
        txt_file.write("\n")
        txt_file.write("-------------------------------")
        txt_file.write("\n")
        txt_file.write("Total Votes " + str(Vote_count))
        txt_file.write("\n")
        txt_file.write("-------------------------------")
        txt_file.write("\n")
        
        for candidate in candidate_votes:
            
            txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/Vote_count)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
            txt_file.write("\n")
        

        txt_file.write("-----------------------------------------------")
        txt_file.write("\n")
        txt_file.write("Winner: " + str(winner[0]))
        txt_file.write("\n")
        txt_file.write("-----------------------------------------------")
        

        