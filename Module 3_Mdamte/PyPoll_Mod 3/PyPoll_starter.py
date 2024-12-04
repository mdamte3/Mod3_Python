
# import csv and os files
import csv
import os   # os allows for path manipulation across operating systems


# Files 
# input file path
file_to_load = os.path.join("Resources", "election_data.csv")  
# output file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  


# name Variables 
total_votes = 0
candidates = {}  
winner = ""
winning_votes = 0


# CSV File
with open(file_to_load) as election_data:
    csvreader = csv.reader(election_data)
    
    # Header row
    header = next(csvreader)
    
    # Data row
    for row in csvreader:
        
        # total votes_count
        total_votes += 1
        
        # Candidate Name
        candidate = row[2]
        
        # Dictionary: Add candidate
        if candidate not in candidates:
            candidates[candidate] = 0
        
        # Candidate: Add to count
        candidates[candidate] += 1

# winner_ candidate with the most votes
for candidate in candidates:
    votes = candidates[candidate]
    if votes > winning_votes:
        winning_votes = votes
        winner = candidate

# output summary
output = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n"
)

# candidate results_ output
for candidate in candidates:
    votes = candidates[candidate]
    vote_percentage = float(votes) / float(total_votes) * 100
    output += f"{candidate}: {vote_percentage:.3f}% ({votes:,})\n"

# winner_display in output
output += (
    f"-------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------\n"
)

# display results of candidates
print(output)

# results to a text file
with open(file_to_output, "w") as txt_file:    
    txt_file.write(output)          







"""





# -*- coding: UTF-8 -*-


# Import necessary modules
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "election_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "election_analysis.txt")  # Output file path

# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts


# Winning Candidate and Winning Count Tracker


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row


        # Get the candidate's name from the row


        # If the candidate is not already in the candidate list, add them


        # Add a vote to the candidate's count


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)


    # Write the total vote count to the text file


    # Loop through the candidates to determine vote percentages and identify the winner


        # Get the vote count and calculate the percentage


        # Update the winning candidate if this one has more votes


        # Print and save each candidate's vote count and percentage


    # Generate and print the winning candidate summary


    # Save the winning candidate summary to the text file
"""