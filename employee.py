import mysql.connector
import matplotlib.pyplot as plt
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Arqi@3052",
     database="emp"
)
if con.is_connected():
    print("Database Connected Successfully")

import mysql.connector

con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Arqi@3052",
    database="emp"
)
cursor = con.cursor()
cursor.execute("SELECT * FROM employees")

for row in cursor.fetchall():
    print(row)
def add_employee():
    emp_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    post = input("Enter Post: ")
    salary = int(input("Enter Salary: "))

    cursor = con.cursor()

    sql = "INSERT INTO employees VALUES(%s,%s,%s,%s)"
    data = (emp_id, name, post, salary)

    cursor.execute(sql, data)
    con.commit()

    print("Employee Added Successfully")
#add_employee()


def remove_employee():
    emp_id = int(input("Enter Employee ID: "))

    if not check_employee(emp_id):
        print("Employee does not exist.")
        return

    cursor = con.cursor()

    sql = "DELETE FROM employees WHERE id=%s"
    data = (emp_id,)

    cursor.execute(sql, data)
    con.commit()

    cursor.close()

    print("Employee Removed Successfully")

def salary_chart():
    cursor = con.cursor()

    cursor.execute("SELECT name, salary FROM employees")
    data = cursor.fetchall()

    names = []
    salaries = []

    for row in data:
        names.append(row[0])
        salaries.append(row[1])

    plt.bar(names, salaries)

    plt.xlabel("Employees")
    plt.ylabel("Salary (₹)")
    plt.title("Employee Salary Comparison")

    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
    cursor.close()
salary_chart()
    

    