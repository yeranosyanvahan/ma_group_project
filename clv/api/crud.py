# crud.py

from sqlalchemy.orm import Session

def read(db: Session, model, condition):
    """

    Parameters
    ----------
    db: Session :
        
    model :
        
    condition :
        

    Returns
    -------

    """
    return db.query(model).filter(condition).first()

def create(db: Session, model, obj_data: dict):
    """

    Parameters
    ----------
    db: Session :
        
    model :
        
    obj_data: dict :
        

    Returns
    -------

    """
    obj = model(**obj_data)
    db.add(obj)
    db.commit()
    db.refresh(obj)
    return obj

def update(db: Session, model, model_id: int, obj_data: dict):
    """

    Parameters
    ----------
    db: Session :
        
    model :
        
    model_id: int :
        
    obj_data: dict :
        

    Returns
    -------

    """
    obj = db.query(model).filter(model.id == model_id).first()
    if obj:
        for key, value in obj_data.items():
            setattr(obj, key, value)
        db.commit()
        db.refresh(obj)
        return obj
    return None

def delete(db: Session, model, model_id: int):
    """

    Parameters
    ----------
    db: Session :
        
    model :
        
    model_id: int :
        

    Returns
    -------

    """
    obj = db.query(model).filter(model.id == model_id).first()
    if obj:
        db.delete(obj)
        db.commit()
        return True
    return False