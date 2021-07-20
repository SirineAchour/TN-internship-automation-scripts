import os
import csv

pwd = os.getcwd()
file = pwd[:len(pwd) - 7] + "scripts\\tables.txt"
referenced_tables = {}
tables_not_used_in_code = []

with open(file) as f:
    for line in f:
        referenced_tables[line.strip()] = 0

file = pwd[:len(pwd) - 7] + "scripts\\tn_tables_and_columns.csv"

with open(file) as f:
    data = [{k: str(v) for k, v in row.items()}
            for row in csv.DictReader(f, skipinitialspace=True)]

for el in data:
    if el['TABLE_NAME'] in referenced_tables.keys():
        if el['STATUS'] != "Not used":
            referenced_tables[el['TABLE_NAME']] = 2
        else:
            referenced_tables[el['TABLE_NAME']] = 1
    else:
        if el['TABLE_NAME'] not in tables_not_used_in_code:
            tables_not_used_in_code.append(el['TABLE_NAME'])

i = 0
print(
    '\033[1m' + '\033[91m' + "List of tables referenced in code but saved as 'Not used' in the excel sheet :" + '\033[0m')
for t in referenced_tables:
    if referenced_tables[t] == 1:
        print(t)
        i = i + 1
print('\033[91m' + "--TOTAL : " + str(i) + '\033[0m')

print()
print('\033[1m' + '\033[91m' + "List of tables in the excel sheet that are never referenced in the code:" + '\033[0m')
for t in tables_not_used_in_code:
    print(t)
print('\033[91m' + "--TOTAL : " + str(len(tables_not_used_in_code)) + '\033[0m')

print()
i = 0
print(
    '\033[1m' + '\033[91m' + "List of tables referenced in the code that aren't mentioned in the excel sheet:" + '\033[0m')
for t in referenced_tables:
    if referenced_tables[t] == 0:
        print(t)
        i = i + 1
print('\033[91m' + "--TOTAL : " + str(i) + '\033[0m')
