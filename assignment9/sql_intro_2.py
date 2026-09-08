import sqlite3
from numpy import rint
import pandas as pd

# Task 2: Read data from lesson.db to a DataFrame
db_path = "../db/lesson.db"

try:
    with sqlite3.connect(db_path) as conn:
        sql_query = """
        SELECT 
            line_items.line_item_id, 
            line_items.quantity, 
            products.product_id, 
            products.product_name, 
            products.price
        FROM line_items
        JOIN products ON line_items.product_id = products.product_id
        """
        df = pd.read_sql_query(sql_query, conn)

    # Task 3: Print the first 5 rows of DataFrame
    print("\n First 5 rows of resulting dataframe:")
    print(df.head())

    # Task 4: add a column 'total'
    df['total'] = df['quantity'] * df['price']
    print("\n First 5 rows of updated dataframe:")
    print(df.head())

    # Task 5: Group by the product_id using agg
    df_summary = df.groupby('product_id').agg({
        'line_item_id': 'count',
        'total': 'sum',
        'product_name': 'first'
    }).reset_index()
    print("\n First 5 rows after groupby & agg: ")
    print(df_summary.head())


    # Task 6: Sort by product_name
    df_summary = df_summary.sort_values(by='product_name')
    print("\n First 5 rows after sorting by product_name: ")
    print(df_summary.head())

    # Task 7: Write summary to file
    df_summary.to_csv("order_summary.csv", index=False)
    print("\nFile 'order_summary.csv' created successfully.")


except sqlite3.Error as e:
    print(f"Database error: {e}")

# close the connection
conn.close()