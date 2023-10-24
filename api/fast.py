
from fastapi import FastAPI, Depends, HTTPException, status, File, UploadFile
from sqlalchemy.orm import Session
from database_models import Base, SessionLocal, engine, Fact_Transacation, Dim_Payment_Method, Dim_Customer
import crud
import csv

app = FastAPI()

def get_db():
    """ """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/transaction/")
def create_transaction(item_data: dict, db: Session = Depends(get_db)):
    """

    Parameters
    ----------
    item_data :
        dict:
    db :
        Session:  (Default value = Depends(get_db))
    item_data : dict :
        
    db : Session :
        (Default value = Depends(get_db))
    item_data: dict :
        
    db: Session :
         (Default value = Depends(get_db))

    Returns
    -------

    
    """
    return crud.create(db, Fact_Transacation, item_data)

@app.get("/transaction/{transaction_id}")
def get_transaction(transaction_id: int, db: Session = Depends(get_db)):
    """

    Parameters
    ----------
    transaction_id :
        int:
    db :
        Session:  (Default value = Depends(get_db))
    transaction_id : int :
        
    db : Session :
        (Default value = Depends(get_db))
    transaction_id: int :
        
    db: Session :
         (Default value = Depends(get_db))

    Returns
    -------

    
    """
    return crud.read(db, Fact_Transacation, transaction_id)

@app.put("/transaction/{transaction_id}")
def update_transaction(transaction_id: int, item_data: dict, db: Session = Depends(get_db)):
    """

    Parameters
    ----------
    transaction_id :
        int:
    item_data :
        dict:
    db :
        Session:  (Default value = Depends(get_db))
    transaction_id : int :
        
    item_data : dict :
        
    db : Session :
        (Default value = Depends(get_db))
    transaction_id: int :
        
    item_data: dict :
        
    db: Session :
         (Default value = Depends(get_db))

    Returns
    -------

    
    """
    updated_item = crud.update(db, Fact_Transacation, transaction_id, item_data)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return updated_item

@app.delete("/transaction/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    """

    Parameters
    ----------
    transaction_id :
        int:
    db :
        Session:  (Default value = Depends(get_db))
    transaction_id : int :
        
    db : Session :
        (Default value = Depends(get_db))
    transaction_id: int :
        
    db: Session :
         (Default value = Depends(get_db))

    Returns
    -------

    
    """
    success = crud.delete(db, Fact_Transacation, transaction_id)
    if not success:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"status": "success", "message": "Transaction deleted successfully"}

@app.post("/payment_method/")
def create_payment_method(item_data: dict, db: Session = Depends(get_db)):
    """

    Parameters
    ----------
    item_data :
        dict:
    db :
        Session:  (Default value = Depends(get_db))
    item_data : dict :
        
    db : Session :
        (Default value = Depends(get_db))
    item_data: dict :
        
    db: Session :
         (Default value = Depends(get_db))

    Returns
    -------

    
    """
    return crud.create(db, Dim_Payment_Method, item_data)

@app.get("/payment_method/{payment_method_id}")
def get_payment_method(payment_method_id: int, db: Session = Depends(get_db)):
    """

    Parameters
    ----------
    payment_method_id :
        int:
    db :
        Session:  (Default value = Depends(get_db))
    payment_method_id : int :
        
    db : Session :
        (Default value = Depends(get_db))
    payment_method_id: int :
        
    db: Session :
         (Default value = Depends(get_db))

    Returns
    -------

    
    """
    return crud.read(db, Dim_Payment_Method, payment_method_id)

@app.put("/payment_method/{payment_method_id}")
def update_payment_method(payment_method_id: int, item_data: dict, db: Session = Depends(get_db)):
    """

    Parameters
    ----------
    payment_method_id :
        int:
    item_data :
        dict:
    db :
        Session:  (Default value = Depends(get_db))
    payment_method_id : int :
        
    item_data : dict :
        
    db : Session :
        (Default value = Depends(get_db))
    payment_method_id: int :
        
    item_data: dict :
        
    db: Session :
         (Default value = Depends(get_db))

    Returns
    -------

    
    """
    updated_item = crud.update(db, Dim_Payment_Method, payment_method_id, item_data)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Payment Method not found")
    return updated_item

@app.delete("/payment_method/{payment_method_id}")
def delete_payment_method(payment_method_id: int, db: Session = Depends(get_db)):
    """

    Parameters
    ----------
    payment_method_id :
        int:
    db :
        Session:  (Default value = Depends(get_db))
    payment_method_id : int :
        
    db : Session :
        (Default value = Depends(get_db))
    payment_method_id: int :
        
    db: Session :
         (Default value = Depends(get_db))

    Returns
    -------

    
    """
    success = crud.delete(db, Dim_Payment_Method, payment_method_id)
    if not success:
        raise HTTPException(status_code=404, detail="Payment Method not found")
    return {"status": "success", "message": "Payment Method deleted successfully"}

@app.post("/customer/")
def create_customer(item_data: dict, db: Session = Depends(get_db)):
    """

    Parameters
    ----------
    item_data :
        dict:
    db :
        Session:  (Default value = Depends(get_db))
    item_data : dict :
        
    db : Session :
        (Default value = Depends(get_db))
    item_data: dict :
        
    db: Session :
         (Default value = Depends(get_db))

    Returns
    -------

    
    """
    return crud.create(db, Dim_Customer, item_data)

@app.get("/customer/{customer_id}")
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    """

    Parameters
    ----------
    customer_id :
        int:
    db :
        Session:  (Default value = Depends(get_db))
    customer_id : int :
        
    db : Session :
        (Default value = Depends(get_db))
    customer_id: int :
        
    db: Session :
         (Default value = Depends(get_db))

    Returns
    -------

    
    """
    return crud.read(db, Dim_Customer, customer_id)

@app.put("/customer/{customer_id}")
def update_customer(customer_id: int, item_data: dict, db: Session = Depends(get_db)):
    """

    Parameters
    ----------
    customer_id :
        int:
    item_data :
        dict:
    db :
        Session:  (Default value = Depends(get_db))
    customer_id : int :
        
    item_data : dict :
        
    db : Session :
        (Default value = Depends(get_db))
    customer_id: int :
        
    item_data: dict :
        
    db: Session :
         (Default value = Depends(get_db))

    Returns
    -------

    
    """
    updated_item = crud.update(db, Dim_Customer, customer_id, item_data)
    if not updated_item:
        raise HTTPException(status_code=404, detail="Customer not found")
    return updated_item

@app.delete("/customer/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    """

    Parameters
    ----------
    customer_id :
        int:
    db :
        Session:  (Default value = Depends(get_db))
    customer_id : int :
        
    db : Session :
        (Default value = Depends(get_db))
    customer_id: int :
        
    db: Session :
         (Default value = Depends(get_db))

    Returns
    -------

    
    """
    success = crud.delete(db, Dim_Customer, customer_id)
    if not success:
        raise HTTPException(status_code=404, detail="Customer not found")
    return {"status": "success", "message": "Customer deleted successfully"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)