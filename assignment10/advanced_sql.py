import sqlite3


conn = sqlite3.connect("../db/lesson.db")
cursor = conn.cursor()


# Task 1: Complex JOINs with Aggregation
# Find the total price of each of the first 5 orders:
# - You need to join the orders table with the line_items table and the products table.  
# - You need to GROUP_BY the order_id.   
# - You need to select the order_id and the SUM of the product price times the line_item quantity.  
# - Then, you ORDER BY order_id and LIMIT 5.  

query = """
SELECT 
    o.order_id, 
    SUM(p.price * li.quantity) AS total_price
FROM orders o 
JOIN line_items li ON o.order_id = li.order_id 
JOIN products p ON li.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id
LIMIT 5;
"""

# Execute and fetch results
cursor.execute(query)
results = cursor.fetchall()
print(results)

# Task 2: Understanding Subqueries
# For each customer, find the average price of their orders:
# - You compute the price of each order as in part 1, but you return the customer_id and the total_price.  
# - That's the subquery. You need to return the total price using AS total_price, and you need to return the customer_id with AS customer_id_b.  
# - In your main statement, you left join the customer table with the results of the subquery, using ON customer_id = customer_id_b.  
# - You aliased the customer_id column in the subquery so that the column names wouldn't collide.  
# - Then group by customer_id -- this GROUP BY comes after the subquery -- and get the average of the total price of the customer orders.  
# - Return the customer name and the average_total_price.

query = """
SELECT 
    c.customer_name, 
    AVG(sub.total_price) AS average_total_price
FROM customers AS c
LEFT JOIN (
    SELECT 
        o.customer_id AS customer_id_b, 
        SUM(p.price * li.quantity) AS total_price
    FROM orders o 
    JOIN line_items li ON o.order_id = li.order_id 
    JOIN products p ON li.product_id = p.product_id
    GROUP BY o.customer_id
) AS sub 
ON c.customer_id = sub.customer_id_b
GROUP BY c.customer_id, c.customer_name;
"""
# Execute and fetch results
cursor.execute(query)
results = cursor.fetchall()
print(results)

# Task 3: An Insert Transaction Based on Data
# You want to create a new order for the customer named Perez and Sons.
# The employee creating the order is Miranda Harris. 
# The customer wants 10 of each of the 5 least expensive products. 
# - You first need to do a SELECT statement to retrieve the customer_id, 
# - another to retrieve the product_ids of the 5 least expensive products, 
# - and another to retrieve the employee_id.  
# - Then, you create the order record and the 5 line_item records comprising the order. 
# - You have to use the customer_id, employee_id, and product_id values you obtained from the SELECT statements. 
# - You have to use the order_id for the order record you created in the line_items records. 
# - The inserts must occur within the scope of one transaction. 
# - Then, using a SELECT with a JOIN, print out the list of line_item_ids for the order along with the quantity and product name for each.


conn.execute("PRAGMA foreign_keys = 1")
try:
    # SELECT statement to retrieve the customer_id
    query = """
        SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons';
    """
    customer_id_target = cursor.execute(query).fetchone()[0] 

    # SELECT statement to retrieve the product_ids of the 5 least expensive products
    query = """
        SELECT product_id FROM products ORDER BY price ASC LIMIT 5;
    """
    product_ids_target = [row[0] for row in cursor.execute(query).fetchall()]

    # SELECT statement to retrieve the employee_id
    query = """
        SELECT employee_id FROM employees WHERE first_name = 'Miranda' AND last_name = 'Harris';
    """
    employee_id_target = cursor.execute(query).fetchone()[0]

    # Create the order record
    query = """
        INSERT INTO orders (customer_id, employee_id, date) 
        VALUES (?, ?, date('now'))
        RETURNING order_id;
    """
    cursor.execute(query, (customer_id_target, employee_id_target))

    # Get the order_id of the newly created order
    order_id_target = cursor.fetchone()[0]

    # Create the 5 line_item records
    query = """
        INSERT INTO line_items (order_id, product_id, quantity) 
        VALUES (?, ?, ?);
    """
    for product_id in product_ids_target:
        cursor.execute(query, (order_id_target, product_id, 10))

    # Commit transaction
    conn.commit()  


    # Using a SELECT with a JOIN, print out the list of line_item_ids for the order along with the quantity and product name for each.
    query = """
        SELECT li.line_item_id, li.quantity, p.product_name
        FROM line_items li
        JOIN products p ON li.product_id = p.product_id
        WHERE li.order_id = ?;
    """
    cursor.execute(query, (order_id_target,))
    line_items = cursor.fetchall()
    print("\nLine items for the new order:")
    print(line_items)



except Exception as e:
    conn.rollback()  # Rollback transaction if there's an error
    print("Error:", e)


# Task 4: Aggregation with HAVING
# Find all employees associated with more than 5 orders.  
# - You want the first_name, the last_name, and the count of orders.  
# - You need to do a JOIN on the employees and orders tables, and then use GROUP BY, COUNT, and HAVING.

query = """
    SELECT e.employee_id,
        e.first_name,
        e.last_name,
        COUNT(o.order_id) AS order_count
    FROM employees AS e
    JOIN orders AS o ON e.employee_id = o.employee_id
    GROUP BY e.employee_id, e.first_name, e.last_name
    HAVING COUNT(o.order_id) > 5;
"""

# Execute and fetch results
cursor.execute(query)
results = cursor.fetchall()
print("\nEmployees with more than 5 orders:")
print(results)



conn.close()
