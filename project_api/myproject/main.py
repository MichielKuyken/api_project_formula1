from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware
import secrets
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

import crud
import models
import schemas
from database import SessionLocal, engine
import os

if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

# "sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


security = HTTPBasic()


origins = [
    "https://michielkuyken.github.io/fomula1_api.github.io/",
    "file:///C:/Users/Eigenaar/Documents/2CCS/API%20development/API%20website/index.html"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_current_username(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    admin_user = crud.get_admin(db=db)
    current_username_bytes = credentials.username.encode("utf8")
    correct_username_bytes = admin_user.username.encode("utf8")
    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    correct_password_bytes = admin_user.password.encode("utf8")
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_username and is_correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username


@app.post("/admin/", response_model=schemas.Admin)
def create_admin(admin: schemas.AdminCreate, db: Session = Depends(get_db)):
    login = crud.get_admin_by_username(db, username=admin.username)
    if login:
        raise HTTPException(status_code=400, detail="Username already registred")
    return crud.create_admin(db=db, admin=admin)


@app.post("/drivers/", response_model=schemas.Driver)
def create_driver(driver: schemas.DriverCreate, db: Session = Depends(get_db)):
    driver_achternaam = crud.get_driver_by_last_name(db, achternaam=driver.achternaam)
    if driver_achternaam:
        raise HTTPException(status_code=400, detail="Last name already registred")
    return crud.create_driver(db=db, driver=driver)


@app.get("/drivers/", response_model=list[schemas.Driver])
def read_drivers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    drivers = crud.get_drivers(db, skip=skip, limit=limit)
    return drivers


@app.get("/drivers/{driver_achternaam}", response_model=schemas.Driver)
def read_driver(driver_achternaam: str, db: Session = Depends(get_db)):
    driver = crud.get_driver(db, driver_achternaam=driver_achternaam)
    if driver_achternaam is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return driver


@app.post("/grandprix/", response_model=schemas.Grandprix)
def create_grandprix(grandprix: schemas.GrandprixCreate, db: Session = Depends(get_db)):
    grandprix_circuitname = crud.get_grandprix_by_circuitname(db, circuitnaam=grandprix.circuitnaam)
    if grandprix_circuitname:
        raise HTTPException(status_code=400, detail="Circuit name already registred")
    return crud.create_grandprix(db=db, grandprix=grandprix)


@app.get("/grandprix/", response_model=list[schemas.Grandprix])
def read_grandprix(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    grandprix = crud.get_all_grandprix(db, skip=skip, limit=limit)
    return grandprix


@app.get("/grandprix/{grandprix_circuitnaam}", response_model=schemas.Grandprix)
def read_grandprix(grandprix_circuitnaam: str, db: Session = Depends(get_db)):
    grandprix = crud.get_grandprix(db, grandprix_circuitnaam=grandprix_circuitnaam)
    if grandprix_circuitnaam is None:
        raise HTTPException(status_code=404, detail="Grandprix not found")
    return grandprix


@app.post("/standings/", response_model=schemas.Standings)
def create_standings(standings: schemas.StandingsCreate, db: Session = Depends(get_db)):
    standings_last_name = crud.get_standings_by_lastname(db, achternaam=standings.achternaam)
    if standings_last_name:
        raise HTTPException(status_code=400, detail="Last name already registred")
    return crud.create_standings(db=db, standings=standings)


@app.get("/standings/", response_model=list[schemas.Standings])
def read_standings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    standings = crud.get_all_standings(db, skip=skip, limit=limit)
    return standings


@app.get("/standings/{standings_achternaam}", response_model=schemas.Standings)
def read_standings(standings_achternaam: str, db: Session = Depends(get_db)):
    standings = crud.get_standings_by_lastname(db, achternaam=standings_achternaam)
    if standings is None:
        raise HTTPException(status_code=404, detail="Standings not found")
    return standings


@app.delete("/drivers/{driver_achternaam}", response_model=schemas.Driver)
def delete_team(driver_achternaam: str, current_username: str = Depends(get_current_username), db: Session = Depends(get_db)):
    drivers = crud.get_driver(db, driver_achternaam=driver_achternaam)
    if not drivers:
        raise HTTPException(status_code=404, detail="Driver not found")
    return crud.delete_driver(db=db, driver=drivers)


@app.delete("/grandprix/{grandprix_circuitnaam}", response_model=schemas.Grandprix)
def delete_team(grandprix_circuitnaam: str, current_username: str = Depends(get_current_username), db: Session = Depends(get_db)):
    grandprix = crud.get_grandprix_by_circuitname(db, circuitnaam=grandprix_circuitnaam)
    if not grandprix:
        raise HTTPException(status_code=404, detail="Grandprix not found")
    return crud.delete_grandprix(db=db, grandprix=grandprix)


@app.delete("/standings/{standings_achternaam}", response_model=schemas.Standings)
def delete_team(standings_achternaam: str, current_username: str = Depends(get_current_username), db: Session = Depends(get_db)):
    standings = crud.get_standings_by_lastname(db, achternaam=standings_achternaam)
    if not standings:
        raise HTTPException(status_code=404, detail="Driver not found")
    return crud.delete_standings(db=db, standings=standings)


@app.delete("/admin/", response_model=schemas.Admin)
def delete_team(admin_username: str, current_username: str = Depends(get_current_username), db: Session = Depends(get_db)):
    admin = crud.get_admin_by_username(db, username=admin_username)
    if not admin:
        raise HTTPException(status_code=404, detail="Admin not found")
    return crud.delete_admin(db=db, admin=admin)


@app.put("/drivers/{driver_id}", response_model=schemas.Driver)
def update_driver(driver_update: schemas.DriverCreate, driver_id: int, current_username: str = Depends(get_current_username), db: Session = Depends(get_db)):
    driver = crud.get_driver_by_id(db, id=driver_id)
    if not driver:
        raise HTTPException(status_code=404, detail="Driver not found")
    updated_driver = crud.update_driver(db, driver, driver_update)
    return updated_driver


@app.put("/grandprix/{grandprix_id}", response_model=schemas.Grandprix)
def update_grandprix(grandprix_update: schemas.GrandprixCreate, grandprix_id: int, current_username: str = Depends(get_current_username), db: Session = Depends(get_db)):
    grandprix = crud.get_grandprix_by_id(db, id=grandprix_id)
    if not grandprix:
        raise HTTPException(status_code=404, detail="Grandprix not found")
    updated_grandprix = crud.update_grandprix(db, grandprix, grandprix_update)
    return updated_grandprix


@app.put("/standings/{standings_id}", response_model=schemas.Standings)
def update_standings(standings_update: schemas.StandingsCreate, standings_id: int, current_username: str = Depends(get_current_username), db: Session = Depends(get_db)):
    standings = crud.get_standings_by_id(db, id=standings_id)
    if not standings:
        raise HTTPException(status_code=404, detail="Standings not found")
    updated_standings = crud.update_standings(db, standings, standings_update)
    return updated_standings
