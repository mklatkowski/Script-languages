import sqlite3

# Połączenie z bazą danych
conn = sqlite3.connect('rentals_2023-06-04.db')
cursor = conn.cursor()


import datetime

def average_start_time(station_name):
    query = f"SELECT AVG((strftime('%s', end_time) - strftime('%s', start_time)) / 60) " \
            f"FROM rentals " \
            f"INNER JOIN stations ON rentals.rental_station = stations.id " \
            f"WHERE stations.station_name = '{station_name}'"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    return result

def average_end_time(station_name):
    query = f"SELECT AVG((strftime('%s', end_time) - strftime('%s', start_time)) / 60) " \
            f"FROM rentals " \
            f"INNER JOIN stations ON rentals.return_station = stations.id " \
            f"WHERE stations.station_name = '{station_name}'"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    return result



def count_unique_bikes(station_name):
    query = f"SELECT COUNT(DISTINCT bike_number) " \
            f"FROM rentals " \
            f"INNER JOIN stations ON rentals.rental_station = stations.id " \
            f"WHERE stations.station_name = '{station_name}'"
    cursor.execute(query)
    result = cursor.fetchone()[0]
    return result


def custom_query():
    query = "SELECT strftime('%H', start_time) AS hours, COUNT(*) AS num_rides " \
            "FROM rentals " \
            "GROUP BY hours " \
            "ORDER BY hours"
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def get_stations():
    query = "SELECT id, station_name FROM stations"
    cursor.execute(query)
    stations = cursor.fetchall()
    return stations


def display_stations(stations):
    for station in stations:
        print(f"{station[0]}. {station[1]}")

def main():
    stations = get_stations()
    display_stations(stations)

    station_name = input("Podaj nazwę stacji: ")

    result_a = average_start_time(station_name)
    result_b = average_end_time(station_name)
    result_c = count_unique_bikes(station_name)
    result_d = custom_query()

    print("Średni czas przejazdu rozpoczynanego nad daną stacją:", result_a, " minut")
    print("Średni czas przejazdu kończonego nad daną stacją:", result_b, "minut")
    print("Liczba różnych rowerów parkowanych nad daną stacją:", result_c)
    print("Liczba wypożyczeń, które były wykonywane o poszczególnych godzinach", result_d)

if __name__ == '__main__':

    main()
    conn.close()