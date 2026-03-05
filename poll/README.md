----

# **PyPoll: Automated Election Results Tabulation**

----

## **Overview**

This folder contains all files associated with the PyPoll Challenge. The core deliverable is `poll_main.py`, a Python script that reads raw polling data, tallies votes, and produces a complete breakdown of election results. The script modernizes and automates what would traditionally be a labor-intensive manual count, transforming a simple CSV file into a definitive electoral summary.

## **Data Source**

The input data is drawn from `election_data.csv`, located in the `resources` folder. The file contains three columns — `Voter ID`, `County`, and `Candidate` — with each row representing a single cast ballot.

## **Calculations**

From this data, the script derives five key electoral metrics:

- Total number of votes cast across the entire election
- A complete list of all candidates who received at least one vote
- Each candidate's percentage share of the total vote
- Each candidate's total raw vote count
- The winner of the election, determined by popular vote

## **Output**

Upon completing all calculations, the script delivers results in two formats simultaneously: a printed summary displayed in the terminal for immediate review, and an exported text file — `election_data.txt` — written to the `analysis` folder for official documentation and future reference.

----

## Copyright

Nicholas J. George © 2023. All Rights Reserved.
