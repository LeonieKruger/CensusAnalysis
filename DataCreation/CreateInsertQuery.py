import csv

openFile = open('/Users/leoniekruger/Downloads/VOCS2016-2017-HOUSEHOLD/VOCS2016-2017-HOUSEHOLD_F1.csv', 'r')
csvFile = csv.reader(openFile)
header = next(csvFile)
headers = map((lambda x: ''+x+'`'), header)
insert = 'INSERT INTO Table (' + ", ".join(headers) + ") VALUES "
for row in csvFile:
    values = map((lambda x: '"'+x+'"'), row)
    print (insert +" ("+ ", ".join(values) +");" )
openFile.close()