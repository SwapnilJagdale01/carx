import MySQLdb

def run():
    # Open database connection ( If database is not created don't give dbname)
    db = MySQLdb.connect("127.0.0.1","root","" )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    # For creating create db
    # Below line  is hide your warning
    cursor.execute("SET sql_notes = 0; ")
    # create db here....
    cursor.execute("create database IF NOT EXISTS carxdb")
    # Commit your changes in the database
    db.commit()

    # disconnect from server
    db.close()
