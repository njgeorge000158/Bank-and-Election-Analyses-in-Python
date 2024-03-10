#*******************************************************************************************
 #
 #  File Name:  bank_main.py
 #
 #  File Description:
 #      This program, bank_main.py, reads budget data composed of two columns: 
 #      'Date' and 'Profit/Losses' from a csv file in the resources folder, 
 #      budget_data.csv.  The Python script takes the profit/loss records and 
 #      calculates each of the following values for the year (2023): the total 
 #      number of records in the data set, the net total amount of 'Profit/Losses', 
 #      the changes in 'Profit/Losses', the greatest increase in profits (date and 
 #      amount), and the greatest decrease in profits (date and amount).  In 
 #      addition, the program both prints the results to the terminal and exports it 
 #      to a text file in the analysis folder, budget_data.txt. 
 #   
 #      Here is a list of the functions and subroutines:
 #
 #      read_file_and_calculate_values
 #      write_data_to_terminal
 #      write_data_to_file
 #
 #
 #  Date            Description                             Programmer
 #  ----------      ------------------------------------    ------------------
 #  07/30/2023      Initial Development                     Nicholas J. George
 #
 #******************************************************************************************/

import csv
from enum import Enum


# This enumeration contains constant values for the input csv file's column indices.
class data_column_indices_enumeration(Enum):

    DATE_COLUMN_INDEX = 0

    PROFIT_LOSS_COLUMN_INDEX = 1


# This enumeration contains indices for the nested summary dictionary's keys.
class dictionary_indices_enumeration(Enum):

    TOTAL_RECORDS = 0

    TOTAL = 1

    AVERAGE_CHANGE = 2

    GREATEST_INCREASE_IN_PROFIT_LOSS = 3

    GREATEST_DECREASE_IN_PROFIT_LOSS = 4


    NESTED_DATA = 1

    DATE = 0

    VALUE = 1


# These constants are the names of the input and output file paths.
CONSTANT_INPUT_FILE_NAME = './resources/budget_data.csv'

CONSTANT_OUTPUT_FILE_NAME = './analysis/budget_data.txt'


# This constant is the title and tile line for the output data.
CONSTANT_OUTPUT_DATA_TITLE = 'Financial Analysis'

CONSTANT_OUTPUT_DATA_TITLE_LINE = '----------------------------'


#*******************************************************************************************
 #
 #  Subroutine Name:  read_file_and_calculate_values
 #
 #  Subroutine Description:
 #      This subroutine reads an input csv file and calculates the summary values
 #      for the program output.
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  7/30/2023           Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def read_file_and_calculate_values():

    # These variables contain the current and last profit/loss values 
    # as the program moves down the rows of input data.
    last_profit_loss_integer = 0


    # These variables contain the change in profit/loss pertaining to the current 
    # and last values versus the net change in profit/loss.
    current_changes_profit_loss_integer = 0

    net_changes_profit_loss_integer = 0


    #This line of code opens the csv file and returns a file object.
    with open(CONSTANT_INPUT_FILE_NAME) as csv_file:

        # This line of code reads the data from the file object and assigns 
        # it to a reader object.
        csv_reader = csv.reader(csv_file)

        # This repetition loop moves down the rows of data and calculates the values 
        # for the summary.
        for csv_index, csv_record in enumerate(csv_reader):

            # If the row index is equal to zero, the program takes no action because the first 
            # row of data is the header information.
            
            # If the row index is greater than one, these lines of code calculate the changes 
            # in profit/loss and update summary dictionary variables for the net total 
            # profit/loss, net total change in profit/loss, and dates and names for the
            # greatest increase and greatest decrease in profit/loss.
            if csv_index > 1: 

                # This line of code takes the current profit/loss value from the row of data 
                # and assigns it to a variable.
                current_profit_loss_integer \
                    = int \
                        (csv_record \
                            [data_column_indices_enumeration.PROFIT_LOSS_COLUMN_INDEX.value])

                # This line of code adds the current profit/loss to the summary dictionary
                # value for the net total profit/loss .
                summary_dictionary \
                    [list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL.value]] \
                        += current_profit_loss_integer


                # This line of code calculates the change in profit/loss and assigns it
                # to a variable.
                current_changes_profit_loss_integer \
                    = current_profit_loss_integer - last_profit_loss_integer

                # This line of code adds the current change in profit/loss to the net total 
                # change in profit/loss.
                net_changes_profit_loss_integer += current_changes_profit_loss_integer


                # This line of code assigns the current profit/loss value to the variable 
                # for the last profit/loss value for processing the next row.
                last_profit_loss_integer = current_profit_loss_integer


                # These lines of code check to see if the current increase in profit/loss 
                # is the greatest increase.  If it is, the program assigns the date and
                # value in the row of data to the appropriate summary dictionary variables.
                if current_changes_profit_loss_integer \
                   > summary_dictionary \
                        [list \
                            (summary_dictionary.keys()) \
                                    [dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]] \
                        [list \
                            (list \
                                (summary_dictionary.items()) \
                                        [dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value] \
                                        [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                [dictionary_indices_enumeration.VALUE.value]]:

                    summary_dictionary \
                        [list \
                            (summary_dictionary.keys()) \
                                [dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]] \
                                    [list \
                                        (list \
                                            (summary_dictionary.items()) \
                                                [dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value] \
                                                [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                        [dictionary_indices_enumeration.DATE.value]] \
                            = csv_record[data_column_indices_enumeration.DATE_COLUMN_INDEX.value]

                    summary_dictionary \
                        [list \
                            (summary_dictionary.keys()) \
                                [dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]] \
                                    [list \
                                        (list \
                                            (summary_dictionary.items()) \
                                                [dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value] \
                                                [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                        [dictionary_indices_enumeration.VALUE.value]] \
                            = current_changes_profit_loss_integer


                # These lines of code check to see if the current decrease in profit/loss 
                # is the greatest decrease.  If it is, the program assigns the date and
                # value to the appropriate summary dictionary variables.
                if current_changes_profit_loss_integer \
                    < summary_dictionary \
                        [list \
                            (summary_dictionary.keys()) \
                                [dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]] \
                                    [list \
                                        (list \
                                            (summary_dictionary.items()) \
                                                [dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value] \
                                                [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                            [dictionary_indices_enumeration.VALUE.value]]:
                    
                    summary_dictionary \
                        [list \
                            (summary_dictionary.keys()) \
                                [dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]] \
                                    [list \
                                        (list \
                                            (summary_dictionary.items()) \
                                                [dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value] \
                                                [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                            [dictionary_indices_enumeration.DATE.value]] \
                            = csv_record[data_column_indices_enumeration.DATE_COLUMN_INDEX.value]
                    
                    summary_dictionary \
                        [list \
                            (summary_dictionary.keys()) \
                                [dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]] \
                                    [list \
                                        (list \
                                            (summary_dictionary.items()) \
                                                [dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value] \
                                                [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                            [dictionary_indices_enumeration.VALUE.value]] \
                            = current_changes_profit_loss_integer


            # If the row index is equal to one, the program is looking at the first row 
            # of data, and there is change in profit/loss to calculate.
            elif csv_index == 1:

                # This line of code assigns the current profit/loss value in the data 
                # to the variable for the last profit/loss value, so the program can 
                # use it in the next iteration.
                last_profit_loss_integer \
                    = int(csv_record[data_column_indices_enumeration.PROFIT_LOSS_COLUMN_INDEX.value])
                

                # This line of code initializes the summary dictionary variable for net 
                # total profit/loss with the current protfit/loss value in the data.
                summary_dictionary \
                    [list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL.value]] \
                        = last_profit_loss_integer
    
    
    # This line of code assigns the row index in the iteration loop to the summary dictionary variable for the total 
    # number of months.
    summary_dictionary \
        [list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL_RECORDS.value]] \
            = csv_index


    # This line of code calculates the average change in profit/loss by taking the net changes in profit/loss 
    # and dividing it by the number of months minus one, because changes in profit/loss do not start until the 
    # second month when there is both a current and last value available.
    summary_dictionary \
        [list(summary_dictionary.keys())[dictionary_indices_enumeration.AVERAGE_CHANGE.value]] \
            = round \
                (float \
                    (net_changes_profit_loss_integer) \
                 / float \
                        (summary_dictionary \
                            [list(summary_dictionary.keys()) \
                                    [dictionary_indices_enumeration.TOTAL_RECORDS.value]] - 1), 2)


#*******************************************************************************************
 #
 #  Subroutine Name:  write_data_to_terminal
 #
 #  Subroutine Description:
 #      This subroutine writes the data in the summary dictionary to the terminal.
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  7/30/2023           Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def write_data_to_terminal():

    print()

    print(CONSTANT_OUTPUT_DATA_TITLE)

    print()

    print(CONSTANT_OUTPUT_DATA_TITLE_LINE)

    print()

    print(f'{list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL_RECORDS.value]}: ' \
          + f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL_RECORDS.value]]:,}')

    print()

    print(f'{list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL.value]}: ' \
          + f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL.value]]:,.2f} USD')

    print()

    print(f'{list(summary_dictionary.keys())[dictionary_indices_enumeration.AVERAGE_CHANGE.value]}: ' \
          + f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.AVERAGE_CHANGE.value]]:,.2f} USD')

    print()

    print(f'{list(summary_dictionary.keys())[dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]}: ' \
          + f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]][list(list(summary_dictionary.items())[dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value][dictionary_indices_enumeration.NESTED_DATA.value].keys())[dictionary_indices_enumeration.DATE.value]]} ' \
          + f'({summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]][list(list(summary_dictionary.items())[dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value][dictionary_indices_enumeration.NESTED_DATA.value].keys())[dictionary_indices_enumeration.VALUE.value]]: ,.2f} USD)')

    print()

    print(f'{list(summary_dictionary.keys())[dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]}: ' \
          + f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]][list(list(summary_dictionary.items())[dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value][dictionary_indices_enumeration.NESTED_DATA.value].keys())[dictionary_indices_enumeration.DATE.value]]} ' \
          + f'({summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]][list(list(summary_dictionary.items())[dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value][dictionary_indices_enumeration.NESTED_DATA.value].keys())[dictionary_indices_enumeration.VALUE.value]]:,.2f} USD)')

    print()


#*******************************************************************************************
 #
 #  Subroutine Name:  write_data_to_file
 #
 #  Subroutine Description:
 #      This subroutine writes the data in the summary dictionary to the output file.
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  7/30/2023           Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

def write_data_to_file():

    with open(CONSTANT_OUTPUT_FILE_NAME, 'w') as txt_file:
    
        txt_file.write('\n')

        txt_file.write(CONSTANT_OUTPUT_DATA_TITLE)

        txt_file.write('\n\n')

        txt_file.write(CONSTANT_OUTPUT_DATA_TITLE_LINE)

        txt_file.write('\n\n')

        txt_file.write(f'{list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL_RECORDS.value]}: ' \
                      + f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL_RECORDS.value]]}')

        txt_file.write('\n\n')
        
        txt_file.write(f'{list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL.value]}: ' \
                      + f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL.value]]:,.2f} USD')

        txt_file.write('\n\n')

        txt_file.write(f'{list(summary_dictionary.keys())[dictionary_indices_enumeration.AVERAGE_CHANGE.value]}: ' \
                      + f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.AVERAGE_CHANGE.value]]:.2f} USD')

        txt_file.write('\n\n')

        txt_file.write(f'{list(summary_dictionary.keys())[dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]}: ' \
                      + f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]][list(list(summary_dictionary.items())[dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value][dictionary_indices_enumeration.NESTED_DATA.value].keys())[dictionary_indices_enumeration.DATE.value]]} ' \
                      + f'({summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value]][list(list(summary_dictionary.items())[dictionary_indices_enumeration.GREATEST_INCREASE_IN_PROFIT_LOSS.value][dictionary_indices_enumeration.NESTED_DATA.value].keys())[dictionary_indices_enumeration.VALUE.value]]:,.2f} USD)')

        txt_file.write('\n\n')

        txt_file.write(f'{list(summary_dictionary.keys())[dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]}: ' \
                      + f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]][list(list(summary_dictionary.items())[dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value][dictionary_indices_enumeration.NESTED_DATA.value].keys())[dictionary_indices_enumeration.DATE.value]]} ' \
                      + f'({summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value]][list(list(summary_dictionary.items())[dictionary_indices_enumeration.GREATEST_DECREASE_IN_PROFIT_LOSS.value][dictionary_indices_enumeration.NESTED_DATA.value].keys())[dictionary_indices_enumeration.VALUE.value]]:,.2f} USD)')

        txt_file.write('\n')


#*******************************************************************************************
 #
 #  Subroutine Name: n/a
 #
 #  Subroutine Description:
 #      This is the main subroutine, the beginning and end of this program's execution.
 #
 #  Subroutine Parameters:
 #
 #  Type    Name            Description
 #  -----   -------------   ----------------------------------------------
 #  n/a     n/a             n/a
 #
 #
 #  Date                Description                                 Programmer
 #  ---------------     ------------------------------------        ------------------
 #  7/30/2023           Initial Development                         Nicholas J. George
 #
 #******************************************************************************************/

summary_dictionary \
     = {'Total Records': 0,
        'Total Profits': 0,
        'Average Change': 0.0,
        'Greatest Increase in Profits': {'Date': '', 'Value': 0 },
        'Greatest Decrease in Profits': {'Date': '', 'Value': 0 }}

read_file_and_calculate_values()

write_data_to_terminal()

write_data_to_file()
