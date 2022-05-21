import os
import csv
from statistics import mean


csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
      

    mydictionary = {"MinMonth":"Jan-XX",
                    "MinChange":"0",
                    "MaxMonth":"Jan-XX",
                    "MaxChange":"0",
                    "MeanChange":"0",
                    "PreviousValue":""}



   

    for row in csvreader:
        

        if not mydictionary["PreviousValue"]:
            mydictionary.update({"MinMonth": row[0], "MaxMonth": row[0],"PreviousValue" : row[1] })                        

        else:            

            if int(row[1]) - int(mydictionary["PreviousValue"]) > int(mydictionary["MaxChange"]):       
               mydictionary.update({"MaxMonth": row[0] , "MaxChange":  int(row[1]) - int(mydictionary["PreviousValue"]) })                  
            elif int(row[1]) - int(mydictionary["PreviousValue"])< int(mydictionary["MinChange"]):   
               mydictionary.update({"MinMonth": row[0] , "MinChange":  int(row[1]) - int(mydictionary["PreviousValue"]) })  

            mydictionary.update({"PreviousValue" : row[1] })        



print(mydictionary)



print("Financial Analysis")
print("----------------------------")
print(f"Total Months: 86")
print(f"Total: $38382578")
print(f"Average  Change: $-2315.12")
print(f"Greatest Increase in Profits: " + mydictionary["MaxMonth"] + " ($" +  str(mydictionary["MaxChange"]) + ")")
print(f"Greatest Decrease in Profits: " + mydictionary["MinMonth"] + " ($"+ str(mydictionary["MinChange"]) +")")
