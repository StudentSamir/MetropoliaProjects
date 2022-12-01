from flask import Flask
import mysql.connector
def database(icao):
    yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='ronaldo',
    autocommit=True)

    tuple = (icao,)
    sql = '''SELECT name, municipality FROM airport
    WHERE ident = %s'''
    kursori = yhteys.cursor()
    kursori.execute(sql, tuple)
    tulos = kursori.fetchone()
    return tulos

app = Flask(__name__)

@app.route('/kentta/<icao>')
def kentta(icao):
    database(icao)

    answer = {
        "ICAO": icao, "Name": database(icao)[0], "municipality": database(icao)[1]
    }

    return answer

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
