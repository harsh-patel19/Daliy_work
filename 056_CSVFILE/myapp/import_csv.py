import csv
from myapp.models import Employee

with open('myapp/product.csv', 'r',) as file:
    reader = csv.DictReader(file)

    for row in reader:
        Employee.objects.create(
            name=row['name'],
            dept=row['dept'],
            salary=row['salary']
        )

print("Data Imported Successfully")