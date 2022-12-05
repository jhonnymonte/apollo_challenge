import csv

with open('./data.csv','rt', encoding='utf8') as f:
    rows = csv.reader(f)
    headers = next(rows)
    colesterol = []
    sugar = []
    hipertrofia=[]
    line = 0
    for row in rows:
        line = line + 1
        if float(row[4]) >= 240 and float(row[0])>40:
            colesterol.append(row)
        if float(row[4]) >= 240 and float(row[0])>40 and float(row[5])==1.0:
            sugar.append(row)
        if float(row[4]) >= 240 and float(row[5])==1.0 and float(row[6])==2.0:
            hipertrofia.append(row)
        
            
promedio_sugar = 100*len(sugar)/line
promedio_colesterol = 100*len(colesterol)/line
promedio_hipertrofia = 100*len(hipertrofia)/line
            
            
            