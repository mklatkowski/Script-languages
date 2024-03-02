from typing import List, Optional
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, Date, ForeignKey, DateTime
from datetime import datetime


class Base(DeclarativeBase):
    pass


class Rentals(Base):
    __tablename__ = "rentals"
    id: Mapped[int] = mapped_column(primary_key=True)
    bike_number: Mapped[int] = mapped_column(Integer)
    start_time: Mapped[Optional[datetime]] = mapped_column(DateTime)
    end_time: Mapped[Optional[datetime]] = mapped_column(DateTime)
    rental_station: Mapped[Optional[int]] = mapped_column(ForeignKey("stations.id"))
    return_station: Mapped[Optional[int]] = mapped_column(ForeignKey("stations.id"))

    rental_station_rel: Mapped["Stations"] = relationship("Stations", foreign_keys=[rental_station])
    return_station_rel: Mapped["Stations"] = relationship("Stations", foreign_keys=[return_station])


class Stations(Base):
    __tablename__ = "stations"
    id: Mapped[int] = mapped_column(primary_key=True)
    station_name: Mapped[str] = mapped_column(String(60))

    def __repr__(self):
        return f'Stations(id={self.id}, name={self.station_name})'
