import csv
# widh reader
with open('sample_employees.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)

# widh dicReader
with open('sample_employees.csv', mode='r') as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(row)


# with writer add row   
with open('sample_employees.csv', mode='a', newline='') as file:
    csv_writer = csv.writer(file)
    csv_writer.writerow(['John Doe', 'Engineering', 'john.doe@company.com'])
