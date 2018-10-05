#Waffle -- Kevin Lin and Ahnaf Kazi
#SoftDev1 pd6
#K17 -- Average
#2018-10-06

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops
digd = {}

for row in c.execute("SELECT * FROM students"):
    studict = {}
    studict['name'] = row[0]
    studict['grades'] = []
    digd[row[2]] = studict
    
for studentid in digd.keys():
    for row in c.execute("SELECT mark FROM grades WHERE grades.id = %d" %(studentid)):
        digd[studentid]['grades'].append(row[1])

    lst = digd[studentid]['grades']
    avg = lst.sum()/len(lst)
    lst = avg
    print(digd[studentid][name] + ' ' + )
