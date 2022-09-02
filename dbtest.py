import sqlite3

verbindung = sqlite3.connect("/home/f.ulmer/PycharmProjects/pythonProject8/datenbank/geburtstage.db")
zeiger = verbindung.cursor()

nachname = "Schiller"
vorname = "Friedrich"
geburtstag = "10.11.1759"

sql_anweisung = """
CREATE TABLE IF NOT EXISTS personen (
vorname VARCHAR(20), 
nachname VARCHAR(30), 
geburtstag DATE
);"""

zeiger.execute("""
                INSERT INTO PERSONEN
                    VALUES(?,?,?)
                """,
               (vorname, nachname, geburtstag)
               )
"""Datenbank vor injections oder ausspähen schützen"""

sql_anweisung = """
INSERT INTO personen VALUES ('Johann Wolfgang von', 'Goethe', '28.8.1749')
"""
"""anfällig für angriffe."""

zeiger.execute("SELECT * FROM personen")
inhalt = zeiger.fetchall()
print(inhalt)

verbindung.commit()
verbindung.close()

