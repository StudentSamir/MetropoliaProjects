from geopy import distance
import mysql.connector


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='ronaldo',
         autocommit=True
        )

def airport_distance(icao):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='" + icao + "'"
    cursor = yhteys.cursor()
    cursor.execute(sql)
    tulos = cursor.fetchall()
    return tulos

airport1 = input("Syötä 1.lentokentän ICAO-koodi:")
airport1_results = airport_distance(airport1)
airport2 = input("Syötä 2.lentokentän ICAO-koodi:")
airport2_results = airport_distance(airport2)

print(f"Lentokenttien välinen etäisyys on {distance.distance(airport1_results, airport2_results).km} kilometria.")
