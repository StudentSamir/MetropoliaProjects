import mysql.connector


yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='ronaldo',
         autocommit=True
        )

maakoodi = input ("Syötä maakoodi:")

def haetyypit():
    sql = 'select distinct type from airport;'
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    return tulos

def haekenttienLKM(maakoodi, tyyppi):
    sql = '''select COUNT(type) from airport
    where iso_country = %s
    and type = %s '''
    kursori = yhteys.cursor()
    kursori.execute(sql, (maakoodi, tyyppi))
    tulos = kursori.fetchone()
    return tulos


tyypit = haetyypit()
#print('tyypit:', tyypit)

for tyyppi in tyypit:

    lkm = haekenttienLKM(maakoodi,tyyppi[0])
    print(f'{tyyppi [0]} lukumäärä ', lkm)

