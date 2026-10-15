import csv
with open("student.csv","r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)
        for row in reader:
            if int(row["SCORE"])>70:
                print(row) 