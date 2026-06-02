import csv

with open("sample.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['year','yeild (ton)','price(thousand rupees per ton)','rainfall (mm)','is_used_fertilizer'])
    writer.writerow(['2020','100','10','50','True'])
    writer.writerow(['2021','200','20','60','False'])
    writer.writerow(['2022','300','30','70','True'])
    writer.writerow(['2023','400','40','80','False'])
    writer.writerow(['2024','500','50','90','True'])
    writer.writerow(['2025','600','60','100','False'])

with open("sample.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

with open("sample.csv", "a", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['2026','700','70','110','True'])
    writer.writerow(['2027','800','80','120','False'])