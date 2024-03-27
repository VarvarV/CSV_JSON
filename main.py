import csv
import json

with open('ikea.csv', encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';', quotechar='"')
    expensive = sorted(reader, key=lambda x: int(x['price']), reverse=True)

for record in expensive[:10]:
    print(record)

with open('ikea.json', 'w') as ikea_file:
    json.dump(expensive, ikea_file)