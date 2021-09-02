import sqlite3
import exceptions
from emp_cls import Employee
from validate import EmployeeValidator


conn = sqlite3.connect('employee.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS employees(name text,sal integer)")

def add_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES(?, ?)", (emp.name, emp.sal))

def get_emp_details():
    c.execute("SELECT rowid, * FROM employees")
    return c.fetchall()


create_table()

emp = Employee('arun', '300')

try:
    employee = EmployeeValidator.emp_validate(emp)
    if employee:
        add_emp(emp)
        print('\n Employee added successfully')

except exceptions.Error as e:
    print('\n', e)

conn.close()



# items = get_emp_details()
# for item in items:
#     print(item)


# def update_emp_details():
#     c.execute("UPDATE employees SET sal=3000 WHERE rowid=4")
#     conn.commit()
#
# def delete_emp():
#     c.execute("DELETE from employees WHERE rowid=5")
#     conn.commit()
#
# create_table()
#
# emp_obj = Employee('', 1020)
#
# if emp_validate(emp_obj):
#     add_emp(emp_obj)
#     print('Employee added successfully')



# add_emp(emp_obj)
# update_emp_details()
# delete_emp()







# def insert_emp(emp):
#     with conn:
#         c.execute("INSERT INTO employees VALUES(?, ?)", (emp_1.name, emp_1.sal))
#
# def get_detail():
#     c.execute("SELECT *FROM employees")
#     return c.fetchall()


# emp_1 = Employee('arc', 1250)
# insert_emp(emp_1)
# print(get_detail())

