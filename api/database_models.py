from sqlalchemy import create_engine, Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

Base = declarative_base()

# Define the engine first
database_url = "mysql+mysqldb://root@127.0.0.1:3306/internet_service_provider"
engine = create_engine(database_url)

# Now, define the session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Fact_Transacation(Base):
    __tablename__ = "fact_transacation"

    transaction_id = Column(Integer, primary_key=True, index=True)
    customer_id = Column(Integer, ForeignKey('dim_customer.customer_id'))
    payment_method_id = Column(Integer, ForeignKey('dim_payment_method.payment_method_id'))
    transaction_date = Column(DateTime)
    amount = Column(Float)
    
    customer = relationship("Dim_Customer", backref="transaction")
    payment_method = relationship("Dim_Payment_Method", backref="transaction")

class Dim_Payment_Method(Base):
    __tablename__ = "dim_payment_method"

    payment_method_id = Column(Integer, primary_key=True)
    payment_method_name = Column(String(255))

class Dim_Customer(Base):
    __tablename__ = "dim_customer"

    customer_id = Column(Integer, primary_key=True)
    age = Column(Integer)
    gender = Column(String(100))


if __name__ == "__main__":
    # Create the database tables
    Base.metadata.create_all(bind=engine)
