from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from database import Base


class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True, index=True)
    achternaam = Column(String, unique=True, index=True)
    voornaam = Column(String)
    land = Column(String)
    nummer = Column(Integer)
    team = Column(String)

    grandprix = relationship("Grandprix", back_populates="drivers")
    standings = relationship("Standings", back_populates="drivers")


class Grandprix(Base):
    __tablename__ = "grandprix"
    id = Column(Integer, primary_key=True, index=True)
    circuitnaam = Column(String, unique=True, index=True)
    land = Column(String)
    winnaar = Column(String)
    driver_id = Column(Integer, ForeignKey("drivers.id"))

    drivers = relationship("Driver", back_populates="grandprix")


class Standings(Base):
    __tablename__ = "standings"
    id = Column(Integer, primary_key=True, index=True)
    achternaam = Column(String, unique=True, index=True)
    voornaam = Column(String)
    punten = Column(Integer)
    driver_id = Column(Integer, ForeignKey("drivers.id"))

    drivers = relationship("Driver", back_populates="standings")


class Admin(Base):
    __tablename__ = "admins"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
