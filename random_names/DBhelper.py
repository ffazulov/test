import sqlite3


class DBHelper:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        self.cursor.execute(query)
        self.conn.commit()

    def insert_data(self, table_name, values):
        placeholders = ", ".join("?" * len(values))
        query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.conn.commit()

    def fetch_data(self, table_name, conditions=None):
        query = f"SELECT * FROM {table_name}"
        if conditions:
            query += f" WHERE {conditions}"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def update_data(self, table_name, set_clause, conditions=None):
        query = f"UPDATE {table_name} SET {set_clause}"
        if conditions:
            query += f" WHERE {conditions}"
        self.cursor.execute(query)
        self.conn.commit()

    def delete_data(self, table_name, conditions=None):
        query = f"DELETE FROM {table_name}"
        if conditions:
            query += f" WHERE {conditions}"
        self.cursor.execute(query)
        self.conn.commit()

    def close(self):
        self.conn.close()


# Создание экземпляра класса DBHelper
db = DBHelper('test.db')

# Создание таблицы "users"
db.create_table('users', 'id INTEGER PRIMARY KEY, name TEXT, age INTEGER')

# Добавление новых пользователей
db.insert_data('users', (1, 'Alice', 25))
db.insert_data('users', (2, 'Bob', 30))
db.insert_data('users', (3, 'Charlie', 35))

# Извлечение данных из таблицы "users"
rows = db.fetch_data('users')
print(rows)  # [(1, 'Alice', 25), (2, 'Bob', 30), (3, 'Charlie', 35)]

# Обновление данных в таблице "users"
db.update_data('users', 'age = 40', 'name = "Bob"')

# Извлечение обновленных данных из таблицы "users"
rows = db.fetch_data('users')
print(rows)  # [(1, 'Alice', 25), (2, 'Bob', 40), (3, 'Charlie', 35)]

# Удаление данных из таблицы "users"
db.delete_data('users', 'name = "Charlie"')

# Извлечение обновленных данных из таблицы "users"
rows = db.fetch_data('users')
print(rows)  # [(1, 'Alice', 25), (2, 'Bob', 40)]

# Закрытие соединения с базой данных
db.close()