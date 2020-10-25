import sqlite3
from student import student 
from classe import classe

mydb = sqlite3.connect("class.db")
mycursor = mydb.cursor()


try:
                    mycursor.execute('''
                    CREATE  TABLE students(                     
                        CIN INTEGER PRIMARY KEY ,
                        name IEXT(20),
                        nickName TEXT(20),
                        classe TEXT(20)
                        )
                    '''.format(student))
                    print('Table students  Created !'.format(student))
except Exception :
                    print('student exist insert data in it !')


def add(cin , name ,nickName , classe) :
    try:

        mycursor.execute('''Insert into students values({},"{}","{}","{}")'''.format(
                            cin,
                            name,
                            nickName,
                            classe))
        print (name + " been added")        
    except Exception as e :
        print(e)

def fetchall():
    rec= mycursor.execute("select * from students")
    fet = str(rec.fetchall())
    print(fet)

def fetch(a,cl):
    rec= mycursor.execute('''select {}  from students where classe = "{}"'''.format(a,cl) )
    fet = str(rec.fetchone())
    print(fet)
add(123,"khaled","khlifi","dsi")
fetch("cin","dsi")
mydb.commit()