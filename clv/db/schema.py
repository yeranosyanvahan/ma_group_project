import logging
import os

#from ..logger import CustomFormatter

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#ch.setFormatter(CustomFormatter())
logger.addHandler(ch)


from sqlalchemy import create_engine,Column,Integer,String,Float, DATE, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime



engine = create_engine('sqlite:///internet_service_provider.db')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Dim_Payment_Method(Base):
    """ """
    __tablename__ = "dim_payment_method"

    payment_method_id = Column(Integer, primary_key=True)
    payment_method_name = Column(String(255))


class Dim_Customer(Base):
    """ """
    __tablename__ = "dim_customer"

    customer_id = Column(Integer, primary_key=True)
    age = Column(Integer)
    gender = Column(String(100))


class Fact_Transacation(Base):
    """ """
    __tablename__ = "fact_transaction"

    transaction_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('dim_customer.customer_id'))
    payment_method_id = Column(Integer, ForeignKey('dim_payment_method.payment_method_id'))
    transaction_date = Column(DateTime)
    amount = Column(Float)

    customer = relationship("Dim_Customer", backref="transaction")
    payment_method = relationship("Dim_Payment_Method", backref="transaction")


class CLV_Prediction(Base):
    """ """
    __tablename__ = "clv_prediction"

    prediction_id = Column(Integer, autoincrement=True, primary_key=True)
    customer_id = Column(Integer, ForeignKey('dim_customer.customer_id'))
    clv = Column(Float)

Base.metadata.create_all(engine)