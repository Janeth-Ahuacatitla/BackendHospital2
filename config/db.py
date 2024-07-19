from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+pymysql://avnadmin:AVNS_kvzv7YJm8WMgNXqUyhK@mysql-19095702-utxicotepec-7f0b.d.aivencloud.com:15030/defaultdb"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base=declarative_base()