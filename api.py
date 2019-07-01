import scrython

import django

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "jreiss1923",
    password = "Bigbrain2@",
    database = 'mtg'
)

mycursor = mydb.cursor()

card = scrython.cards.Named(exact="Sorin, Lord of Innistrad")

id = card.multiverse_ids()[0]


mycursor.execute("insert into u_c_assc (user_id, card_id) values ('%s', '%s')" % ("1", str(id)))
mydb.commit()
print("committed")


