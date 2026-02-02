import csv

rows = []

with open( "data.csv", newline ="")as f:
    reader = csv.reader(f)
    headers = next(reader)
    for row in reader:
        row [2] = str (int(row[2]) + 1)
        rows.append(row)

with open ("new_data.csv" , " w " , newline = " " )as f:
    writer = csv.writer(f)
    writer. writerow (headers)
    writer.writerows(rows)