from flask import Flask, request
import json
import mysql.connector

app = Flask(__name__)

yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='ronaldo',
    autocommit=True
)

@app.route('/kentta/<icao>')
def kentta(icao):
    sql = f'select ident, name, municipality from airport where ident = "{icao}"'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    return (tulos)

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
