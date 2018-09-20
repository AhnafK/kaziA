#Waffle -- Kevin Lin and Ahnaf Kazi
#SoftDev1 pd6
#K17 -- Average
#2018-10-06

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O

DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

for row in c.execute("SELECT * FROM students"):
    return type(row)
