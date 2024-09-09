import sqlite3

# Create a database in RAM
db = sqlite3.connect(':memory:')

# Get a cursor object
cursor = db.cursor()
cursor.execute('''
    CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
)''')


cursor.execute('''DELETE FROM Ages''')

# Insert users
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Tomasz', 39)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Annick', 36)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Ryhs', 29)''')
cursor.execute('''INSERT INTO Ages (name, age) VALUES ('Natalie', 34)''')

#Select user
cursor.execute('''SELECT hex(name || age) AS X FROM Ages ORDER BY X''')

#retrieve the first row
user1 = cursor.fetchone()
#Print the first column retrieved(user's name)
print("The first row in the resulting record set : "+user1[0])

#Commit changes into database
db.commit()
#Close database
db.close()