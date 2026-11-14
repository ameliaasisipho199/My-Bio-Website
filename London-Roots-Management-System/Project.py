import sqlite3
from abc import ABC, abstractmethod
from datetime import datetime

def create_tables():
    conn = sqlite3.connect("london_roots.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Employee (
        employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        cell TEXT,
        email TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Customer (
        customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        surname TEXT,
        cell TEXT,
        email TEXT,
        billing_address TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Product (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        quantity INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Sales (
        sale_id INTEGER PRIMARY KEY AUTOINCREMENT,
        sale_date TEXT,
        product_name TEXT,
        sale_total REAL
    )
    """)

    conn.commit()
    conn.close()


# BASE CLASS 
class PersonManager(ABC):

    @abstractmethod
    def insert_person(self):
        pass

    @abstractmethod
    def remove_person(self):
        pass

    @abstractmethod
    def display_all(self):
        pass


# EMPLOYEE 
class EmployeeManager(PersonManager):

    def insert_person(self):
        conn = sqlite3.connect("london_roots.db")
        cursor = conn.cursor()

        name = input("Enter name: ")
        surname = input("Enter surname: ")
        cell = input("Enter cell: ")
        email = input("Enter email: ")

        cursor.execute("INSERT INTO Employee (name, surname, cell, email) VALUES (?, ?, ?, ?)",
                       (name, surname, cell, email))

        conn.commit()
        conn.close()
        print("Employee added!")

    def remove_person(self):
        conn = sqlite3.connect("london_roots.db")
        cursor = conn.cursor()

        emp_id = input("Enter employee ID: ")
        cursor.execute("DELETE FROM Employee WHERE employee_id=?", (emp_id,))

        conn.commit()
        conn.close()
        print("Employee removed!")

    def display_all(self):
        conn = sqlite3.connect("london_roots.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Employee")
        for emp in cursor.fetchall():
            print(emp)

        conn.close()


# CUSTOMER
class CustomerManager(PersonManager):

    def insert_person(self):
        conn = sqlite3.connect("london_roots.db")
        cursor = conn.cursor()

        name = input("Enter name: ")
        surname = input("Enter surname: ")
        cell = input("Enter cell: ")
        email = input("Enter email: ")
        address = input("Enter billing address: ")

        cursor.execute("INSERT INTO Customer (name, surname, cell, email, billing_address) VALUES (?, ?, ?, ?, ?)",
                       (name, surname, cell, email, address))

        conn.commit()
        conn.close()
        print("Customer added!")

    def remove_person(self):
        conn = sqlite3.connect("london_roots.db")
        cursor = conn.cursor()

        cust_id = input("Enter customer ID: ")
        cursor.execute("DELETE FROM Customer WHERE customer_id=?", (cust_id,))

        conn.commit()
        conn.close()
        print("Customer removed!")

    def display_all(self):
        conn = sqlite3.connect("london_roots.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Customer")
        for cust in cursor.fetchall():
            print(cust)

        conn.close()


# STORE
class Store:

    def addProduct(self):
        conn = sqlite3.connect("london_roots.db")
        cursor = conn.cursor()

        name = input("Product name: ")
        price = float(input("Price: "))
        quantity = int(input("Quantity: "))

        cursor.execute("INSERT INTO Product (name, price, quantity) VALUES (?, ?, ?)",
                       (name, price, quantity))

        conn.commit()
        conn.close()
        print("Product added!")

    def removeProduct(self):
        conn = sqlite3.connect("london_roots.db")
        cursor = conn.cursor()

        pid = input("Product ID: ")
        cursor.execute("DELETE FROM Product WHERE product_id=?", (pid,))

        conn.commit()
        conn.close()
        print("Product removed!")

    def updateProduct(self):
        conn = sqlite3.connect("london_roots.db")
        cursor = conn.cursor()

        pid = input("Product ID: ")
        price = float(input("New price: "))
        quantity = int(input("New quantity: "))

        cursor.execute("UPDATE Product SET price=?, quantity=? WHERE product_id=?",
                       (price, quantity, pid))

        conn.commit()
        conn.close()
        print("Product updated!")

    def displayProducts(self):
        conn = sqlite3.connect("london_roots.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Product")
        for p in cursor.fetchall():
            print(p)

        conn.close()

    def sellProduct(self):
        conn = sqlite3.connect("london_roots.db")
        cursor = conn.cursor()

        pid = input("Product ID: ")
        qty = int(input("Quantity: "))

        cursor.execute("SELECT name, price, quantity FROM Product WHERE product_id=?", (pid,))
        product = cursor.fetchone()

        if product:
            name, price, stock = product

            if stock == 0:
                print("Product out of stock!")
            elif qty > stock:
                print("Not enough stock!")
            else:
                total = price * qty
                new_stock = stock - qty

                cursor.execute("UPDATE Product SET quantity=? WHERE product_id=?",
                               (new_stock, pid))

                cursor.execute("INSERT INTO Sales (sale_date, product_name, sale_total) VALUES (?, ?, ?)",
                               (datetime.now(), name, total))

                conn.commit()
                print("Sale successful!")
        else:
            print("Product not found!")

        conn.close()

    def displaySales(self):
        conn = sqlite3.connect("london_roots.db")
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Sales")
        for sale in cursor.fetchall():
            print(sale)

        conn.close()


# MAIN MENU 
def main():
    create_tables()

    emp = EmployeeManager()
    cust = CustomerManager()
    store = Store()

    while True:
        print("\nWelcome to the Store Management System!")
        print("1. Manage Employees")
        print("2. Manage Customers")
        print("3. Manage Products")
        print("4. Manage Sales")
        print("\n0. Exit")

        choice = input("\nselect an option: ")

        # EMPLOYEES
        if choice == "1":
            while True:
                print("\n1. Add employee")
                print("2. Remove employee")
                print("3. Display employees")
                print("0. Return to main menu")

                ch = input("\nselect an option: ")

                if ch == "1":
                    emp.insert_person()
                elif ch == "2":
                    emp.remove_person()
                elif ch == "3":
                    emp.display_all()
                elif ch == "0":
                    break

        # CUSTOMERS
        elif choice == "2":
            while True:
                print("\n1. Add customer")
                print("2. Remove customer")
                print("3. Display customers")
                print("0. Return to main menu")

                ch = input("\nselect an option: ")

                if ch == "1":
                    cust.insert_person()
                elif ch == "2":
                    cust.remove_person()
                elif ch == "3":
                    cust.display_all()
                elif ch == "0":
                    break

        # PRODUCTS
        elif choice == "3":
            while True:
                print("\n1. Add a product")
                print("2. Remove a product")
                print("3. Update a product")
                print("4. Display all products")
                print("5. Sell a product")
                print("0. Return to main menu")

                ch = input("\nselect an option: ")

                if ch == "1":
                    store.addProduct()
                elif ch == "2":
                    store.removeProduct()
                elif ch == "3":
                    store.updateProduct()
                elif ch == "4":
                    store.displayProducts()
                elif ch == "5":
                    store.sellProduct()
                elif ch == "0":
                    break

        # SALES
        elif choice == "4":
            while True:
                print("\n1. Sell a product")
                print("2. Display all sales")
                print("0. Return to main menu")

                ch = input("\nselect an option: ")

                if ch == "1":
                    store.sellProduct()
                elif ch == "2":
                    store.displaySales()
                elif ch == "0":
                    break

        elif choice == "0":
            print("Goodbye!")
            break


main()