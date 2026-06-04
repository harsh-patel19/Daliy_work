import csv
from myapp.models import *

with open('myapp/product.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        Product.objects.create(
            name = row['name'],
            qty = row['qty'],
            price = row['price'],
            image = row['image']

        )
print("Import data sucssfully")