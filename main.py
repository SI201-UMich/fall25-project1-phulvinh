# SI 201 Project 1
# Your name: Phu Le
# Your student id: 10566445
# Your email: phule@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): ChatGPT
# Asked ChatGPT for debugging when needed, all code is original
# NOTE: I AM A STUDENT CURRENTLY ENROLLED IN SI 305, I AM USING PANDAS AND MATPLOTLIB HERE TO TRAIN MYSELF MORE
# ADDITIONAL NOTE: THE DATASET CHOSEN IS SAMPLE SUPERSTORE DATASET

#Importing dependencies
import math
import csv
import os
import unittest


'''
Variables
- Ship Mode: str()
- Segment: str()
- Country: str()
- City: str()
- State: str()
- Postal Code: int()
- Region: str()
- Category: str()
- Sub-Category: str()
- Sales: float()
'''

def read_data(file_name):
    #adding weird path sourcing method for vsc to find file
    source_directory = os.path.dirname(__file__)
    full_csv_file_path = os.path.join(source_directory, file_name)
    
    #creating a list to store the variety of dicts
    all_rows = []
    with open(full_csv_file_path, 'r') as file_handle:
        file_data = csv.DictReader(file_handle)

        #loop through each row
        for row in file_data:
            each_dict = {}
            
            #DictReader seperates each data according to column header and column data per row, need to finalize the dict and append
            for column_header, column_data in row.items():
                each_dict[column_header] = column_data
            all_rows.append(each_dict)

    return all_rows

def net_profit_margin_per_selected_state(rows, selected_state):
    #net profit margin = net profit / total sales
    total_sales = 0
    total_profit = 0
    
    #aggregating total sales and total profit for specific state
    for data in rows:
        if data["State"] == selected_state:
            total_profit += float(data["Profit"])
            total_sales += float(data["Sales"])
    
    #returning net profit margin at 2 decimal places rounded 
    return(f"{total_profit/total_sales * 100:.2f}%")

def main():
    file_name = "SampleSuperstore.csv"
    data = read_data(file_name)
    print(net_profit_margin_per_selected_state(data,"New York"))

if __name__ == "__main__":
    main()