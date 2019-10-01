import sqlite3

try:
    # Openb database
    connection = sqlite3.connect('C:\\Users\\Home\\Desktop\\Automation\\Database.db')
    c = connection.cursor()
    print("DB connection succesful ")

except:
    print('Couldnt open the database')

username = input(str("Fill in your username: "))

c.execute("""SELECT * FROM main.naw WHERE naam = ?;""", (username,))
print(c.fetchall())

c.close()
connection.close()
