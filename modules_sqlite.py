"""
    # Copyright © 2022 By Nguyễn Phú Khương
    # ZALO : 0363561629
    # Email : dev.phukhuong0709@hotmail.com
    # Github : npk-0709
"""
import sqlite3


class SQLite:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_table(self, table_name, columns):
        """
        Tạo một bảng mới

        :param table_name: Tên bảng
        :param columns: Danh sách các cột và kiểu dữ liệu (ví dụ: [('id', 'INTEGER PRIMARY KEY'), ('name', 'TEXT')])
        """
        columns_str = ', '.join([f'{col[0]} {col[1]}' for col in columns])
        create_table_sql = f'CREATE TABLE IF NOT EXISTS {table_name} ({columns_str})'
        self.cursor.execute(create_table_sql)
        self.conn.commit()

    def insert_data(self, table_name, data):
        """
        Thêm dữ liệu vào bảng

        :param table_name: Tên bảng
        :param data: Dữ liệu để thêm (ví dụ: {'name': 'John Doe', 'age': 25})
        """
        columns_str = ', '.join(data.keys())
        values_str = ', '.join(['?' for _ in data.values()])
        insert_data_sql = f'INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})'
        self.cursor.execute(insert_data_sql, tuple(data.values()))
        self.conn.commit()

    def select_data(self, table_name, condition=None):
        """
        Truy vấn dữ liệu từ bảng

        :param table_name: Tên bảng
        :param condition: Điều kiện truy vấn (ví dụ: 'age > 21')
        :return: Kết quả truy vấn
        """
        condition_str = f' WHERE {condition}' if condition else ''
        select_data_sql = f'SELECT * FROM {table_name}{condition_str}'
        self.cursor.execute(select_data_sql)
        return self.cursor.fetchall()

    def close_connection(self):
        """Đóng kết nối đến cơ sở dữ liệu"""
        self.conn.close()


if __name__ == '__main__':
    db = SQLite('example.db')
    db.create_table(
        'users', [('id', 'INTEGER PRIMARY KEY'), ('name', 'TEXT'), ('age', 'INTEGER')])
    db.insert_data('users', {'name': 'John Doe', 'age': 25})
    db.insert_data('users', {'name': 'Jane Doe', 'age': 30})
    result = db.select_data('users', 'age = 25')
    print(result)
    db.close_connection()
