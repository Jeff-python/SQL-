import sqlite3
import csv


def create_table(dbname="employee.db"):
    with sqlite3.connect(dbname) as conn:
        cur = conn.cursor()

        SQL = """CREATE TABLE courses (
            pk INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR,
            cellphone VARCHAR,
            homephone VARCHAR,
            workphone VARCHAR,
            email VARCHAR,
            country VARCHAR
        );"""

        cur.execute(SQL)


tu = []
with open('employee.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        tu.append(row) 
        # "INSERT INTO courses(name, cellphone, homephone, workphone, email, country ) VALUES (?,?,?,?,?,?);"
        # cur.execute()
    



      


if __name__ == "__main__":
    create_table()