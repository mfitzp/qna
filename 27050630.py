import csv

mapper = dict()
with open('CSV1', 'r') as f1:
    reader = csv.reader(f1)
    for row in reader:
        # Column 3 contains the match; but we only want the left-most (before semi-colon)
        i = row[3].split(';')[0]
        # Column 4 contains the target value for output
        t = row[4]
        if i not in mapper:
            mapper[i] = t
        elif row[3] == row[4]:
            mapper[i] = t        
    
with open('CSV2', 'r') as f2:
    with open('FINAL_CSV', 'wb') as fo:
        reader = csv.reader(f2)
        writer = csv.writer(fo)
        for row in reader:
            if row[1] in mapper:
                row.append( mapper[ row[1] ] )
            writer.writerow(row)
    