__author__ = 'rakesh'

import csv

with open('test.csv','r') as csvfile: # input csv file
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        print row[-1]




