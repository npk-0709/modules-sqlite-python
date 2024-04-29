# modules-sqlite-python
```python
from modules_sqlite import *
    db = SQLite('example.db')
    db.create_table(
        'users', [('id', 'INTEGER PRIMARY KEY'), ('name', 'TEXT'), ('age', 'INTEGER')])
    db.insert_data('users', {'name': 'John Doe', 'age': 25})
    db.insert_data('users', {'name': 'Jane Doe', 'age': 30})
    result = db.select_data('users', 'age = 25')
    print(result)
    db.close_connection()
```
