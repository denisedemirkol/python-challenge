import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    electiondata = {}      

    for row in csvreader:
        if not electiondata:            
            electiondata = {row[2]:1}
        else:
            if row[2] in electiondata:
                electiondata.update({row[2]:  int(electiondata[row[2]])+1 })       
            else:
                electiondata [row[2]] =1

    totalvotes = sum(electiondata.values())   

    outputlines = []
    outputlines.append ("Election Results")
    outputlines.append ("----------------------------")
    outputlines.append (f"Total Votes: {totalvotes}")
    outputlines.append ("----------------------------")


    l_perc = 0.00    
    l_winner = ""
    for w in sorted(electiondata, key=electiondata.get, reverse=True):        
        l_perc =  ((electiondata[w] / totalvotes * 100))
        formatted = '{0:.3f}'.format(l_perc)
        outputlines.append (f"{w} : %{formatted} ({electiondata[w]})")
        if not l_winner:
            l_winner = w
        
    outputlines.append ("----------------------------")
    outputlines.append (f"Winner : {l_winner}")
    outputlines.append ("----------------------------")


    output_path = os.path.join( "Analysis", "Analysis.txt")
    with open(output_path, 'w', newline='') as textfile:


        for line in outputlines:
            textfile.write(line)
            textfile.write('\n')
            print(line)        
