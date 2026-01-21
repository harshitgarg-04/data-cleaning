#DATA CLEANING + CSV WRITE

import csv
with open("raw_students.csv", "r") as infile:
    reader = csv.reader(infile)
    header = next(reader)                                                         

    cleaned_data = []

    for row in reader:                                                            
        name = row[0]                                                             
        marks = row[1]                                                            
                                                                                  
        if marks == "":                                                           
            marks = "0"   # missing value handled                                 

        cleaned_data.append([name, marks])

with open("cleaned_students.csv", "w", newline="") as outfile:
    writer = csv.writer(outfile)
    writer.writerow(header)
    writer.writerows(cleaned_data)

print("Cleaned data saved to cleaned_students.csv")
