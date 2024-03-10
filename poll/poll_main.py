#*******************************************************************************************
 #
 #  File Name:  poll_main.py
 #
 #  File Description:
 #      This program takes a poll data set from a CSV file in the resources folder, 
 #      election_data.csv, composed of three columns: "Voter ID", "County", and 
 #      "Candidate".  This Python script analyzes the votes and calculates each 
 #      of the following values: the total number of votes cast, a complete list 
 #      of candidates who received votes, the percentage of votes each candidate 
 #      won, the total number of votes each candidate won, and the winner of the 
 #      election based on the popular vote.  In addition, the program both prints 
 #      the analysis to the terminal and exports the results to a text file, 
 #      election_data.txt, in the analysis folder.
 #
 #      Here is a List of subroutines and functions:
 #
 #      calculate_candidate_percentages
 #      determine_winner
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


# This enumeration contains indices for the input csv file's columns.
class data_column_indices_enumeration(Enum):

    BALLOT_ID_INDEX = 0

    COUNTY_INDEX = 1

    CANDIDATE_INDEX = 2


# This enumeration contains indices for the nested summary dictionary's keys.
class dictionary_indices_enumeration(Enum):

    TOTAL_VOTES = 0

    CANDIDATES = 1

    WINNER = 2


    NESTED_DATA = 1

    NAME = 0

    PERCENT = 1

    VOTE_COUNT = 2


# These constants are the names of the input and output file paths.
CONSTANT_INPUT_FILE_NAME = './resources/election_data.csv'

CONSTANT_OUTPUT_FILE_NAME = './analysis/election_data.txt'


# These constants are the title and tile line for the output data.
CONSTANT_OUTPUT_DATA_TITLE = 'Election Results'

CONSTANT_OUTPUT_DATA_TITLE_LINE = '----------------------------'


# This constant is the program's message if there is a tie for the winner.
CONSTANT_CANDIDATE_TIE_MESSAGE = 'There is no winner: the election is a tie!'


#*******************************************************************************************
 #
 #  Subroutine Name:  calculate_candidate_percentages()
 #
 #  Subroutine Description:
 #      This subroutine calculates each candidate's percentage of the total vote based 
 #      on the candidate's vote count and the total vote count.  The program assigns 
 #      the calculated percentage to the summary dictionary's candidate percent list.
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

def calculate_candidate_percentages():

    temp_percent_float = 0.0

    for candidate_index, candidate_name \
        in enumerate \
                (summary_dictionary \
                    [list \
                        (summary_dictionary.keys()) \
                            [dictionary_indices_enumeration.CANDIDATES.value]] \
                    [list \
                        (list \
                            (summary_dictionary.items()) \
                                [dictionary_indices_enumeration.CANDIDATES.value] \
                                [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                    [dictionary_indices_enumeration.NAME.value]]):
        
        temp_percent_float \
            = round \
                ((summary_dictionary \
                    [list \
                        (summary_dictionary.keys()) \
                                [dictionary_indices_enumeration.CANDIDATES.value]] \
                    [list \
                        (list \
                            (summary_dictionary.items()) \
                                [dictionary_indices_enumeration.CANDIDATES.value] \
                                [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                    [dictionary_indices_enumeration.VOTE_COUNT.value]] \
                                        [candidate_index] \
                     / summary_dictionary \
                            [list \
                                (summary_dictionary.keys()) \
                                    [dictionary_indices_enumeration.TOTAL_VOTES.value]]) * 100, 3)
        
        summary_dictionary \
            [list \
                (summary_dictionary.keys()) \
                    [dictionary_indices_enumeration.CANDIDATES.value]] \
            [list \
                (list \
                    (summary_dictionary.items()) \
                        [dictionary_indices_enumeration.CANDIDATES.value] \
                        [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                            [dictionary_indices_enumeration.PERCENT.value]] \
            .append (temp_percent_float)
        

#*******************************************************************************************
 #
 #  Subroutine Name:  determine_winner()
 #
 #  Subroutine Description:
 #      This subroutine compares each candidate's vote count to find the winner of the
 #      election and, also, checks for a tie.
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

def determine_winner():

    # This variable tells the program whether a tie has occurred between two or more winning 
    # candidates.
    candidate_tie_boolean = False

    # This variable holds the winning candidate's nested index in the summary dictionary.
    winner_index_integer = 0

    # This variable holds the winning candidate's vote count.
    winner_vote_count_integer = 0 


    # This repetiton loop starts with the first candidate then looks for another candidate 
    # with a greater vote count. 
    for candidate_index, candidate_name \
        in enumerate \
            (summary_dictionary \
                [list \
                    (summary_dictionary.keys()) \
                        [dictionary_indices_enumeration.CANDIDATES.value]] \
                [list \
                    (list \
                        (summary_dictionary.items()) \
                            [dictionary_indices_enumeration.CANDIDATES.value] \
                            [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                [dictionary_indices_enumeration.NAME.value]]):
        
        # The program compares vote counts to determine the greatest one and stores the winning 
        # candidate's index and vote count in the appropriate variables.
        if candidate_index > 0:

            if winner_vote_count_integer \
                < summary_dictionary \
                    [list \
                        (summary_dictionary.keys()) \
                            [dictionary_indices_enumeration.CANDIDATES.value]] \
                                [list \
                                    (list \
                                        (summary_dictionary.items()) \
                                            [dictionary_indices_enumeration.CANDIDATES.value] \
                                            [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                                [dictionary_indices_enumeration.VOTE_COUNT.value]] \
                                [candidate_index]:
            
                winner_vote_count_integer \
                    = summary_dictionary \
                        [list \
                            (summary_dictionary.keys()) \
                                [dictionary_indices_enumeration.CANDIDATES.value]] \
                                    [list \
                                        (list \
                                            (summary_dictionary.items()) \
                                                [dictionary_indices_enumeration.CANDIDATES.value] \
                                                [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                                    [dictionary_indices_enumeration.VOTE_COUNT.value]] \
                                    [candidate_index]
            
                winner_index_integer = candidate_index
       

        # The program initializes the vote count variable with the first candidate's vote count; 
        # the index is already initialized to the first candidate upon declaration.
        else:

            winner_vote_count_integer \
                = summary_dictionary \
                    [list \
                        (summary_dictionary.keys()) \
                            [dictionary_indices_enumeration.CANDIDATES.value]] \
                        [list \
                            (list \
                                (summary_dictionary.items()) \
                                    [dictionary_indices_enumeration.CANDIDATES.value] 
                                    [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                        [dictionary_indices_enumeration.VOTE_COUNT.value]] \
                        [candidate_index]


    # The program now takes the winning candidate's vote count and compares it to the other candidate's 
    # vote counts.  If there is a match, the program changes the Boolean flag value to true and writes 
    # a message to the appropriate summary dictionary variable before exiting the iteration loop.
    for candidate_index, candidate_name \
        in enumerate \
            (summary_dictionary \
                [list \
                    (summary_dictionary.keys()) \
                        [dictionary_indices_enumeration.CANDIDATES.value]] \
                [list \
                    (list \
                        (summary_dictionary.items()) \
                            [dictionary_indices_enumeration.CANDIDATES.value] \
                            [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                [dictionary_indices_enumeration.NAME.value]]):
  
        if winner_vote_count_integer \
            == summary_dictionary \
                    [list \
                        (summary_dictionary.keys()) \
                            [dictionary_indices_enumeration.CANDIDATES.value]] \
                                [list \
                                    (list \
                                        (summary_dictionary.items()) \
                                            [dictionary_indices_enumeration.CANDIDATES.value] \
                                            [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                                [dictionary_indices_enumeration.VOTE_COUNT.value]] \
                                [candidate_index] \
            and candidate_index != winner_index_integer:

            candidate_tie_boolean = True

            summary_dictionary \
                [list \
                    (summary_dictionary.keys()) \
                        [dictionary_indices_enumeration.WINNER.value]] = CONSTANT_CANDIDATE_TIE_MESSAGE
            
            break

    
    # If there is no tie, the program writes the winning candidate's name to the appropriate summary 
    # dictionary variable.
    if candidate_tie_boolean == False:
        
        summary_dictionary \
            [list \
                (summary_dictionary.keys()) \
                    [dictionary_indices_enumeration.WINNER.value]] \
            = summary_dictionary \
                [list \
                    (summary_dictionary.keys()) \
                        [dictionary_indices_enumeration.CANDIDATES.value]] \
                            [list \
                                (list \
                                    (summary_dictionary.items()) \
                                        [dictionary_indices_enumeration.CANDIDATES.value] \
                                            [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                                [dictionary_indices_enumeration.NAME.value]] \
                            [winner_index_integer]


#*******************************************************************************************
 #
 #  Subroutine Name:  read_file_and_calculate_values
 #
 #  Subroutine Description:
 #      This subroutine reads the input csv file and calculates the summary values needed 
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

    # This variable is the candidate's name from the current row of data.
    current_candidate_name_string \
        = ''

    # This variable is a Boolean flag that tells the program that it has encountered
    # a new candidate in the data.
    candidate_found_boolean \
        = False


    #This line of code opens the csv file and returns a file object.
    with open(CONSTANT_INPUT_FILE_NAME) as csv_file:

        # This line of code reads the data from the file object and assigns 
        # it to a reader object.
        csv_reader = csv.reader(csv_file)


        # This repetition loop moves down the rows of data and calculates the values 
        # for the summary.
        for csv_index, csv_record in enumerate(csv_reader):
   
            # If the row index is equal to zero, the program takes no action because the 
            # first row of data is the header information.
            
            # If the row index is greater than one, the program increments vote counts 
            # and looks for new candidates.
            if csv_index > 1: 
                
                # This line of code assigns the current candidate's name to the appropriate 
                # variable.
                current_candidate_name_string \
                    = csv_record \
                            [data_column_indices_enumeration.CANDIDATE_INDEX.value]
                
                # This line of code initializes the Boolean flag to False for processing.
                candidate_found_boolean \
                    = False


                # This repetition loop looks at all the existing candidates in the summary 
                # dictionary.
                for candidate_index, candidate_name \
                    in enumerate \
                        (summary_dictionary \
                            [list \
                                (summary_dictionary.keys()) \
                                    [dictionary_indices_enumeration.CANDIDATES.value]] \
                            [list \
                                (list \
                                    (summary_dictionary.items()) \
                                        [dictionary_indices_enumeration.CANDIDATES.value] \
                                        [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                            [dictionary_indices_enumeration.NAME.value]]):
                
                    # If the program finds the current candidate in the summary dictionary, it 
                    # increments the candidate's vote count, sets the Boolean flag to True, 
                    # and exits the repetition loop.
                    if candidate_name == current_candidate_name_string:
                        
                        summary_dictionary \
                            [list \
                                (summary_dictionary.keys()) \
                                    [dictionary_indices_enumeration.CANDIDATES.value]] \
                            [list \
                                (list \
                                    (summary_dictionary.items()) \
                                        [dictionary_indices_enumeration.CANDIDATES.value] \
                                        [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                            [dictionary_indices_enumeration.VOTE_COUNT.value]] \
                            [candidate_index] \
                                += 1
                        
                        candidate_found_boolean = True
                        
                        break
                

                # If the program did not find the current candidate in the summary dictionary, 
                # it adds the candidate and sets the vote count to one.
                if candidate_found_boolean == False:

                    summary_dictionary \
                        [list \
                            (summary_dictionary.keys()) \
                                [dictionary_indices_enumeration.CANDIDATES.value]] \
                        [list \
                            (list \
                                (summary_dictionary.items()) \
                                    [dictionary_indices_enumeration.CANDIDATES.value] \
                                    [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                        [dictionary_indices_enumeration.NAME.value]] \
                        .append(current_candidate_name_string)
                    
                    summary_dictionary \
                        [list \
                            (summary_dictionary.keys()) \
                                [dictionary_indices_enumeration.CANDIDATES.value]] \
                        [list \
                            (list \
                                (summary_dictionary.items()) \
                                    [dictionary_indices_enumeration.CANDIDATES.value] \
                                    [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                        [dictionary_indices_enumeration.VOTE_COUNT.value]] \
                        .append(1)


            # If the row index is equal to one, the Python script adds the first candidate to the summary 
            # dictionary and sets his/her vote count to one.
            elif csv_index == 1:

                current_candidate_name_string \
                    = csv_record[data_column_indices_enumeration.CANDIDATE_INDEX.value]

                summary_dictionary \
                    [list \
                        (summary_dictionary.keys()) \
                            [dictionary_indices_enumeration.CANDIDATES.value]] \
                    [list \
                        (list \
                            (summary_dictionary.items()) \
                                [dictionary_indices_enumeration.CANDIDATES.value] \
                                [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                    [dictionary_indices_enumeration.NAME.value]] \
                    .append(current_candidate_name_string)
               
                summary_dictionary \
                    [list \
                        (summary_dictionary.keys()) \
                            [dictionary_indices_enumeration.CANDIDATES.value]] \
                    [list \
                        (list \
                            (summary_dictionary.items()) \
                                [dictionary_indices_enumeration.CANDIDATES.value] \
                                [dictionary_indices_enumeration.NESTED_DATA.value].keys()) \
                                    [dictionary_indices_enumeration.VOTE_COUNT.value]] \
                    .append(1)
    

    # This line of code takes the counter from the repetition loop and assigns its value to the summary 
    # dictionary's total votes variable.
    summary_dictionary \
        [list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL_VOTES.value]] \
            = csv_index


    calculate_candidate_percentages()

    determine_winner()


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

    print(f'{list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL_VOTES.value]}:' \
          + f' {summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL_VOTES.value]]:,}')

    print()

    print(CONSTANT_OUTPUT_DATA_TITLE_LINE)

    print()


    for candidate_index, candidate_name in enumerate(summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.CANDIDATES.value]]):
        
        print(f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.CANDIDATES.value]][list(list(summary_dictionary.items())[dictionary_indices_enumeration.CANDIDATES.value][dictionary_indices_enumeration.NESTED_DATA.value].keys())[dictionary_indices_enumeration.NAME.value]][candidate_index]}:' \
              + f' {summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.CANDIDATES.value]][list(list(summary_dictionary.items())[dictionary_indices_enumeration.CANDIDATES.value][dictionary_indices_enumeration.NESTED_DATA.value].keys())[dictionary_indices_enumeration.PERCENT.value]][candidate_index]:,.2f}%' \
              + f' ({summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.CANDIDATES.value]][list(list(summary_dictionary.items())[dictionary_indices_enumeration.CANDIDATES.value][dictionary_indices_enumeration.NESTED_DATA.value].keys())[dictionary_indices_enumeration.VOTE_COUNT.value]][candidate_index]:,})')
        
        print()


    print(CONSTANT_OUTPUT_DATA_TITLE_LINE)

    print()

    print(f'{list(summary_dictionary.keys())[dictionary_indices_enumeration.WINNER.value]}: ' \
          + f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.WINNER.value]]}')

    print()

    print(CONSTANT_OUTPUT_DATA_TITLE_LINE)

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

        txt_file.write(f'{list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL_VOTES.value]}: ' \
                      + f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.TOTAL_VOTES.value]]:,}')

        txt_file.write('\n\n')

        txt_file.write(CONSTANT_OUTPUT_DATA_TITLE_LINE)

        txt_file.write('\n\n')


        for candidate_index, candidate_name in enumerate(summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.CANDIDATES.value]]):
            
            txt_file.write(f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.CANDIDATES.value]][list(list(summary_dictionary.items())[dictionary_indices_enumeration.CANDIDATES.value][dictionary_indices_enumeration.NESTED_DATA.value].keys())[dictionary_indices_enumeration.NAME.value]][candidate_index]}: ' \
                          + f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.CANDIDATES.value]][list(list(summary_dictionary.items())[dictionary_indices_enumeration.CANDIDATES.value][dictionary_indices_enumeration.NESTED_DATA.value].keys())[dictionary_indices_enumeration.PERCENT.value]][candidate_index]:,.2f}% ' \
                          + f'({summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.CANDIDATES.value]][list(list(summary_dictionary.items())[dictionary_indices_enumeration.CANDIDATES.value][dictionary_indices_enumeration.NESTED_DATA.value].keys())[dictionary_indices_enumeration.VOTE_COUNT.value]][candidate_index]:,})')
            
            txt_file.write('\n\n')


        txt_file.write(CONSTANT_OUTPUT_DATA_TITLE_LINE)

        txt_file.write('\n\n')

        txt_file.write(f'{list(summary_dictionary.keys())[dictionary_indices_enumeration.WINNER.value]}: ' \
                      + f'{summary_dictionary[list(summary_dictionary.keys())[dictionary_indices_enumeration.WINNER.value]]}')

        txt_file.write('\n\n')

        txt_file.write(CONSTANT_OUTPUT_DATA_TITLE_LINE)

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
    = {'Total Votes': 0,
       'Candidates': {'Name': [], 'Percent': [], 'Vote Count': []},
       'Winner' : ''}

read_file_and_calculate_values()

write_data_to_terminal()

write_data_to_file()
