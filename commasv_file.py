import csv
with open("/home/aruna/Downloads/ind_nifty50list.csv","r")as csv_file:
    details=csv.reader(csv_file)
    print(details)
    for line in details:
        print(line)

with open("/home/aruna/Downloads/ind_nifty50list.csv","r")as csv_file:
    content=csv.DictReader(csv_file)
    print(content)
    for line in content:
        print(line)
