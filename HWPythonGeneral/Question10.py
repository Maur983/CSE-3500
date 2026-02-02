lines = []
with open("data.csv" )as f:
    lines = f.readlines()
headers = lines [0]
rows = lines [1:]
new_rows = []
for row in rows:
    name,birthday,year = row.strip().split(",")
    year = str(int(year)+1)
    new_rows.append(f"{name},{birthday},{year}\n")
with open("data.csv","w")as f:
    f.write(headers)
    f.writelines(new_rows)