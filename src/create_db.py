import csv
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    Float,
    ForeignKey,
    create_engine,
    MetaData,
)
import sqlalchemy
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

pymysql.install_as_MySQLdb()
Base = sqlalchemy.orm.declarative_base()


sqlalchemy.engine.Engine._should_log_info = lambda self: False
sqlalchemy.engine.Engine._should_log_debug = lambda self: False


class Products(Base):
    __tablename__ = "products"

    product_number = Column("product_number", Integer, primary_key=True)
    product = Column("product", String(100))
    product_line = Column("product_line", String(100))
    product_type = Column("product_type", String(100))
    product_brand = Column("product_brand", String(100))
    product_color = Column("product_color", String(100))
    unit_cost = Column("unit_cost", Float)
    unit_price = Column("unit_price", Float)


class Retailers(Base):
    __tablename__ = "retailers"

    retailer_code = Column("retailer_code", Integer, primary_key=True)
    retailer_name = Column("retailer_name", String(100))
    type = Column("type", String(100))
    country = Column("country", String(100))


class Methods(Base):
    __tablename__ = "methods"

    order_method_code = Column("order_method_code", Integer, primary_key=True)
    order_method_type = Column("order_method_type", String(100))


class DailySales(Base):
    __tablename__ = "daily_sales"

    retailer_code = Column(
        "retailer_code", Integer, ForeignKey(Retailers.retailer_code)
    )
    order_method_code = Column(
        "order_method_code",
        Integer,
        ForeignKey(Methods.order_method_code),
    )
    product_number = Column(
        "product_number", Integer, ForeignKey(Products.product_number)
    )
    quantity = Column("quantity", Integer)
    date = Column("date", DateTime)
    unit_price = Column("unit_price", Float)
    unit_sale_price = Column("unit_sale_price", Float)

    __table_args__ = (
        sqlalchemy.PrimaryKeyConstraint(
            "order_method_code", "retailer_code", "product_number"
        ),
    )


class OneK(Base):
    __tablename__ = "onek"

    retailer_code = Column("retailer_code", Integer, primary_key=True)
    product_number = Column("product_number", Integer, primary_key=True)
    date = Column("date", DateTime)
    quantity = Column("quantity", Integer)

    __table_args__ = (
        sqlalchemy.PrimaryKeyConstraint(
            "retailer_code", "product_number", "quantity", "date"
        ),
    )


class CSV:
    def __init__(self, headers, rows):
        self.headers = headers
        self.rows = rows
        self.normalize_headers()

    def normalize_headers(self):
        self.headers = [x.lower().replace(" ", "_") for x in self.headers]

    def get_labled(self, id: int):
        return dict(zip(self.headers, self.rows[id]))


def get_csv(name):
    rows = []
    headers = []
    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                headers += row
                line_count += 1
            else:
                line_count += 1
                rows.append(row)
    return CSV(headers, rows)


def init_db():
    engine = create_engine(
        "mysql+mysqldb://user:password@0.0.0.0:8001/db", pool_recycle=3600, echo=True
    )
    conn = engine.connect()
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

    return conn, engine


def load_db(conn: sqlalchemy.engine.base.Connection):
    failure = False
    for table in [
        {"name": "datasets/go_methods.csv", "class": Methods},
        {"name": "datasets/go_products.csv", "class": Products},
        {"name": "datasets/go_retailers.csv", "class": Retailers},
        {"name": "datasets/go_daily_sales.csv", "class": DailySales},
        {"name": "datasets/go_1k.csv", "class": OneK},
    ]:
        csv_items = get_csv(table["name"])

        tuples_inserted = []
        tuples_skipped = 0

        for i in range(len(csv_items.rows)):
            items = csv_items.get_labled(i)

            if items.get("date") is not None:
                items["date"] = datetime.strptime(items["date"], "%d/%m/%Y")

            try:
                query = sqlalchemy.insert(table["class"]).values(items)
                res = conn.execute(query)

                tuples_inserted.append(res.inserted_primary_key_rows)
            except Exception as e:
                if e.orig.args[0] == 1062:  # Duplicate entry
                    tuples_skipped += 1
                    continue
                else:
                    # print(f"[ERROR] FAILED inserting {items} into {table['name']}: {e.orig.args}")
                    failure = True
                    break

        print(f"Inserted {len(tuples_inserted)} rows into {table['class'].__name__}")
        print(f"Skipped {tuples_skipped} duplicates")
        print(f"Last inserted was {tuples_inserted[:10]}...")

        if failure:
            print(f"[ERROR] Aborted!")
            break
        else:
            conn.commit()


def get_db_all(clss, conn):
    output = conn.execute(sqlalchemy.select(clss)).fetchall()
    return output


if __name__ == "__main__":
    conn = init_db()
    load_db(conn)
