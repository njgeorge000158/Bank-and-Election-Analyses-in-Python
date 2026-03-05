![bank_and_election_analyses](https://github.com/njgeorge000158/Bank-and-Election-Analyses-in-Python/assets/137228821/37fb5c30-c051-4ed5-af80-6ea34480914a)

----

# **Python-Driven Financial and Electoral Analysis: PyBank and PyPoll**

----

## **Project Overview**

For this project, I developed two independent Python scripts to automate the analysis of financial and electoral data. Though distinct in purpose, both scripts share a common design philosophy: they are built to be versatile and reusable, capable of processing any dataset formatted consistently with their respective inputs — not just the specific files used here.

## **PyBank: Corporate Profit and Loss Analysis**

The first script, `bank_main.py`, analyzes a single year of profit and loss records for one company. The source data — housed in `budget_data.csv` within the Resources folder — contains 86 months of financial entries for the fiscal year 2023. The script reads this file and automatically computes the following metrics:

- **Total months in the dataset:** 86
- **Net profit/loss over the entire period:** $22,564,198
- **Average month-over-month change:** -$8,311.11
- **Greatest single-month increase:** $1,862,002 on August 16, 2023
- **Greatest single-month decrease:** -$1,825,558 on February 14, 2023

The results reveal a company that, despite generating a substantial net profit over the year, experienced notable volatility in its monthly performance — with a swing of nearly $3.7 million between its best and worst months. The negative average month-over-month change further suggests that, while the company remained profitable in aggregate, its financial momentum trended slightly downward across the period.

## **PyPoll: Municipal Election Vote Tabulation**

The second script, `poll_main.py`, was developed to modernize the vote-counting process for a small rural town. Drawing from `election_data.csv` in the Resources folder, the script tallies votes across the full election dataset and produces a complete breakdown of results:

- **Total votes cast:** 369,711
- **Candidates and results:**

| Candidate | Votes | Share |
|---|---|---|
| Diana DeGette | 272,892 | 73.81% |
| Charles Casper Stockham | 85,213 | 23.05% |
| Raymon Anthony Doane | 11,606 | 3.14% |

- **Winner by popular vote:** Diana DeGette

DeGette's victory was decisive, capturing nearly three-quarters of all votes cast — more than three times the share of her nearest competitor. The margin leaves no ambiguity in the outcome.

**Versatility and Extensibility**

Both scripts are designed with flexibility in mind. PyBank can process profit and loss records from any company or time period, provided the data follows the same CSV structure. PyPoll is equally adaptable: it can handle elections with any number of candidates, including write-in entries, and is equipped to identify and announce tied outcomes — making it a practical tool for a range of real-world electoral scenarios.

----

## Copyright

Nicholas J. George © 2023. All Rights Reserved.
