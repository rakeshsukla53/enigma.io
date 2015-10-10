__author__ = 'rakesh'

import csv

with open('solution.csv', 'wb') as f: # output csv file
    writer = csv.writer(f)
    with open('state_abbreviations.csv','r') as csvfile: # input csv file
        reader = csv.reader(csvfile, delimiter=',')
        count = 0
        for row in reader:
            row[0] = row[1]  #replacing each state abbreviation with its associate state name
            writer.writerow(row) #write to the solution file
f.close()

