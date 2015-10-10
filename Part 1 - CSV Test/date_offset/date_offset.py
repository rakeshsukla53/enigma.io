__author__ = 'rakesh'

import csv
from dateutil.parser import parse
import re

f = open('solution.csv', 'wb')  #output solution file
writer = csv.writer(f)
count = 0
with open('test.csv','r') as csvfile: # input csv file
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        if count == 0:
            row.append('start_date_description')
            writer.writerow(row) #first row of the file
            count += 1
        else:
            date = re.match(r'[a-zA-Z]+\W[0-9]+,\W[0-9]+|[0-9]{4}-[0-9]{2}-[0-9]{2}|[0-9]{2}/[0-9]{2}/[0-9]{4}', str(row[-1]))
            #filter out invalid date using a regular expression
            if date:
                dt = parse(date.group())
                row[10] = (dt.strftime('%Y-%m-%d')) #converting datefield into ISO format
            else:
                row.append(str(row[-1]))
                row[10] = ''
            writer.writerow(row)  #writing new row to output file

f.close()


