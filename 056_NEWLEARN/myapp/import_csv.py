import csv
from myapp.models import Product

with open('myapp/product.csv', 'r') as file:
    reader = csv.DictReader(file)

    for row in reader:
        Product.objects.create(
            name=row['name'],
            qty=row['qty'],
            price=row['price'],
            dec=row['dec'],
          
        )

print("Data Imported")