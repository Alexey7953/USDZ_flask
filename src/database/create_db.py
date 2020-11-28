import sqlite3

with sqlite3.connect('USDZ.db') as connection:
    cursor = connection.cursor()

    cursor.execute(
        "CREATE TABLE  users ("
        "id         INTEGER PRIMARY KEY AUTOINCREMENT,"
        "first_name      TEXT NOT NULL,"
        "last_name        TEXT NOT NULL,"
        "email      TEXT NOT NULL,"
        "password   TEXT NOT NULL,"
        "position    TEXT NOT NULL"
        ");"
    )

    cursor.execute(
        "CREATE TABLE  company ("
        "id         INTEGER PRIMARY KEY AUTOINCREMENT,"
        "company_name   TEXT NOT NULL,"
        "city   TEXT NOT NULL,"
        "address TEXT NOT NULL,"
        "phone_number TEXT NOT NULL,"
        "email TEXT NOT NULL,"
        "ITN     INTEGER NOT NULL,"
        "IEC     INTEGER NOT NULL,"
        "Note TEXT NOT NULL"
        ");"
    )

    cursor.execute(
        "CREATE TABLE  employees ("
        "id         INTEGER PRIMARY KEY AUTOINCREMENT,"
        "surname TEXT NOT NULL,"
        "firstname TEXT NOT NULL,"
        "based TEXT NOT NULL,"
        "authorized TEXT NOT NULL,"
        "position TEXT NOT NULL"
        ");"
    )

    cursor.execute(
        "CREATE TABLE  seminar ("
        "id         INTEGER PRIMARY KEY AUTOINCREMENT,"
        "price INTEGER,"        
        "number INTEGER,"        
        "amount INTEGER,"        
        "themes TEXT NOT NULL,"
        "when_seminar TEXT NOT NULL,"
        "place_seminar TEXT NOT NULL,"
        "workshop_leader TEXT NOT NULL,"
        "authorized TEXT NOT NULL,"
        "type_contract TEXT NOT NULL,"
        "notes TEXT NOT NULL"
        ");"
    )

