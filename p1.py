from datetime import datetime
import mysql.connector
from p2 import generate_invoice

# totalInvoice = 0

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="invoice_generator"
        )
        if connection.is_connected():
            print("Connected to MySQL database")
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def update_company_counts():
    if db_connection:
        cursor = db_connection.cursor()
        
        # Get total product count from stock table
        cursor.execute("SELECT COUNT(*) FROM stock")
        total_products = cursor.fetchone()[0]
        
        # Get total sales count from sales table
        cursor.execute("SELECT COUNT(*) FROM sales")
        total_sales = cursor.fetchone()[0]
        
        # Update invoiceCount and productCount in ownCompany table
        update_query = "UPDATE ownCompany SET invoiceCount = %s, productCount = %s"
        cursor.execute(update_query, (total_sales, total_products))
        db_connection.commit()
        
        cursor.close()
        db_connection.close()
        print("Company counts updated successfully.")
        print("\n" + "-"*50 + "\n")

def change_company_details():
    print("Changing company details...")
    cursor = db_connection.cursor()
        
    # Fetch and display company details
    cursor.execute("SELECT * FROM ownCompany")
    company = cursor.fetchone()

    details = [
        ["companyName", company[1]],
        ["name", company[2]],
        ["GSTIN", company[3]],
        ["email", company[4]],
        ["mobileNum", company[3]],
        ["address", company[2]],
        
    ]

    for i in range(len(details)):
        print(f"Press 1. to change {details[i][0]}: {details[i][1]}")
        print("Press 0. to keep it same")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_value = input(f"Enter new {details[i][0]}: ")
            cursor.execute(f"UPDATE ownCompany SET {details[i][0]} = %s WHERE id = 1", (new_value,))
            db_connection.commit()
            print(f"{details[i][0]} updated successfully.")
            print("\n" + "-"*50 + "\n")

def add_customer_details():
    print("Adding customer details...")
    companyName = input("Enter company name: ")
    name = input("Enter customer name: ")
    mobileNum = input("Enter phone number: ")
    email = input("Enter email: ")
    gstNum = input("Enter GST number: ")
    address = input("Enter address: ")

    if db_connection:
        cursor = db_connection.cursor()
        query = "INSERT INTO customerDetails (companyName, name, mobileNum, email, GSTIN, address) VALUES (%s, %s, %s, %s, %s, %s)"
        values = (companyName, name, mobileNum, email, gstNum, address)
        cursor.execute(query, values)
        db_connection.commit()
        cursor.close()
        db_connection.close()
        print("Customer details added successfully.")
        print("\n" + "-"*50 + "\n")

def change_customer_details():
    print("Changing customer details...")
    cursor = db_connection.cursor()
        
    # Fetch and display all customers
    cursor.execute("SELECT id, name, companyName FROM customerDetails")
    customers = cursor.fetchall()
    print("Select a customer:")
    for customer in customers:
        print(f"{customer[0]}. {customer[1]} from {customer[2]}")
    customer_id = int(input("Enter customer ID: "))

    cursor.execute("SELECT * FROM customerDetails where id=%s", (customer_id,))
    customer = cursor.fetchone()

    details = [
        ["companyName", customer[1]],
        ["name", customer[2]],
        ["mobileNum", customer[3]],
        ["email", customer[4]],
        ["GSTIN", customer[5]],
        ["address", customer[6]]
    ]

    for i in range(len(details)):
        print(f"Press 1. to change {details[i][0]}: {details[i][1]}")
        print("Press 0. to keep it same")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_value = input(f"Enter new {details[i][0]}: ")
            cursor.execute(f"UPDATE customerDetails SET {details[i][0]} = %s WHERE id = %s", (new_value, customer_id))
            db_connection.commit()
            print(f"{details[i][0]} updated successfully.")
            print("\n" + "-"*50 + "\n")

def add_product_details():
    print("Adding product details...")
    product_name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    unit = input("Enter unit: ")
    price = float(input("Enter price: "))
    total_amount = quantity * price

    if db_connection:
        cursor = db_connection.cursor()
        query = "INSERT INTO stock (productName, quantity, unit, price, totalAmount) VALUES (%s, %s, %s, %s, %s)"
        values = (product_name, quantity, unit, price, total_amount)
        cursor.execute(query, values)
        db_connection.commit()
        cursor.close()
        db_connection.close()
        print("Product details added successfully.")
        print("\n" + "-"*100 + "\n")

def change_product_details():
    print("Changing product details...")
    cursor = db_connection.cursor()
        
    # Fetch and display all products
    cursor.execute("SELECT id, productName FROM stock")
    products = cursor.fetchall()
    print("Select a product:")
    print("\n" + "-"*50 + "\n")
    for product in products:
        print(f"{product[0]}. {product[1]}")
    print("\n" + "-"*50 + "\n")
    product_id = int(input("Enter product ID: "))
    print()

    cursor.execute("SELECT * FROM stock where id=%s", (product_id,))
    product = cursor.fetchone()

    details = [
        ["productName", product[1]],
        ["quantity", product[2]],
        ["unit", product[3]],
        ["price", product[4]],
    ]

    for i in range(len(details)):
        print("\n" + "-"*50 + "\n")
        print(f"Press 1. to change {details[i][0]}: {details[i][1]}")
        print("Press 0. to keep it same")
        print("\n" + "-"*50 + "\n")
        choice = int(input("Enter your choice: "))
        print()
        if choice == 1:
            new_value = input(f"Enter new {details[i][0]}: ")
            cursor.execute(f"UPDATE stock SET {details[i][0]} = %s, totalAmount={details[1][1]*details[3][1]} WHERE id = %s", (new_value, product_id))
            db_connection.commit()
            print(f"{details[i][0]} updated successfully.")
            print("\n" + "-"*50 + "\n")

def makeInvoice():
    print("\n" + "-"*100 + "\n")
    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()
        
        # Fetch and display all customers
        cursor.execute("SELECT id, name, companyName FROM customerDetails")
        customers = cursor.fetchall()
        print("Select a customer:")
        print("\n" + "-"*50 + "\n")        
        for customer in customers:
            print(f"{customer[0]}. {customer[1]} from {customer[2]}")
        print("\n" + "-"*50 + "\n")
        customer_id = int(input("Enter customer ID: "))
        print()
        
        # Fetch and display all products
        cursor.execute("SELECT id, productName FROM stock")
        products = cursor.fetchall()
        print("Select products:")
        selected_products = []
        while True:
            print("\n" + "-"*50 + "\n")
            for product in products:
                print(f"{product[0]}. {product[1]}")
            print("\n" + "-"*50 + "\n")
            product_id = int(input("Enter product ID (or 0 to finish): "))
            if product_id == 0:
                break
            quantity = int(input("Enter quantity: "))
            selected_products.append((product_id, quantity))
        
        # Generate invoice
        today_date = datetime.now().strftime("%d-%m-%Y")

        print("Enter the GST rate: ")
        gst_rate = int(input())
        print("Enter the discount: ")
        discount = int(input())
    
        cursor.execute("SELECT * FROM customerDetails where id=%s", (customer_id,))
        customer = cursor.fetchone()
        
        cursor.execute("SELECT COUNT(*) FROM sales")
        totalInvoice = cursor.fetchone()[0]


        generate_invoice(cursor, totalInvoice+1, today_date, customer[2], customer[6], customer[1], customer[4], customer[3], customer[5], selected_products, gst_rate, discount, f"invoice_{totalInvoice+1}.pdf")

        # Update product quantities in stock table and add sales details to sales table
        for product_id, quantity in selected_products:
            
            cursor.execute("SELECT productName, unit, price FROM stock WHERE id = %s", (product_id,))
            product = cursor.fetchone()
            total_amount = product[2] * quantity
            cursor.execute(
                "INSERT INTO sales (productName, productId, customerId, quantity, unit, price, gst, totalAmount, date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)",
                (product[0], product_id, customer_id, quantity, product[1], product[2], gst_rate, total_amount, today_date)
            )

            cursor.execute("UPDATE stock SET quantity = quantity - %s, totalAmount = totalAmount - %s WHERE id = %s", (quantity, total_amount, product_id))


        update_company_counts()
        
        db_connection.commit()
        cursor.close()
        db_connection.close()
        print("Invoice created, stock updated, and sales recorded successfully.")
        print()
        print("\n" + "-"*100 + "\n")

def changeOrAddComapnyCustomerOrProduct():
    while True:
        print()
        print("\n" + "-"*100 + "\n")
        print("Press 1. to change or edit in own company details")
        print("Press 2. to add customer details")
        print("Press 3. to change or edit in customer details")
        print("Press 4. to add product details")
        print("Press 5. to change or edit in product details")
        print("Press 6. to make invoice")
        print("Press 0. to exit")
        print("\n" + "-"*100 + "\n")
        print()
        choice = int(input("Enter your choice: "))
        print()
        if choice == 0:
            break
        switcher = {
            1: change_company_details,
            2: add_customer_details,
            3: change_customer_details,
            4: add_product_details,
            5: change_product_details,
            6: makeInvoice
        }
        
        func = switcher.get(choice, lambda: print("Invalid choice"))
        func()

# Example usage
if __name__ == "__main__":
    db_connection = connect_to_database()
    if db_connection:
        changeOrAddComapnyCustomerOrProduct()
        db_connection.close()

