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

def read_data(filename):
    source_dir = os.path.dirname(__file__)
    full_path = os.path.join(source_dir, filename)
    
    rows = []
    with open(full_path, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            clean_row = {k: v.strip() for k, v in row.items()}
            rows.append(clean_row)
    return rows

def main():
    file_name = "SampleSuperstore.csv"
    data = read_data(file_name)
    print(data)

if __name__ == "__main__":
    main()