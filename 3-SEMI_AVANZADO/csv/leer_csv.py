import csv 

with open('3-SEMI_AVANZADO/csv/archivo.csv') as archivo:
    reader= csv.reader(archivo)
    for row in reader: 
        print(row) 