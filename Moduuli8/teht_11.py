import mysql.connector

def haeLentokentta(icao):
    tuple = (icao,)
    sql = '''SELECT name, municipality FROM airport
    WHERE ident = %s''';
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    return tulos;

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='ronaldo',
         autocommit=True
         )

kentta= haeLentokentta('00KS')
print('kentta:',kentta)
if kentta is not None:
    print(f'Nimi: {kentta[0]}, Kunta: {kentta[1]} ')