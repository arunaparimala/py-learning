import csv
with open("/home/aruna/Downloads/ind_nifty50list.csv","r") as csv_file:
    details=csv_file.readlines()
    print(details)
    for line in details:
        print(line)



