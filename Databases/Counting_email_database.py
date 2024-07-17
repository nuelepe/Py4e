import sqlite3

#Connect to a database from sqlite.
connector = sqlite3.connect('email_count.sqlite')
#Create a pointer to the connection of the database.
cursor = connector.cursor()

#Disconnect or drop the table if already exists
cursor.execute('DROP TABLE IF EXISTS Counts')

#Create the table with it's SCHEMA
cursor.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    org = email.split('@')[1]

    cursor.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cursor.fetchone()
    if row is None:
        cursor.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cursor.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org,))

connector.commit()    

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cursor.execute(sqlstr):
    print(str(row[0]), row[1])

cursor.close()