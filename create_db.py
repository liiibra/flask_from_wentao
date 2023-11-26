import sqlite3
import random
from datetime import datetime, timedelta

# 创建或连接到数据库
conn = sqlite3.connect('test_database.db')
cursor = conn.cursor()

# 创建表格
cursor.execute('''
    CREATE TABLE IF NOT EXISTS test_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date DATE,
        test_version TEXT,
        platform TEXT,
        pass_rate FLOAT,
        test_log_path TEXT,
        test_execution_timestamp INTEGER,
        data_upload_timestamp INTEGER
    )
''')

# 生成一些示例数据并插入表格
test_versions = ['v1.0', 'v2.0', 'v3.0', 'v4.0', 'v5.0']
platforms = ['Windows', 'Mac', 'Linux']
test_log_paths = ['/path/to/log1', '/path/to/log2', '/path/to/log3']

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

for _ in range(100):
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    test_version = random.choice(test_versions)
    platform = random.choice(platforms)
    pass_rate = round(random.uniform(50, 100), 2)
    test_log_path = random.choice(test_log_paths)
    test_execution_timestamp = int(date.timestamp())
    data_upload_timestamp = int((date + timedelta(hours=random.randint(1, 24))).timestamp())

    cursor.execute('''
        INSERT INTO test_results (date, test_version, platform, pass_rate, test_log_path, test_execution_timestamp, data_upload_timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (date.date(), test_version, platform, pass_rate, test_log_path, test_execution_timestamp, data_upload_timestamp))

conn.commit()
conn.close()

print("表格创建并数据插入成功！")
