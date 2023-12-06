import os
os.getcwd()

dir = '../Data/camion.csv'

with open (dir, 'rt', encoding='utf8') as f:
    headers = next(f).split(',')
    print(headers, end='')
    for line in f:
        row = line.split(',')
        print(row, end='')

















