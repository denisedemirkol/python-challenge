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
                    "PreviousValue":"",
                    "TotalAmount":"0"}

    changelist = []

    for row in csvreader:
        
        if not mydictionary["PreviousValue"]:
            mydictionary.update({"MinMonth": row[0], "MaxMonth": row[0],"PreviousValue" : row[1], "TotalAmount" : row[1] })                        
        else:            

            if int(row[1]) - int(mydictionary["PreviousValue"]) > int(mydictionary["MaxChange"]):       
               mydictionary.update({"MaxMonth": row[0] , "MaxChange":  int(row[1]) - int(mydictionary["PreviousValue"]) })                  
            elif int(row[1]) - int(mydictionary["PreviousValue"])< int(mydictionary["MinChange"]):   
               mydictionary.update({"MinMonth": row[0] , "MinChange":  int(row[1]) - int(mydictionary["PreviousValue"]) })  

            changelist.append (int(row[1]) - int(mydictionary["PreviousValue"]))
            mydictionary.update({"PreviousValue" : row[1] }) 
            mydictionary.update({"TotalAmount" : int(mydictionary["TotalAmount"])+int(row[1]) })       
            



print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {len(changelist)+1}")
print(f"Total: $"+ str(mydictionary["TotalAmount"]))
print(f"Average  Change: $" +str(   round(mean(changelist),2) ))
print(f"Greatest Increase in Profits: " + mydictionary["MaxMonth"] + " ($" +  str(mydictionary["MaxChange"]) + ")")
print(f"Greatest Decrease in Profits: " + mydictionary["MinMonth"] + " ($"+ str(mydictionary["MinChange"]) +")")
