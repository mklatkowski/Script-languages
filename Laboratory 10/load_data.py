import csv
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from base import Base, Rentals, Stations


def load_data(csv_file, session):
    try:
        with open(csv_file, 'r', encoding='UTF-8') as file:
            reader = csv.reader(file)
            next(reader)
            i = 0
            for row in reader:
                rental = Rentals()
                rental.id = int(row[0])
                rental.bike_number = int(row[1])
                rental.start_time = datetime.strptime(row[2], '%Y-%m-%d %H:%M:%S')
                rental.end_time = datetime.strptime(row[3], '%Y-%m-%d %H:%M:%S')
                rental.rental_station = create_station(row[4], session)
                rental.return_station = create_station(row[5], session)
                session.add(rental)
                i+=1
                print(i)

            session.commit()
    except FileNotFoundError:
        print("Plik nie został znaleziony.")
    except IntegrityError:
        session.rollback()
        print("Błąd: Powtarzający się klucz główny. Dane mogą już istnieć w bazie danych." + row[0])
    except Exception as e:
        session.rollback()
        print("Wystąpił błąd podczas wczytywania danych:", str(e))
    finally:
        session.close()


def create_station(station_name, session):
    existing_station = session.query(Stations).filter_by(station_name=station_name).first()
    if existing_station:
        return existing_station.id

    new_station = Stations(station_name=station_name)
    session.add(new_station)
    session.commit()
    return new_station.id


if __name__ == '__main__':
    db_file = 'rentals_' + datetime.now().strftime('%Y-%m-%d') + '.db'
    engine = create_engine(f'sqlite:///{db_file}')
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    csv_file = input("Podaj ścieżkę do pliku CSV z historią przejazdów: ")
    load_data(csv_file, session)
