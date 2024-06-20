import sqlite3


def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(error)
    return connection


def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(f'Таблица: {error}')


def insert_products(connection, products):
    try:
        sql = '''
             INSERT INTO products 
             (product_title, price, quantity) 
             VALUES 
             (?, ?, ?)
             '''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as error:
        print(f'Добавление: {error}')


def update_quantity_products(connection, products):
    try:
        sql = '''
           UPDATE products SET quantity = ? 
           WHERE id = ?
             '''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as error:
        print(f'Изменение кол-ва: {error}')

def update_price_products(connection, products):
    try:
        sql = '''
           UPDATE products SET price = ? 
           WHERE id = ?
             '''
        cursor = connection.cursor()
        cursor.execute(sql, products)
        connection.commit()
    except sqlite3.Error as error:
        print(f'Изменение цены: {error}')

def delete_products(connection, id):
    try:
        sql = '''
           DELETE FROM products WHERE id = ?
             '''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as error:
        print(f'Удаление: {error}')

def select_all_products(connection):
    try:
        sql = '''
           SELECT * FROM products
           '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'Вывод всего в консоль: {error}')

def select_products(connection, limit):
    try:
        sql = '''
           SELECT * FROM products WHERE price <= ?
           '''
        cursor = connection.cursor()
        cursor.execute(sql, (limit,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'Выборка: {error}')

def search_products(connection, limit):
    try:
        sql = '''
           SELECT * FROM products WHERE product_title LIKE ?  
           '''
        cursor = connection.cursor()
        cursor.execute(sql, (limit,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'Поиск: {error}')


sql_to_create_products_table = '''
   CREATE TABLE products (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   product_title VARCHAR(200) NOT NULL,
   price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
   quantity INTEGER NOT NULL DEFAULT 0
);
'''
my_connection = create_connection('hw.db')
if my_connection is not None:
    create_table(my_connection, sql_to_create_products_table)
    insert_products(my_connection, ('Детское мыло', 61.5, 110))
    insert_products(my_connection, ('Хоз мыло', 25.4, 300))
    insert_products(my_connection, ('Шампунь + бальзам', 61.5, 110))
    insert_products(my_connection, ('Шампунь от перхоти', 61.5, 110))
    insert_products(my_connection, ('Шампунь для жирных волос', 105.5, 110))
    insert_products(my_connection, ('Шампунь для сухих волос', 61.5, 110))
    insert_products(my_connection, ('Шампунь для нормальных волос', 61.5, 110))
    insert_products(my_connection, ('Бальзам после мытья', 61.5, 110))
    insert_products(my_connection, ('Гель для душа ромашка', 120, 200))
    insert_products(my_connection, ('Гель для душа каштан', 120, 250))
    insert_products(my_connection, ('Гель для душа сирень', 120, 150))
    insert_products(my_connection, ('Гель для душа роза', 120, 150))
    insert_products(my_connection, ('Порошок', 100.3, 80))
    insert_products(my_connection, ('Порошок для белого', 100.3, 60))
    insert_products(my_connection, ('Порошок для черного', 100.3, 70))
    update_quantity_products(my_connection,(300, 2))
    update_price_products(my_connection, (75.99, 2))
    delete_products(my_connection, 2)
    select_all_products(my_connection)
    select_products(my_connection, 100)
    search_products(my_connection, '%мыло')

    print('Connection successful!')
    my_connection.close()
