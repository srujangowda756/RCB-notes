# import datetime
# d={1:{"product_name":"biscute","product_price":100,"brand_name":"parle","date":datetime.datetime.now()},2:{"product_name":"chacolate","product_price":12,"brand_name":"cadberry","date":datetime.datetime.now()}}
# backup_data={}


# def add_sales():
#     temp={}
#     product_name = input("Enter product name: ")
#     product_price = int(input("Enter product price: "))
#     brand_name=input("Enter brand name: ")
#     date=datetime.datetime.now()

#     temp["product_name"] = product_name
#     temp["product_price"] = product_price
#     temp["brand_name"] = brand_name
#     temp["date"] = date
#     d[len(d)+1] = temp

# def view_sales():
#     sales_id = int(input("Enter sales id: "))
#     try:
#         print(d[sales_id])
#     except KeyError:
#         print("Sales id not found")
    
# def total_sales():
#     total = 0
#     for i in d:
#         total += d[i]["product_price"]
#     print("Total sales:", total)
#     print("Average sales:", total/len(d))

# def highest_and_lowest():
#     highest = float('-inf')
#     lowest = float('inf')
#     for i in d:
#         if d[i]["product_price"] > highest:
#             highest = d[i]["product_price"]
#         if d[i]["product_price"] < lowest:
#             lowest = d[i]["product_price"]
#     print("Highest sales:", highest)
#     print("Lowest sales:", lowest)

# def sort_the_sales():
#     li=[]
#     for i in d:
#         li.append([d[i]["product_price"],d[i]["product_name"]])
#     ans=sorted(li,key=lambda x: x[0])
#     for i in ans:
#         print(i[1],i[0])

# def monthy_sales():
#     monthly_sales = {"jan":0,"feb":0,"mar":0,"apr":0,"may":0,"jun":0,"jul":0,"aug":0,"sep":0,"oct":0,"nov":0,"dec":0}
#     for i in d:
#         monthly_sales[d[i]["date"].strftime("%b").lower()] += d[i]["product_price"]
#     for i in monthly_sales:
#         print(i,"==", monthly_sales[i])


# while True:
#     print("1.Add sales\n2.View sales\n3.Display total and avg sales\n4.Highest and lowest sales \n5.sort the sales\n6.Search the sales \n7.Generate the bussiess insights\n8.Monthy summary\n9.Back up data\n10.Clear data\n11.Exit")
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         add_sales()
#     elif choice == 2:
#         view_sales()
#     elif choice == 3:
#         total_sales()
#     elif choice == 4:
#         highest_and_lowest()
#     elif choice==5:
#         sort_the_sales()
#     elif choice==6:
#         view_sales()
#     elif choice==7:
#         total_sales()
#         highest_and_lowest()
#     elif choice==8:
#         monthy_sales()            
#     elif choice==9:
#         backup_data = d.copy()
#         print("Data backed up successfully")
#     elif choice==10:
#         d.clear()
#         print("Data cleared successfully")
#     elif choice==11:
#         break
#     else:
#         print("Invalid choice")










"A robot must plan using obstacal detector and enery optimizer both with plan_path paranthesis"


class ObstacleDetection:
    def plan_path(self):
        return "obstacle detection"
    

class EnergyOptimizer:
    def plan_path(self):
        return "Energy optimizer"

class SmartRobot(ObstacleDetection,EnergyOptimizer):
    def __init__(self):
        self.object=ObstacleDetection.plan_path(self)
        self.energy=EnergyOptimizer.plan_path(self)
    def __str__(self):
        return f"Combinig {self.object} and { self.energy }"

r=SmartRobot()
print(r)


