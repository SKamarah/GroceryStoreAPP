from sql_connection import get_sql_connection


def get_all_products(connection):
    cursor = connection.cursor()

    query = (
        " SELECT Products.product_id, Products.Name, Products.unit_id, Products.price_per_unit, "
        "unit_table.unit_measure_name "
        "FROM Products inner join unit_table on Products.unit_id = unit_table.unit_id")

    cursor.execute(query)

    response = []

    for (product_id, name, unit_id, price_per_unit, unit_measure_name) in cursor:
        response.append(
            {
                'product_id': product_id,
                'name': name,
                'unit_id': unit_id,
                'price_per_unit': price_per_unit,
                'unit measure name': unit_measure_name
            }
        )

    return response


def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, unit_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['unit_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid


def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid


if __name__ == '__main__':
    connection = get_sql_connection()
    #print(get_all_products(connection))
    print(delete_product(connection, 7))
