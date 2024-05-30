import mysql.connector
from mysql.connector import Error
import csv

database_configuration = {
    'host': 'localhost',
    'database': 'inventory_managment_db',
    'user': 'root',
    'password': 'tiger'
}


conn = mysql.connector.connect(**database_configuration)
cursor = conn.cursor()

def add_product(id, name, description, price, quantity):
    try:
        cursor.execute("INSERT INTO products (id, name, description, price, quantity) VALUES (%s, %s, %s, %s, %s)", (id, name, description, price, quantity))
        conn.commit()
        print(f"Product '{name}' added successfully!")
    except Error as e:
        print(f"Error while adding product: {e}")
def update_product(id, name, description, price, quantity):
    try:
        cursor.execute("UPDATE products SET name=%s, description=%s, price=%s, quantity=%s WHERE id=%s", (name, description, price, quantity, id))
        conn.commit()
        print(f"Product '{name}' updated successfully!")
    except Error as e:
        print(f"Error while updating product: {e}")
def delete_product(id):
    try:
        cursor.execute("DELETE FROM products WHERE id=%s", (id,))
        conn.commit()
        print(f"Product with ID '{id}' deleted successfully!")
    except Error as e:
        print(f"Error while deleting product: {e}")

def view_products():
    try:
        cursor.execute("SELECT * FROM products")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except Error as e:
        print(f"Error while viewing products: {e}")
def search_p_by_name(name):
    try:
        cursor.execute("SELECT * FROM products WHERE name LIKE %s", (f'%{name}%',))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except Error as e:
        print(f"Error while searching for product by name: {e}")
def check_low_stock_products(amount):
    try:
        cursor.execute("SELECT * FROM products WHERE quantity < %s", (amount,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except Error as e:
        print(f"Error while checking low stock products: {e}")
def view_products_by_id(id):
    try:
        cursor.execute("SELECT * FROM products WHERE id=%s", (id,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        return rows
    except Error as e:
        print(f"Error while viewing product by ID: {e}")
def restock_products(id, quantity):
    try:
        cursor.execute("UPDATE products SET quantity=quantity+%s WHERE id=%s", (quantity, id))
        conn.commit()
        print("Stock updated successfully")
    except Error as e:
        print(f"Error while restocking product: {e}")
def export_inventory_to_csv(filename):
    products = view_products()
    if products:
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['ID', 'Name', 'Description', 'Price', 'Quantity'])
            for product in products:
                writer.writerow(product)
        print(f"Inventory exported to {filename} successfully!")
    else:
        print("No products to export.")
def main():
    while True:
        print("\nInventory Management System")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. View Products")
        print("5. Search Product by Name")
        print("6. Check Low Stock Products")
        print("7. View Product Details")
        print("8. Restock Product")
        print("9. Export Inventory to CSV")
        print("10. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            id = int(input("Enter product ID: "))
            name = input("Enter product name: ")
            description = input("Enter product description: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            add_product(id, name, description, price, quantity)
        elif choice == '2':
            id = int(input("Enter id of product to update: "))
            name = input("Enter new name of product: ")
            description = input("Enter the new description of product: ")
            price = float(input("Enter the new price of product: "))
            quantity = int(input("Enter the new quantity of product: "))
            update_product(id, name, description, price, quantity)
        elif choice == '3':
            id = int(input("Enter the id of the product to delete: "))
            delete_product(id)
        elif choice == '4':
            view_products()
        elif choice == '5':
            name = input("Enter the name of the product to search: ")
            search_p_by_name(name)
        elif choice == '6':
            amount = int(input("Enter the minimum stock limit to check: "))
            check_low_stock_products(amount)
        elif choice == '7':
            id = int(input("Enter the product id to see product details: "))
            view_products_by_id(id)
        elif choice == '8':
            id = int(input("Enter the ID of product to be restocked: "))
            quantity = int(input("Enter the product quantity: "))
            restock_products(id, quantity)
        elif choice == '9':
            filename = input("Enter the file name: ")
            export_inventory_to_csv(filename)
        elif choice == '10':
            break
        else:
            print("Invalid Choice. Please Try Again")

if __name__ == "__main__":
    main()

    if conn:
        cursor.close()
        conn.close()
