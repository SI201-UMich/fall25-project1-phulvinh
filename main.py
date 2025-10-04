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
THIS IS HOW VARIABLES SHOULD BE FORMATTED
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
    ''' Function references the state column, the profit column, and the sales column'''
    
    #net profit margin = net profit / total sales
    total_sales = 0
    total_profit = 0
    
    #aggregating total sales and total profit for specific state
    for data in rows:
        if data["State"] == selected_state:
            total_profit += float(data["Profit"])
            total_sales += float(data["Sales"])
    
    #returning net profit margin at 2 decimal places rounded 
    return(f"The net profit margin for {selected_state} is {total_profit/total_sales * 100:.2f}%.")

def dict_of_city_and_revenue_per_city(rows, selected_state):
    #first step need to identify aggregate list of city before adding up sales
    list_of_city = []
    for data in rows:
        if data["State"] == selected_state:
            if data["City"] not in list_of_city:
                list_of_city.append(data["City"])
            else:
                continue
        else:
            continue
    
    #second step is to loop through each row and see if the data is in the list of city, then cherry pick to make a dictionary
    return_dict = {}
    for data in rows:
        if data["City"] in list_of_city:
            if data["City"] in return_dict.keys():
                return_dict[data["City"]] += float(data["Sales"])
            else:
                return_dict[data["City"]] = float(data["Sales"])
        else:
            continue
    print(f"The selected state of {selected_state} had these cities with these respective sales:")
    return(return_dict)

def write_result_of_net_profit_margin_to_txt(file_name, profit_margin_text):
    
    #open new text file taking in only file name and the string response from profit margin calculation function
    with open(file_name, "w") as new_file:
        new_file.write(profit_margin_text)
    return(None)

def write_result_of_dict_of_city_and_revenue_per_city_to_csv(file_name, city_revenue_dict):
    
    #open new csv file taking in new file name and pre writing the header of the file then looping through return dict to write rows
    with open(file_name, "w") as new_file:
        writer = csv.writer(new_file)
        writer.writerow(["City", "Total Sales"])
        for city, total_revenue in city_revenue_dict.items():
            writer.writerow([city, round(total_revenue, 2)])
    return(None)

def main():
    #identify file name then calling the read_data function to turn data into a readable and iterable list of dict representing rows
    file_name = "SampleSuperstore.csv"
    data = read_data(file_name)
    
    #calc 1: Net profit margin of all New York state shipment
    result_of_calculation_1 = net_profit_margin_per_selected_state(data,"New York")
    print(result_of_calculation_1)

    #calc 2: Total sales for categorize by each city within the Georgia state
    result_of_calculation_2 = dict_of_city_and_revenue_per_city(data, "Georgia")
    print(result_of_calculation_2)

    #write output to files
    write_result_of_net_profit_margin_to_txt("profit_margin_NY.txt", result_of_calculation_1)
    write_result_of_dict_of_city_and_revenue_per_city_to_csv("city_revenue_GA.csv", result_of_calculation_2)
    print("Results written to profit_margin_NY.txt and city_revenue_GA.csv")

if __name__ == "__main__":
    main()