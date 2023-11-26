from flask import Flask, render_template

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random
import time

# 创建一个 SQLite 数据库引擎
engine = create_engine(
    "sqlite:///test_database_sqlalchemy.db"
)  # 这里的 echo=True 可以显示执行的 SQL 语句

# 声明一个基类
Base = declarative_base()


# 定义一个数据模型类
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)


class TestResult(Base):
    __tablename__ = "test_results"

    id = Column(Integer, primary_key=True)
    date = Column(DateTime)
    test_version = Column(String)
    platform = Column(String)
    pass_rate = Column(Float)
    test_log_path = Column(String)
    test_execution_timestamp = Column(Integer)
    data_upload_timestamp = Column(Integer)


app = Flask(__name__)


@app.route("/")
def main_page():
    return "<p>This is the main page for results showing test</p>"


@app.route("/index")
def index():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        data = []
        all_results = session.query(TestResult).all()
        data = [
            {
                "id": result.id,
                "date": result.date,
                "test_version": result.test_version,
                "platform": result.platform,
                # "pass_rate": f'<a href="{result.test_log_path}">{result.pass_rate}</a>',
                "pass_rate": result.pass_rate,
                "test_log_path": result.test_log_path

            }
            for result in all_results 
        ]
        print(data)
    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
