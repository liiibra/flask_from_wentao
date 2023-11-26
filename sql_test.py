from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
import time
# 创建一个 SQLite 数据库引擎
engine = create_engine('sqlite:///example.db')  # 这里的 echo=True 可以显示执行的 SQL 语句

# 声明一个基类
Base = declarative_base()

# 定义一个数据模型类
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

class TestResults(Base):
    __tablename__ = "sql_test"
    id = Column(Integer, primary_key=True)
    date = Column(DATE)
    test_version TEXT,
    platform TEXT,
    pass_rate FLOAT,
    test_log_path TEXT,
    test_execution_timestamp INTEGER,
    data_upload_timestamp INTEGER
    date, test_version, platform, pass_rate, test_log_path, test_execution_timestamp, data_upload_timestamp
# 创建表格
Base.metadata.create_all(engine)

surnames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller']
names = ['Emma', 'Noah', 'Olivia', 'Liam', 'Ava', 'William', 'Sophia', 'James', 'Amelia', 'Benjamin']

# 创建一个会话
Session = sessionmaker(bind=engine)
with Session() as session:
    for i in range(100):
        user = User(name=random.choice(surnames)+"_"+random.choice(names),age=i)
        session.add(user)

    # session.commit()

# 查询数据
t1 = time.time()
all_users = session.query(User).all()
print(time.time() - t1)
print(all_users)
# for user in all_users:
    # print(f"ID: {user.id}, Name: {user.name}, Age: {user.age}")

# 关闭会话
session.close()
