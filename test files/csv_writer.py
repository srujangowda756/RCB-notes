import csv
f=open('data.csv','w+',newline='')
writer=csv.writer(f,delimiter=',')
writer.writerows([['name','age','city'],['man',21,'America'],['woman',21,'America']])
f.seek(0,0)
reader=csv.DictReader(f,delimiter=',')
for row in reader:
    print(row)
f.close()