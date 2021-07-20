import os
import glob

pwd = os.getcwd()
directory = pwd[:len(pwd) - 7] + "site\\TN-Nodejs-Production\\js-scripts"
called_tables = []
check_next_contents = False


def add_tables(tabls):
    if len(tabls) != 0:
        for table in tabls:
            table = table.strip()
            while table.endswith('"') or table.endswith("'") or table.endswith(",") or table.endswith(";"):
                table = table[: len(table) - 1]
                table.strip()
            if "." in table:
                table = table[: table.index('.')]
                table.strip()
            if len(table) != 0 and table not in called_tables:
                called_tables.append(table)


for file in glob.iglob(directory + '**/**', recursive=True):
    if os.path.isfile(file):
        with open(file, 'r') as f:
            contents = f.read().strip().replace('\n', ' ')
            tables = []
            for t in contents.split("SELECT ")[1:]:
                tables.append(t.split("FROM ")[1].strip().split()[0])
            add_tables(tables)

            tables = []
            for t in contents.split("INSERT INTO")[1:]:
                tables.append(t.split()[0])
            add_tables(tables)
            tables = []
            for t in contents.split("UPDATE")[1:]:
                if t.startswith(' rank') or t.startswith(' RELATION') or t.startswith(' note=?'):
                    continue
                tables.append(t.split()[0])
            add_tables(tables)
            tables = []
            for t in contents.split("DELETE FROM ")[1:]:
                tables.append(t.split()[0])
            add_tables(tables)

for t in called_tables:
    print(t)
print(len(called_tables))