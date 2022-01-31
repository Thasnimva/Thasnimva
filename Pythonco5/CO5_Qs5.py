import csv
field_names=['ROLLNO','NAME','COURSE']

data=[{'ROLLNO':101,'NAME':'Thasni','COURSE':'MCA'},{'ROLLNO':102,'NAME':'Sithara','COURSE':'MCA'},{'ROLLNO':103,'NAME':'shirin','COURSE':'MCA'}]
with open('Details.csv','w', newline='')as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = field_names)
    writer.writeheader()
    writer.writerows(data)


with open('Details.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
