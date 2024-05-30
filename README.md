# InventoryManagment
This Inventory Management System is a Python-based application that interacts with a MySQL database to manage product inventories. The system allows users to add, update, delete, and view products, check low stock levels, restock products, search products by name, and export the inventory to a CSV file.
Create a database named inventory_management_db.
    - Create a table named `products` with the following schema:
      sql
      CREATE TABLE products (
          id INT PRIMARY KEY,
          name VARCHAR(255),
          description TEXT,
          price DECIMAL(10, 2),
          quantity INT
      );

      
