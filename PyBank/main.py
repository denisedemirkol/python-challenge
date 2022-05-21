import os
import csv
from statistics import mean


csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
      

    changelist = []
    prevvalue = 0    
    l_change = 0
    
    for row in csvreader:
        
        #changelist.append(row)
        #changelist.append((row[0],row[1]))

        if not prevvalue:
            prevvalue = row[1]
            changelist.append((row[0],row[1],"0"))
        else:            
            l_change = int(prevvalue) - int(row[1])
            changelist.append((row[0],row[1],l_change))
            prevvalue = row[1]

print(changelist)
#changelist.append(zip(row[0],row[1]))