from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
from datetime import datetime, timedelta

# 创建数据库连接
engine = create_engine('sqlite:///test_database_sqlalchemy.db', echo=False)

# 声明基类
Base = declarative_base()

# 定义表格模型
class TestResult(Base):
    __tablename__ = 'test_results'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    test_version = Column(String)
    platform = Column(String)
    pass_rate = Column(Float)
    test_log_path = Column(String)
    test_execution_timestamp = Column(Integer)
    data_upload_timestamp = Column(Integer)

# 创建表格
Base.metadata.create_all(engine)

# 创建会话
Session = sessionmaker(bind=engine)
session = Session()

# 生成一些示例数据并插入表格
test_versions = ['v1.0', 'v2.0', 'v3.0']
platforms = ['Windows', 'Mac', 'Linux']
test_log_paths = ['/path/to/log1', '/path/to/log2', '/path/to/log3']

start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 12, 31)

for _ in range(10):
    date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    test_version = random.choice(test_versions)
    platform = random.choice(platforms)
    pass_rate = round(random.uniform(50, 100), 2)
    test_log_path = random.choice(test_log_paths)
    test_execution_timestamp = int(date.timestamp())
    data_upload_timestamp = int((date + timedelta(hours=random.randint(1, 24))).timestamp())

    test_result = TestResult(date=date, test_version=test_version, platform=platform, pass_rate=pass_rate,
                             test_log_path=test_log_path, test_execution_timestamp=test_execution_timestamp,
                             data_upload_timestamp=data_upload_timestamp)

    session.add(test_result)

# 提交数据并关闭会话
session.commit()
session.close()

print("表格创建并数据插入成功！")
