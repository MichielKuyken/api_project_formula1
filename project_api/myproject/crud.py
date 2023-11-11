from sqlalchemy.orm import Session

import models
import schemas


def get_driver(db: Session, driver_achternaam: str):
    return db.query(models.Driver).filter(models.Driver.achternaam == driver_achternaam).first()


def get_driver_by_last_name(db: Session, achternaam: str):
    return db.query(models.Driver).filter(models.Driver.achternaam == achternaam).first()


def get_driver_by_id(db: Session, id: int):
    return db.query(models.Driver).filter(models.Driver.id == id).first()


def get_drivers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Driver).offset(skip).limit(limit).all()


def create_driver(db: Session, driver: schemas.DriverCreate):
    db_driver = models.Driver(**driver.dict())
    db.add(db_driver)
    db.commit()
    db.refresh(db_driver)
    return db_driver


def delete_driver(db: Session, driver: schemas.Driver):
    db.delete(driver)
    db.commit()
    return driver


def update_driver(db: Session, existing_driver: models.Driver, driver_update: schemas.DriverCreate):
    for key, value in driver_update.dict().items():
        setattr(existing_driver, key, value)
    db.commit()
    db.refresh(existing_driver)
    return existing_driver


def get_grandprix(db: Session, grandprix_circuitnaam: str):
    return db.query(models.Grandprix).filter(models.Grandprix.circuitnaam == grandprix_circuitnaam).first()


def get_grandprix_by_id(db: Session, id: int):
    return db.query(models.Grandprix).filter(models.Grandprix.id == id).first()


def get_grandprix_by_circuitname(db: Session, circuitnaam: str):
    return db.query(models.Grandprix).filter(models.Grandprix.circuitnaam == circuitnaam).first()


def get_all_grandprix(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Grandprix).offset(skip).limit(limit).all()


def create_grandprix(db: Session, grandprix: schemas.GrandprixCreate):
    db_grandprix = models.Grandprix(**grandprix.dict())
    db.add(db_grandprix)
    db.commit()
    db.refresh(db_grandprix)
    return db_grandprix


def delete_grandprix(db: Session, grandprix: schemas.Grandprix):
    db.delete(grandprix)
    db.commit()
    return grandprix


def update_grandprix(db: Session, existing_grandprix: models.Grandprix, grandprix_update: schemas.GrandprixCreate):
    for key, value in grandprix_update.dict().items():
        setattr(existing_grandprix, key, value)
    db.commit()
    db.refresh(existing_grandprix)
    return existing_grandprix


def get_standings(db: Session, standings_achternaam: str):
    return db.query(models.Standings).filter(models.Standings.achternaam == standings_achternaam).first()


def get_standings_by_id(db: Session, id: int):
    return db.query(models.Standings).filter(models.Standings.id == id).first()


def get_standings_by_lastname(db: Session, achternaam: str):
    return db.query(models.Standings).filter(models.Standings.achternaam == achternaam).first()


def get_all_standings(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Standings).offset(skip).limit(limit).all()


def create_standings(db: Session, standings: schemas.StandingsCreate):
    db_standings = models.Standings(**standings.dict())
    db.add(db_standings)
    db.commit()
    db.refresh(db_standings)
    return db_standings


def delete_standings(db: Session, standings: schemas.Standings):
    db.delete(standings)
    db.commit()
    return standings


def update_standings(db: Session, existing_standings: models.Standings, standings_update: schemas.StandingsCreate):
    for key, value in standings_update.dict().items():
        setattr(existing_standings, key, value)
    db.commit()
    db.refresh(existing_standings)
    return existing_standings


def get_admin(db: Session):
    return db.query(models.Admin).first()


def get_admin_by_username(db: Session, username: str):
    return db.query(models.Admin).filter(models.Admin.username == username).first()


def create_admin(db: Session, admin: schemas.AdminCreate):
    if len(db.query(models.Admin).all()) == 0:
        db_admin = models.Admin(username=admin.username, password=admin.password)
        db.add(db_admin)
        db.commit()
        db.refresh(db_admin)
        return db_admin
