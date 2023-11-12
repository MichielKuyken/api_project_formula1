
from pydantic import BaseModel


class DriverBase(BaseModel):
    achternaam: str
    voornaam: str
    land: str
    team: str
    nummer: int


class DriverCreate(DriverBase):
    pass


class Driver(DriverBase):
    id: int

    class Config:
        orm_mode = True


class GrandprixBase(BaseModel):
    circuitnaam: str
    land: str
    winnaar: str | None = None
    driver_id: int | None = None


class GrandprixCreate(GrandprixBase):
    pass


class Grandprix(GrandprixBase):
    id: int

    class Config:
        orm_mode = True


class StandingsBase(BaseModel):
    achternaam: str
    voornaam: str
    punten: int
    driver_id: int


class StandingsCreate(StandingsBase):
    pass


class Standings(StandingsBase):
    id: int

    class Config:
        orm_mode = True


class AdminBase(BaseModel):
    username: str


class AdminCreate(AdminBase):
    password: str


class Admin(AdminBase):
    id: int

    class Config:
        orm_mode = True
