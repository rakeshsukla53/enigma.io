__author__ = 'rakesh'

import csv

with open('solution.csv', 'wb') as f: # output csv file
    writer = csv.writer(f)
    with open('test.csv','r') as csvfile: # input csv file
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            row[8] = " ".join(row[8].split()).strip()  #removing extra spaces from the string
            writer.writerow(row) #writing to a new file
f.close()










