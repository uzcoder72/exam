import psycopg2

db_name = 'n47'
password = '123'
host = 'localhost'
port = 5432
user = 'postgres'

with psycopg2.connect(dbname=db_name,
                      user=user,
                      password=password,
                      host=host,
                      port=port) as conn:
    with conn.cursor() as cur:
        create_table_query = """create table if not exists Product(
            id serial PRIMARY KEY,
            name varchar(70) not null unique,
            price int,
            color varchar(200),
            image varchar(250)
        );
        """
        cur.execute(create_table_query)
        conn.commit()
        print('Table Successfully Created')


def insert_products_data(name,price,color,image):
        connection = psycopg2.connect(
            host=host,
            database=db_name,
            user=user,
            password=password,
            port=port
        )
        cursor = connection.cursor()
        insert_query = '''
            INSERT INTO Product (name, price,color,image)
            VALUES (%s, %s, %s,%s);
        '''
        cursor.execute(insert_query, (name, price, color,image))
        connection.commit()
        print("Ma'lumot qo'shildi!")
# insert_products_data('Fridge',1000,'blue','https/image')
def select_all_products():
    connection = psycopg2.connect(
        host=host,
        database=db_name,
        user=user,
        password=password,
        port=port
    )
    cursor = connection.cursor()
    cursor.execute('Select * from Product')
    result=cursor.fetchall()
    for i in result:
        print(i)
# select_all_products()
def update_product_data():
    cursor = conn.cursor()

    sql = "UPDATE Product SET image = 'Canyon 123' WHERE id = 1"

    cursor.execute(sql)

    conn.commit()

    print(cursor.rowcount, " Update success")
# update_product_data()
def delete_product():
    cursor = conn.cursor()

    sql = "DELETE FROM Product WHERE id = 1"

    cursor.execute(sql)

    conn.commit()

    print(cursor.rowcount, " Delete success")
# delete_product()

class Alphabet:
    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def print_alphabet(self):
        for letter in self.alphabet:
            print(letter)
# alphabet_instance = Alphabet()
# alphabet_instance.print_alphabet()

import threading
import time

def print_numbers(start, end):
    for num in range(start, end + 1):
        print(num)

def print_letters():
    letters = 'ABCDE'
    for letter in letters:
        print(letter)
        time.sleep(1)

# if __name__ == "__main__":
    num_thread = threading.Thread(target=print_numbers, args=(1, 5))
    letter_thread = threading.Thread(target=print_letters)

    num_thread.start()
    letter_thread.start()

    num_thread.join()
    letter_thread.join()


import psycopg2

class Product:
    def __init__(self, name, price, color, image):
        self.name = name
        self.price = price
        self.color = color
        self.image = image

    def save(self):
        connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            password=password,
            host=host,
            port=port
        )
        cursor = connection.cursor()
        sql = '''INSERT INTO Product (name, price, color, image)
                 VALUES (%s, %s, %s, %s);
              '''
        val = (self.name, self.price, self.color, self.image)
        cursor.execute(sql, val)
        print("Malumotlar qo'shild")
        connection.commit()
        connection.close()


# iphone = Product(name="Iphone", price="500", color="red", image="https/image1")
# iphone.save()


import psycopg2

db_name = 'n47'
password = '123'
host = 'localhost'
port = 5432
user = 'postgres'

try:
    conn = psycopg2.connect(
        dbname=db_name,
        user=user,
        password=password,
        host=host,
        port=port
    )

    cur = conn.cursor()


    cur.execute("SELECT * FROM Product")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    conn.commit()

except psycopg2.Error as e:
    print(f"Error connecting to SQL: {e}")
finally:
    if conn:
        conn.close()


import psycopg2
conn = psycopg2.connect(
    host=host,
    database=db_name,
    user=user,
    password=password,
    port=port
)


cur = conn.cursor()


cur.execute("""
    INSERT INTO Product(name,price,color,image)
    VALUES (%s, %s, %s, %s)
""", ('Essence Mascara Lash Princess', 10,'Colorfull', 'https/image/product'))


conn.commit()

cur.close()
conn.close()

print("Data inserted successfully!")