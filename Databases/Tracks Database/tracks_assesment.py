import sqlite3

database = sqlite3.connect("track_assesment.sqlite")
pointer = database.cursor()

#Creating clean tables
pointer.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;
                      
CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
 ''')
#Open the file, slice it by rows and then divide the rows into an array with the different columns
file = open('tracks.csv')

for line in file:
    line = line.strip()
    columns = line.split(',')
    if len(columns)<6: continue

    title = columns[0]
    artist = columns[1]
    album = columns[2]
    count = columns[3]
    rating = columns[4]
    length =  columns[5]
    genre = columns[6]

    pointer.execute('INSERT OR IGNORE INTO Artist (name) VALUES (?)',(artist,))
    pointer.execute('SELECT id FROM Artist WHERE name = ?',  (artist,))
    artist_id = pointer.fetchone()[0]

    pointer.execute('INSERT OR IGNORE INTO Genre (name) VALUES (?)',(genre,))
    pointer.execute('SELECT id FROM Genre WHERE name = ?',  (genre,))
    genre_id = pointer.fetchone()[0]

    pointer.execute('INSERT OR IGNORE INTO Album (title, artist_id) VALUES (?,?)',(album,artist_id))
    pointer.execute("SELECT id FROM Album WHERE title = ?", (album,))
    album_id = pointer.fetchone()[0]

    pointer.execute("INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) VALUES (?,?,?,?,?,?)",
                    (title, album_id, genre_id, length , rating, count))
    
database.commit()



