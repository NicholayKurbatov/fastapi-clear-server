from sqlalchemy import MetaData, Table, Column, Integer, String, JSON, ForeignKey


metadata = MetaData()

test_table = Table(
    'test', 
    metadata, 
    Column('id', Integer, primary_key=True),
    Column('info', String, nullable=True),
    Column('data', JSON, nullable=True), 
)