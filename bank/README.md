----

# **PyBank: Automated Profit and Loss Analysis**

----

## **Overview**

This folder contains all files associated with the PyBank challenge. The centerpiece is `bank_main.py`, a Python script that reads, processes, and summarizes a company's profit and loss records for the fiscal year 2023. The script is designed to automate what would otherwise be a tedious manual calculation, producing a clean, structured financial summary from raw transactional data.

## **Data Source**

The input data resides in `budget_data.csv`, located in the `resources` folder. The file contains two columns — `Date` and `Profit/Losses` — with each row representing a single monthly financial record for the company.

## **Calculations**

From this data, the script computes five key financial metrics:

- Total number of records in the dataset
- Net total profit and loss over the entire period
- Average month-over-month change in profit and loss
- Greatest single-period increase in profits, including the date and amount
- Greatest single-period decrease in profits, including the date and amount

## **Output**

Once all calculations are complete, the script delivers results in two formats simultaneously: a printed summary displayed directly in the terminal for immediate review, and an exported text file — `budget_data.txt` — written to the `analysis` folder for documentation and future reference.

----

## Copyright

Nicholas J. George © 2023. All Rights Reserved.
