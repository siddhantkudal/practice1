# -*- coding: utf-8 -*-
"""
Created on Sat Jan  8 12:14:21 2022

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 17:37:44 2022

@author: User
"""
import mysql.connector

con = mysql.connector.connect(host="localhost", user="root", password="sidd@kudal27", database="ads")

# CREATE A CURSOR
c=con.cursor()
#CREATE A SALES TABLE
'''
c.execute("""CREATE TABLE cars(
car_name text,
color text,
car_size text,
quantity int )""")
'''
'''
many_types=[("Audi","Black","4Seater",2),
("Audi","Black","7Seater",1),
("Audi","white","4Seater",11),
("Audi","white","medium",9),
("Audi","white","7Seater",15),
("Audi","white","4Seater",2),
("Audi","Black","medium",5),
("BMW","Blue","medium",6),
("BMW","Blue","7Seater",12),
("BMW","pastel","4Seater",4),
("BMW","pastel","medium",3),
("BMW","pastel","7Seater",3),
("BMW","white","4Seater",2),
("BMW","white","medium",3),
("BMW","white","7Seater",0),
("Innova","Black","4Seater",2),
("Innova","Black","medium",6),
("Innova","Black","7Seater",6),
("Innova","Grey","medium",1),
("Innova","Grey","4Seater",4),
("Innova","Grey","7Seater",2),
("Innova","white","4Seater",17),
("Innova","white","medium",1),
("Innova","white","7Seater",10),
("Thar","red","4Seater",14),
("Thar","red","medium",6),
("Thar","red","7Seater",0),
("Thar","Black","4Seater",1),
("Thar","Black","medium",0),
("Thar","Black","7Seater",1),
("Thar","Black","4Seater",3),
("Thar","Black","4Seater",0),
("Thar","Black","4Seater",2)
]
#DISPLAY THE TABLE
c.executemany ("INSERT INTO cars VALUES (?,?,?,?)",
many_types)'''
c.execute("SELECT * FROM cars")
details=c.fetchall()
for det in details:
    print(det)

print("Roll up")
c.execute("SELECT car_name,SUM(quantity) FROM cars GROUP BY car_name WITH ROLLUP")
details=c.fetchall()
for det in details:
    print(det)
  

print("slicing")
temp1=input("Enter the car name:")
#c.execute("SELECT car_name,SUM(quantity) FROM cars WHERE car_name='Thar' GROUP BY car_name")
c.execute("SELECT car_name,SUM(quantity) FROM cars WHERE car_name='"+temp1+"' GROUP BY car_name")

result = c.fetchall()
print(result)


print("dicing")
name1=input("Enter the car name:")
name2=input("Enter the color:")
c.execute("SELECT car_name,SUM(quantity) FROM cars WHERE car_name='"+name1+"' AND color='"+name2+"' GROUP BY car_name")

result = c.fetchall()
print(result)

c.execute("SELECT car_name FROM cars PIVOT(sum(quantity) for (car_size) in ('4Seater','medium','7Seater'))")
result = c.fetchall()
print(result)

# COMMIT OUR COMMAND
con.commit()





con.close()

